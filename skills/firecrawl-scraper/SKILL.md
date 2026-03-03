---
name: firecrawl-scraper
description: Web scraping via Firecrawl API. Use when the user needs to scrape, crawl, extract content from websites, map site URLs, or search the web with full content extraction. Returns clean markdown.
metadata: {"openclaw":{"emoji":"🔥","primaryEnv":"FIRECRAWL_API_KEY","requires":{"env":["FIRECRAWL_API_KEY"],"anyBins":["python3","python"]}}}
---

# Firecrawl Scraper

## When to Use

- User asks to scrape/extract/read a webpage
- User needs to crawl an entire site or section
- User wants to map all URLs on a site
- User needs web search with full content extraction
- `web_fetch` is blocked or returns garbage (JS-heavy sites)

## Usage

Run the script from the skill directory:

```bash
python3 skills/firecrawl-scraper/scripts/scrape.py --url <URL> --mode scrape
```

### Modes

| Mode | Purpose | Example |
|------|---------|---------|
| `scrape` | Single page → markdown | `--url https://example.com --mode scrape` |
| `crawl` | Crawl site with depth | `--url https://docs.example.com --mode crawl --depth 2` |
| `map` | List all URLs on a site | `--url https://example.com --mode map` |
| `search` | Web search + extract | `--mode search --query "firecrawl pricing"` |

### Arguments

- `--url` — Target URL (required for scrape/crawl/map)
- `--mode` — One of: scrape, crawl, map, search (default: scrape)
- `--query` — Search query (required for search mode)
- `--depth` — Crawl depth (default: 2, only for crawl mode)
- `--output` — Save output to file instead of stdout

### Output Format

JSON to stdout:
```json
{
  "ok": true,
  "mode": "scrape",
  "source_url": "https://example.com",
  "markdown": "# Page Title\n\nPage content...",
  "metadata": { "title": "...", "description": "..." }
}
```

For crawl/map modes, `results` is an array instead of a single `markdown` field.

## Guidelines

- Store large outputs in `.firecrawl/` directory using `--output .firecrawl/result.json`
- Don't read entire output files at once — use grep, head, or incremental reads
- For crawl mode, start with `--depth 1` and increase only if needed
- If Firecrawl API returns rate limit errors, wait and retry once
