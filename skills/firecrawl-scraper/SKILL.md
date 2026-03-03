---
name: firecrawl-scraper
description: "Web scraping, crawling, and search via Firecrawl API. Use when the user needs to: scrape a webpage, extract content from a URL, read a website, crawl an entire site or docs, map all URLs on a domain, or search the web with full content extraction. Also use when web_fetch is blocked or returns garbage on JS-heavy sites. Returns clean markdown optimized for LLM context."
metadata: {"openclaw":{"emoji":"🔥","primaryEnv":"FIRECRAWL_API_KEY","requires":{"env":["FIRECRAWL_API_KEY"],"anyBins":["python3","python"]}}}
---

# Firecrawl Scraper

## Usage

```bash
python3 skills/firecrawl-scraper/scripts/scrape.py --url <URL> --mode scrape
python3 skills/firecrawl-scraper/scripts/scrape.py --url <URL> --mode crawl --depth 2
python3 skills/firecrawl-scraper/scripts/scrape.py --url <URL> --mode map
python3 skills/firecrawl-scraper/scripts/scrape.py --mode search --query "<query>"
```

Use `--output .firecrawl/result.json` to save large outputs to file instead of stdout.

## Guidelines

- Store outputs in `.firecrawl/` directory — never flood the context with raw output.
- Use grep, head, or incremental reads on saved output files.
- Start crawl with `--depth 1`, increase only if needed.
- On rate limit errors, wait and retry once.
