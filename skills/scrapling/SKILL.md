---
name: scrapling
description: |
  Adaptive web scraping framework - handles single requests to full-scale crawls.
  Bypasses Cloudflare, supports proxy rotation, concurrent crawling with pause/resume.
  Built-in element learning for page changes.
---

# Scrapling Skill

Web scraping framework for AI agents. Handles simple requests to complex crawls.

## Setup (One-time)

```bash
# Create venv
python3 -m venv ~/.scrapling-venv
source ~/.scrapling-venv/bin/activate

# Install with all features
pip install "scrapling[all]>=0.4.3"

# Download browser dependencies
scrapling install --force
```

**Docker alternative (CLI only):**
```bash
docker pull pyd4vinci/scrapling
```

## When to Use

- **Simple sites** → `scrapling extract get`
- **Dynamic content** → `scrapling extract fetch`
- **Protected sites (Cloudflare)** → `scrapling extract stealthy-fetch`

## CLI Commands

### HTTP Requests
```bash
# Basic GET → Markdown
scrapling extract get "https://example.com" page.md

# With custom headers
scrapling extract get "https://api.site.com" data.json -H "User-Agent: MyBot/1.0"

# With cookies
scrapling extract get "https://site.com" out.md --cookies "session=abc123"

# CSS selector extraction
scrapling extract get "https://blog.site.com" articles.md --css-selector "article"

# POST with JSON
scrapling extract post "https://api.site.com/search" results.json -j '{"query":"test"}'
```

### Browser Automation
```bash
# Wait for JS loading
scrapling extract fetch "https://app.site.com" content.md --network-idle

# Wait for specific element
scrapling extract fetch "https://site.com" data.txt --wait-selector ".loaded"

# Visible browser (debug)
scrapling extract fetch "https://site.com" page.html --no-headless
```

### Stealth/Bypass
```bash
# Basic bypass
scrapling extract stealthy-fetch "https://site.com" content.md

# Solve Cloudflare
scrapling extract stealthy-fetch "https://cloudflare.site.com" out.md --solve-cloudflare

# With proxy
scrapling extract stealthy-fetch "https://site.com" out.md --proxy "http://proxy:8080"
```

## 🔒 Security: Always Use --ai-targeted

**CRITICAL:** When scraping for AI consumption, ALWAYS add `--ai-targeted` flag:

```bash
scrapling extract get "https://site.com" content.md --ai-targeted
```

This sanitizes hidden elements and prevents prompt injection.

## Python API (Advanced)

### Basic HTTP
```python
from scrapling.fetchers import Fetcher, FetcherSession

# One-off request
page = Fetcher.get('https://example.com/')
content = page.css('.content::text').getall()

# With session
with FetcherSession(impersonate='chrome') as session:
    page = session.get('https://quotes.toscrape.com/')
    quotes = page.css('.quote .text::text').getall()
```

### Stealth Mode (Cloudflare)
```python
from scrapling.fetchers import StealthyFetcher, StealthySession

# One-off
page = StealthyFetcher.fetch('https://cloudflare.site.com/')

# With session
with StealthySession(headless=True, solve_cloudflare=True) as session:
    page = session.fetch('https://site.com/')
```

### Spider Framework
```python
from scrapling.spiders import Spider, Response

class MySpider(Spider):
    name = "myspider"
    start_urls = ["https://example.com/"]
    concurrent_requests = 5

    async def parse(self, response: Response):
        for item in response.css('.item'):
            yield {
                "title": item.css('.title::text').get(),
                "link": item.css('a::attr(href)').get(),
            }

# Run with pause/resume
result = MySpider(crawldir="./crawl_data").start()
```

## Quick Reference

| Need | Command |
|------|---------|
| Simple page | `scrapling extract get URL out.md` |
| JS-heavy site | `scrapling extract fetch URL out.md` |
| Cloudflare protected | `scrapling extract stealthy-fetch URL out.md --solve-cloudflare` |
| AI consumption | Add `--ai-targeted` to any command |
| Custom proxy | Add `--proxy "http://user:pass@host:port"` |

## Cleanup

Always clean temp files after scraping:
```bash
rm -f /tmp/scrapling_*
```

## Notes

- Prefer `.md` output for readability
- Use CSS selectors (`-s`) to avoid large HTML blobs
- Start with `get`, escalate to `fetch` if empty, then `stealthy-fetch`