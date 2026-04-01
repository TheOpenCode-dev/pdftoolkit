#!/usr/bin/env python3
"""PDF Page Counter - Count pages in multiple PDFs."""

import sys
from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError:
    print("Install pypdf: pip install pypdf")
    sys.exit(1)

def count_pages(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        return len(reader.pages)
    except Exception as e:
        return f"Error: {e}"

def scan_folder(folder_path):
    folder = Path(folder_path)
    total = 0
    results = []
    
    for file in sorted(folder.glob('*.pdf')):
        pages = count_pages(file)
        if isinstance(pages, int):
            total += pages
            results.append((file.name, pages))
        else:
            results.append((file.name, pages))
    
    print(f"{'File':<40} {'Pages'}")
    print("-" * 50)
    for name, pages in results:
        print(f"{name:<40} {pages}")
    print("-" * 50)
    print(f"Total: {total} pages across {len(results)} files")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Count PDF pages')
    parser.add_argument('folder', help='Folder with PDFs')
    args = parser.parse_args()
    scan_folder(args.folder)