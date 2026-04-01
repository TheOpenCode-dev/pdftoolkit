#!/usr/bin/env python3
"""Batch Renamer - Rename multiple files with patterns."""

import os
import sys
import re
from pathlib import Path

def rename_files(folder_path, pattern, replace, prefix='', suffix='', sequential=False):
    folder = Path(folder_path)
    files = sorted([f for f in folder.iterdir() if f.is_file()])
    
    for i, file in enumerate(files, 1):
        new_name = pattern
        
        if sequential:
            ext = file.suffix
            new_name = f"{i:03d}{ext}"
        else:
            new_name = re.sub(pattern, replace, file.name)
        
        new_name = prefix + new_name + suffix
        new_path = folder / new_name
        
        if new_path.exists():
            print(f"⚠ Skipped (exists): {new_name}")
            continue
        
        file.rename(new_path)
        print(f"✓ {file.name} → {new_name}")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Batch rename files')
    parser.add_argument('folder', help='Folder with files')
    parser.add_argument('--pattern', '-p', default='(.*)', help='Regex pattern (default: (.*))')
    parser.add_argument('--replace', '-r', default='\\1', help='Replacement')
    parser.add_argument('--prefix', help='Add prefix')
    parser.add_argument('--suffix', help='Add suffix')
    parser.add_argument('--sequential', '-s', action='store_true', help='Sequential numbering')
    args = parser.parse_args()
    
    rename_files(args.folder, args.pattern, args.replace, args.prefix, args.suffix, args.sequential)