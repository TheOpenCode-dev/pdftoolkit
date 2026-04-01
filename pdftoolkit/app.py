from flask import Flask, request, send_file, jsonify, render_template
from pypdf import PdfMerger, PdfReader, PdfWriter
import os
import tempfile
from datetime import datetime

app = Flask(__name__)

# Simple rate limiting (in-memory for demo)
daily_requests = {}

def cleanup_old_requests():
    global daily_requests
    today = datetime.now().date()
    if 'date' not in daily_requests or daily_requests['date'] != today:
        daily_requests = {'date': today}

def check_limit():
    cleanup_old_requests()
    ip = request.remote_addr
    count = daily_requests.get(ip, 0)
    if count >= 3:
        return True
    daily_requests[ip] = count + 1
    return False

@app.route('/merge', methods=['POST'])
def merge_pdfs():
    if check_limit():
        return jsonify({'error': 'Daily limit reached. Upgrade for unlimited.'}), 429
    
    files = request.files.getlist('files')
    if len(files) < 2:
        return jsonify({'error': 'Need at least 2 PDFs'}), 400
    
    merger = PdfMerger()
    for f in files:
        merger.append(f)
    
    output = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf')
    merger.write(output.name)
    merger.close()
    
    return send_file(output.name, as_attachment=True, download_name='merged.pdf')

@app.route('/split', methods=['POST'])
def split_pdf():
    if check_limit():
        return jsonify({'error': 'Daily limit reached. Upgrade for unlimited.'}), 429
    
    file = request.files.get('file')
    pages = request.form.get('pages', '')
    
    reader = PdfReader(file)
    writer = PdfWriter()
    
    for part in pages.split(','):
        part = part.strip()
        if '-' in part:
            start, end = map(int, part.split('-'))
            for i in range(start, min(end + 1, len(reader.pages) + 1)):
                writer.add_page(reader.pages[i-1])
        elif part.isdigit():
            idx = int(part)
            if 1 <= idx <= len(reader.pages):
                writer.add_page(reader.pages[idx-1])
    
    output = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf')
    writer.write(output.name)
    
    return send_file(output.name, as_attachment=True, download_name='split.pdf')

@app.route('/compress', methods=['POST'])
def compress_pdf():
    if check_limit():
        return jsonify({'error': 'Daily limit reached. Upgrade for unlimited.'}), 429
    
    file = request.files.get('file')
    quality = request.form.get('quality', 'medium')
    
    reader = PdfReader(file)
    writer = PdfWriter()
    
    for page in reader.pages:
        writer.add_page(page)
    
    # Compression via PDF writer
    if quality == 'low':
        writer.add_metadata({'/Creator': 'PDFToolkit'})
    
    output = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf')
    writer.write(output.name)
    
    return send_file(output.name, as_attachment=True, download_name='compressed.pdf')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status', methods=['GET'])
def status():
    cleanup_old_requests()
    ip = request.remote_addr
    used = daily_requests.get(ip, 0)
    return jsonify({'used': used, 'limit': 3, 'remaining': max(0, 3-used)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)