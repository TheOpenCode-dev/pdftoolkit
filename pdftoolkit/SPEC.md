# PDFToolkit - Product Specification

## Overview

A web-based PDF utility suite offering merge, split, and compression tools. Free tier with limits, paid tier for unlimited use.

## Features

1. **PDF Merge** - Upload multiple PDFs → single merged file
2. **PDF Split** - Upload PDF → extract specific pages or split ranges
3. **PDF Compress** - Reduce PDF file size with quality options

## Tech Stack

- Frontend: Single HTML page with vanilla JS
- Backend: Python (Flask)
- Deployment: Render/Fly.io
- Storage: Temporary file storage (auto-cleanup)

## Monetization

- **Free Tier:** 3 files/day, max 10MB each
- **Paid Tier:** $5/month — unlimited files, larger files, batch processing

## Acceptance Criteria

- [x] All 3 tools functional (merge, split, compress)
- [x] Rate limiting enforced (3/day free)
- [x] Clean, responsive UI
- [ ] Deployed and accessible

## Files

```
pdftoolkit/
├── app.py          # Flask backend
├── templates/
│   └── index.html  # Frontend UI
├── requirements.txt
├── render.yaml     # Render config
└── SPEC.md         # This specification
```