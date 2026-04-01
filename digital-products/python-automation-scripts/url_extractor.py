#!/usr/bin/env python3
"""URL Extractor - Extract URLs from text/HTML files."""

import re
import sys
from pathlib import Path
from urllib.parse import urlparse

def extract_urls(file_path, unique=True):
    path = Path(file_path)
    content = path.read_text(errors='ignore')
    
    # Regex for URLs
    url_pattern = re.compile(r'https?://[^\s<>"{}|\\^`\[\]]+')
    urls = url_pattern.findall(content)
    
    if unique:
        urls = list(dict.fromkeys(urls))  # Preserve order, remove dupes
    
    return urls

def save_urls(urls, output_file):
    output = Path(output_file)
    output.write_text('\n'.join(urls))
    print(f"✓ Saved {len(urls)} URLs → {output_file}")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Extract URLs from file')
    parser.add_argument('file', help='Text or HTML file')
    parser.add_argument('--output', '-o', help='Output file (default: urls.txt)')
    parser.add_argument('--all', action='store_true', help='Keep duplicates')
    args = parser.parse_args()
    
    urls = extract_urls(args.file, unique=not args.all)
    
    if args.output:
        save_urls(urls, args.output)
    else:
        for url in urls:
            print(url)
        print(f"\n{len(urls)} URLs found")