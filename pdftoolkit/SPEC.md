# PDFToolkit - Product Specification

## Concept
A web-based PDF utility suite offering merge, split, and compression tools. Free tier with limits, paid for unlimited use.

## Features
1. **PDF Merge** - Upload multiple PDFs → single merged file
2. **PDF Split** - Upload PDF → extract specific pages or split ranges
3. **PDF Compress** - Reduce PDF file size with quality options

## Tech Stack
- Frontend: Single HTML page with vanilla JS (no framework needed)
- Backend: Python (Flask) on Render/Fly.io
- Storage: Temporary file storage (auto-cleanup)

## Monetization
- Free: 3 files/day, max 10MB each
- Paid ($5/mo): Unlimited files, larger files, batch processing

## UI Design
- Clean, professional look — dark theme with accent color
- Drag & drop file upload
- Progress indicators
- Instant download on completion

## Acceptance Criteria
- [x] All 3 tools functional (merge, split, compress)
- [x] Rate limiting enforced (3/day free)
- [x] Clean, responsive UI
- [ ] Deployed and accessible

## Deployment (Render.com)
1. Push to GitHub
2. Connect repo to Render
3. Auto-deploys from render.yaml

## Files
```
pdftoolkit/
├── app.py          # Flask backend
├── templates/
│   └── index.html  # Frontend UI
├── requirements.txt
├── render.yaml     # Render config
└── SPEC.md         # This spec
```