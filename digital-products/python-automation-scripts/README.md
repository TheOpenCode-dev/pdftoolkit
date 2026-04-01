# Python Automation Scripts Pack

Boost your productivity with 10 ready-to-use Python scripts.

## Quick Start

### Prerequisites
- Python 3.8 or higher
- Install dependencies:
```bash
pip install -r requirements.txt
```

### Run a Script
```bash
python script_name.py [arguments]
```

---

## Scripts Overview

| Script | Purpose | Command Example |
|--------|---------|-----------------|
| File Organizer | Sort files by type | `python file_organizer.py /path/to/folder` |
| Image Resizer | Batch resize images | `python image_resizer.py /path --width 800` |
| CSV Cleaner | Dedupe or merge CSVs | `python csv_cleaner.py /path --dedupe` |
| Screenshot Tool | CLI screenshots | `python screenshot.py --output screenshot.png` |
| URL Extractor | Extract URLs from file | `python url_extractor.py file.txt` |
| Folder Sync | Mirror folders | `python folder_sync.py source dest` |
| PDF Page Counter | Count PDF pages | `python pdf_page_counter.py /path` |
| Text to Speech | Convert text to audio | `python text_to_speech.py file.txt` |
| Duplicate Finder | Find duplicate files | `python duplicate_finder.py /path` |
| Batch Renamer | Rename with patterns | `python batch_renamer.py /path --prefix "new_"` |

---

## Detailed Usage

### File Organizer
Organizes files in a folder into categorized subfolders.

```
python file_organizer.py <folder_path>
```

Creates folders: `images/`, `videos/`, `audio/`, `documents/`, `archives/`, `code/`, `data/`, `others/`

### Image Resizer
Batch resize images with flexible options.

```
python image_resizer.py <folder> [--width WIDTH] [--height HEIGHT] [--scale PERCENT]
```

Examples:
```bash
python image_resizer.py ./photos --width 800
python image_resizer.py ./photos --height 600
python image_resizer.py ./photos --scale 50
```

### CSV Cleaner
Remove duplicates or merge multiple CSVs.

```
python csv_cleaner.py <folder> [--merge] [--dedupe]
```

### Screenshot Tool
Take screenshots from command line.

```
python screenshot.py [--output FILEPATH]
```

### URL Extractor
Extract all URLs from text or HTML files.

```
python url_extractor.py <file> [--output FILEPATH] [--all]
```

### Folder Sync
Mirror source folder to destination (rsync-like).

```
python folder_sync.py <source> <destination> [--delete]
```

### PDF Page Counter
Count pages in multiple PDFs.

```
python pdf_page_counter.py <folder>
```

### Text to Speech
Convert text files to audio.

```
python text_to_speech.py <file> [--output AUDIO_FILE] [--voice VOICE_NAME]
```

### Duplicate Finder
Find duplicate files by content hash.

```
python duplicate_finder.py <folder>
```

### Batch Renamer
Rename multiple files with patterns.

```
python batch_renamer.py <folder> [--pattern PATTERN] [--replace REPLACE] [--prefix PREFIX] [--suffix SUFFIX] [--sequential]
```

Examples:
```bash
python batch_renamer.py ./files --prefix "img_"
python batch_renamer.py ./files --suffix "_backup"
python batch_renamer.py ./files --sequential
```

---

## Troubleshooting

**"Module not found" error**
```bash
pip install -r requirements.txt
```

**Permission denied on macOS/Linux**
```bash
chmod +x *.py
```

**Python version check**
```bash
python3 --version
```

---

## License

Personal use only. Reselling or redistribution prohibited.

## Support

For issues or questions, contact: your@email.com