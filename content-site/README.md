# AI Tools Hub

A curated directory of the best AI tools for writing, image generation, video, audio, and productivity.

## Quick Start

### View the Site

Simply open `index.html` in a browser, or deploy to Vercel/Netlify:

1. Push to GitHub
2. Connect to Vercel or Netlify
3. Automatic deployment

### Local Development

```bash
# Open directly in browser
open index.html

# Or use a simple server
python -m http.server 8000
```

Then visit http://localhost:8000

---

## How-to Guides

### How to Add a New Tool

1. Open `index.html`
2. Find the `tools` array in the script section
3. Add a new object:
```javascript
{ name: "Tool Name", icon: "🎨", category: "writing", pricing: "free", desc: "Description", url: "https://tool.com", tags: ["Tag1", "Tag2"] }
```

### How to Deploy

**Vercel:**
1. Go to vercel.com
2. "Add New" → "Project"
3. Import GitHub repo
4. Deploy

**Netlify:**
1. Go to netlify.com
2. "Add new site" → "Import from Git"
3. Select repo
4. Deploy

### How to Add Affiliate Links

1. Find the tool's URL in the `tools` array
2. Replace with your affiliate link
3. Or add a tracking parameter: `https://tool.com?ref=aitoolshub`

---

## Reference

### Tool Object Schema

```javascript
{
  name: String,        // Tool name
  icon: String,        // Emoji icon
  category: String,    // writing|image|video|audio|productivity|dev
  pricing: String,    // "free" or "paid"
  desc: String,       // Short description
  url: String,        // Tool website URL
  tags: Array         // Search tags
}
```

### Categories

| Category ID | Display Name |
|-------------|--------------|
| writing | AI Writing |
| image | Image Generation |
| video | Video |
| audio | Audio |
| productivity | Productivity |
| dev | Dev Tools |

### Pricing Classes

- `.free` — Green badge for free tools
- `.paid` — Orange badge for paid tools

---

## Explanation

### Why this site?

AI tools are multiplying rapidly. This site helps people discover the best ones, organized by use case.

### Monetization Strategy

1. **Affiliate links** — Each tool link includes your affiliate ID
2. **AdSense** — After 100+ daily visitors, apply for AdSense
3. **Sponsored** — Companies pay to have tools featured

### Design Decisions

- **Static HTML** — No build step, easy to edit
- **Dark theme** — Modern, easy on eyes
- **Client-side filtering** — Fast, no server needed
- **Responsive** — Works on mobile and desktop