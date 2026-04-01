#!/usr/bin/env python3
"""Duplicate Finder - Find duplicate files by hash."""

import hashlib
import os
from pathlib import Path

def get_file_hash(file_path):
    h = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

def find_duplicates(folder_path):
    folder = Path(folder_path)
    hashes = {}
    
    for file in folder.rglob('*'):
        if not file.is_file():
            continue
        h = get_file_hash(file)
        hashes.setdefault(h, []).append(file)
    
    dupes = {k: v for k, v in hashes.items() if len(v) > 1}
    
    if dupes:
        print(f"Found {len(dupes)} sets of duplicates:\n")
        for h, files in dupes.items():
            print(f"Hash: {h[:8]}...")
            for f in files:
                print(f"  - {f}")
            print()
    else:
        print("No duplicates found.")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Find duplicate files')
    parser.add_argument('folder', help='Folder to scan')
    args = parser.parse_args()
    find_duplicates(args.folder)