#!/usr/bin/env python3
"""CSV Cleaner - Clean, dedupe, and merge CSVs."""

import csv
import os
from pathlib import Path

def read_csv(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        return list(csv.DictReader(f)), f.name

def write_csv(path, rows, fieldnames):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def remove_duplicates(rows):
    seen = set()
    unique = []
    for row in rows:
        key = tuple(sorted(row.items()))
        if key not in seen:
            seen.add(key)
            unique.append(row)
    return unique

def merge_csvs(folder_path, output='merged.csv'):
    folder = Path(folder_path)
    all_rows = []
    fieldnames = set()
    
    for file in folder.glob('*.csv'):
        rows, name = read_csv(file)
        if rows:
            fieldnames.update(rows[0].keys())
            all_rows.extend(rows)
            print(f"✓ Loaded {len(rows)} rows from {file.name}")
    
    fieldnames = sorted(fieldnames)
    write_csv(folder / output, all_rows, fieldnames)
    print(f"\nMerged {len(all_rows)} total rows → {output}")

def deduplicate(folder_path, output='deduplicated.csv'):
    folder = Path(folder_path)
    file = list(folder.glob('*.csv'))[0]
    rows, name = read_csv(file)
    
    original = len(rows)
    rows = remove_duplicates(rows)
    
    write_csv(folder / output, rows, rows[0].keys() if rows else [])
    print(f"✓ Removed {original - len(rows)} duplicates → {output}")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='CSV Cleaner')
    parser.add_argument('folder', help='Folder with CSV files')
    parser.add_argument('--merge', action='store_true', help='Merge all CSVs')
    parser.add_argument('--dedupe', action='store_true', help='Remove duplicates')
    args = parser.parse_args()
    
    if args.merge:
        merge_csvs(args.folder)
    elif args.dedupe:
        deduplicate(args.folder)
    else:
        print("Use --merge or --dedupe")