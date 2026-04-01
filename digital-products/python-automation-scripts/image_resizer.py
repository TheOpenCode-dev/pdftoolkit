#!/usr/bin/env python3
"""Image Resizer - Batch resize images."""

import os
import sys
from pathlib import Path
from PIL import Image

def resize_images(folder_path, width=None, height=None, scale_percent=None):
    folder = Path(folder_path)
    output_folder = folder / 'resized'
    output_folder.mkdir(exist_ok=True)
    
    extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']
    count = 0
    
    for file in folder.iterdir():
        if not file.is_file() or file.suffix.lower() not in extensions:
            continue
        
        img = Image.open(file)
        
        if scale_percent:
            new_w = int(img.width * scale_percent / 100)
            new_h = int(img.height * scale_percent / 100)
        elif width and height:
            new_w, new_h = width, height
        elif width:
            ratio = width / img.width
            new_w, new_h = width, int(img.height * ratio)
        elif height:
            ratio = height / img.height
            new_w, new_h = int(img.width * ratio), height
        else:
            print("Specify --width, --height, or --scale")
            return
        
        img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        img.save(output_folder / file.name, quality=85)
        print(f"✓ {file.name} → {new_w}x{new_h}")
        count += 1
    
    print(f"\nDone! {count} images resized → {output_folder}")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Batch resize images')
    parser.add_argument('folder', help='Folder containing images')
    parser.add_argument('--width', type=int, help='Target width')
    parser.add_argument('--height', type=int, help='Target height')
    parser.add_argument('--scale', type=int, help='Scale by percentage')
    args = parser.parse_args()
    
    resize_images(args.folder, args.width, args.height, args.scale)