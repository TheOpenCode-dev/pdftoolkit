# PDFToolkit

A free online PDF tool for merging, splitting, and compressing PDF files.

## Quick Start

### Running Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Open http://localhost:5000 in your browser.

### Deployment

Deploy to Render.com:

1. Push to GitHub
2. Connect repo to Render
3. Configure:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

---

## How-to Guides

### How to Merge PDFs

1. Go to the Merge section
2. Drop multiple PDF files into the upload area
3. Click "Merge PDFs"
4. Download the merged file

### How to Split a PDF

1. Go to the Split section
2. Upload a PDF file
3. Enter pages to extract (e.g., `1,3-5,8`)
4. Click "Split PDF"
5. Download the split file

### How to Compress a PDF

1. Go to the Compress section
2. Upload a PDF file
3. Select quality (Low/Medium/High)
4. Click "Compress PDF"
5. Download the compressed file

---

## Reference

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page |
| `/merge` | POST | Merge multiple PDFs |
| `/split` | POST | Split PDF by page numbers |
| `/compress` | POST | Compress PDF with quality settings |
| `/status` | GET | Check rate limit usage |

### Environment Variables

None required for local development.

### Rate Limits

- **Free tier:** 3 uses per day
- **Paid tier:** Unlimited

---

## Explanation

### Why this tool?

PDFToolkit solves common PDF problems without installing software. Everything runs in the browser — your files are processed server-side and deleted after download.

### Architecture

- **Frontend:** Vanilla HTML/CSS/JS — no framework needed
- **Backend:** Flask with pypdf for PDF manipulation
- **Rate limiting:** In-memory tracking by IP address
- **Storage:** Temporary files with automatic cleanup

### Security

- Files are deleted immediately after processing
- No permanent storage
- Rate limiting prevents abuse