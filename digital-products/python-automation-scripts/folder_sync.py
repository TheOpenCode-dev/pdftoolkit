#!/usr/bin/env python3
"""Folder Sync - Mirror folder contents (rsync-like)."""

import os
import shutil
import hashlib
from pathlib import Path

def get_hash(file_path):
    h = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

def sync_folders(source, dest, delete=False):
    src = Path(source)
    dst = Path(dest)
    dst.mkdir(parents=True, exist_ok=True)
    
    copied = 0
    updated = 0
    deleted = 0
    
    # Copy/update files
    for file in src.rglob('*'):
        if not file.is_file():
            continue
        
        rel_path = file.relative_to(src)
        dst_file = dst / rel_path
        
        # Create parent dirs
        dst_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Check if needs copy
        needs_copy = True
        if dst_file.exists():
            if get_hash(file) == get_hash(dst_file):
                needs_copy = False
        
        if needs_copy:
            shutil.copy2(file, dst_file)
            if dst_file.exists():
                updated += 1
                print(f"✓ Updated: {rel_path}")
            else:
                copied += 1
                print(f"✓ Copied: {rel_path}")
        else:
            print(f"= Unchanged: {rel_path}")
    
    # Delete extra files in dest
    if delete:
        for file in dst.rglob('*'):
            if not file.is_file():
                continue
            rel_path = file.relative_to(dst)
            src_file = src / rel_path
            if not src_file.exists():
                file.unlink()
                deleted += 1
                print(f"✗ Deleted: {rel_path}")
    
    print(f"\nDone: {copied} copied, {updated} updated, {deleted} deleted")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Sync two folders')
    parser.add_argument('source', help='Source folder')
    parser.add_argument('dest', help='Destination folder')
    parser.add_argument('--delete', action='store_true', help='Delete files not in source')
    args = parser.parse_args()
    sync_folders(args.source, args.dest, args.delete)