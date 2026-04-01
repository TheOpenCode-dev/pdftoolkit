#!/usr/bin/env python3
"""File Organizer - Sort files by type into folders."""

import os
import shutil
from pathlib import Path

# Map extensions to folder names
EXT_MAP = {
    'images': ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'svg', 'webp', 'ico'],
    'videos': ['mp4', 'avi', 'mov', 'mkv', 'flv', 'wmv'],
    'audio': ['mp3', 'wav', 'flac', 'aac', 'ogg', 'm4a'],
    'documents': ['pdf', 'doc', 'docx', 'txt', 'rtf', 'odt', 'xls', 'xlsx', 'ppt', 'pptx'],
    'archives': ['zip', 'rar', '7z', 'tar', 'gz', 'bz2'],
    'code': ['py', 'js', 'html', 'css', 'java', 'c', 'cpp', 'go', 'rs', 'ts'],
    'data': ['json', 'xml', 'csv', 'yaml', 'yml', 'sql'],
}

def get_folder(ext):
    ext = ext.lower()
    for folder, exts in EXT_MAP.items():
        if ext in exts:
            return folder
    return 'others'

def organize(folder_path):
    folder = Path(folder_path)
    if not folder.exists():
        print(f"Folder not found: {folder_path}")
        return
    
    for file in folder.iterdir():
        if not file.is_file():
            continue
        
        ext = file.suffix.lstrip('.')
        target_folder = get_folder(ext)
        target_path = folder / target_folder
        
        target_path.mkdir(exist_ok=True)
        shutil.move(str(file), str(target_path / file.name))
        print(f"✓ {file.name} → {target_folder}/")

if __name__ == '__main__':
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else '.'
    print(f"Organizing: {target}")
    organize(target)