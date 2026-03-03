#!/usr/bin/env python3
"""Firecrawl web scraper for OpenClaw.

Usage:
    python3 scrape.py --url https://example.com --mode scrape
    python3 scrape.py --url https://docs.example.com --mode crawl --depth 2
    python3 scrape.py --url https://example.com --mode map
    python3 scrape.py --mode search --query "firecrawl pricing"
"""

import argparse
import json
import os
import sys
import time
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError


API_BASE = "https://api.firecrawl.dev/v1"


def get_api_key():
    key = os.environ.get("FIRECRAWL_API_KEY")
    if not key:
        print(json.dumps({"ok": False, "error": "FIRECRAWL_API_KEY not set"}))
        sys.exit(1)
    return key


def api_request(method, endpoint, data=None):
    """Make a request to the Firecrawl API."""
    api_key = get_api_key()
    url = f"{API_BASE}/{endpoint}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    body = json.dumps(data).encode() if data else None
    req = Request(url, data=body, headers=headers, method=method)

    try:
        with urlopen(req) as resp:
            return json.loads(resp.read().decode())
    except HTTPError as e:
        error_body = e.read().decode() if e.fp else str(e)
        try:
            error_data = json.loads(error_body)
            msg = error_data.get("error", error_body)
        except (json.JSONDecodeError, ValueError):
            msg = error_body
        return {"ok": False, "error": f"HTTP {e.code}: {msg}"}
    except URLError as e:
        return {"ok": False, "error": f"Connection error: {e.reason}"}


def poll_job(job_id, endpoint, max_wait=120):
    """Poll an async job until completion."""
    elapsed = 0
    interval = 2
    while elapsed < max_wait:
        result = api_request("GET", f"{endpoint}/{job_id}")
        status = result.get("status")
        if status == "completed":
            return result
        if status in ("failed", "cancelled"):
            return {"ok": False, "error": f"Job {status}", "details": result}
        time.sleep(interval)
        elapsed += interval
        interval = min(interval * 1.5, 10)
    return {"ok": False, "error": f"Job timed out after {max_wait}s"}


def scrape(url):
    """Scrape a single URL and return markdown."""
    result = api_request("POST", "scrape", {
        "url": url,
        "formats": ["markdown"],
    })
    if not result.get("success") and not result.get("data"):
        return {"ok": False, "error": result.get("error", "Unknown error"), "source_url": url}

    data = result.get("data", result)
    return {
        "ok": True,
        "mode": "scrape",
        "source_url": url,
        "markdown": data.get("markdown", ""),
        "metadata": data.get("metadata", {}),
    }


def crawl(url, depth=2):
    """Crawl a site starting from URL."""
    result = api_request("POST", "crawl", {
        "url": url,
        "maxDepth": depth,
        "scrapeOptions": {"formats": ["markdown"]},
    })

    if not result.get("success") and not result.get("id"):
        return {"ok": False, "error": result.get("error", "Unknown error"), "source_url": url}

    # Crawl is async — poll for results
    job_id = result.get("id")
    if job_id:
        result = poll_job(job_id, "crawl")
        if not result.get("ok", True):
            return result

    pages = result.get("data", [])
    return {
        "ok": True,
        "mode": "crawl",
        "source_url": url,
        "pages_count": len(pages),
        "results": [
            {
                "url": p.get("metadata", {}).get("sourceURL", ""),
                "title": p.get("metadata", {}).get("title", ""),
                "markdown_length": len(p.get("markdown", "")),
            }
            for p in pages
        ],
        "full_data_available": True,
    }


def map_site(url):
    """Map all URLs on a site."""
    result = api_request("POST", "map", {"url": url})

    if not result.get("success"):
        return {"ok": False, "error": result.get("error", "Unknown error"), "source_url": url}

    links = result.get("links", [])
    return {
        "ok": True,
        "mode": "map",
        "source_url": url,
        "urls_count": len(links),
        "urls": links,
    }


def search(query):
    """Search the web and extract content."""
    result = api_request("POST", "search", {
        "query": query,
        "scrapeOptions": {"formats": ["markdown"]},
    })

    if not result.get("success") and not result.get("data"):
        return {"ok": False, "error": result.get("error", "Unknown error"), "query": query}

    data = result.get("data", [])
    return {
        "ok": True,
        "mode": "search",
        "query": query,
        "results_count": len(data),
        "results": [
            {
                "url": item.get("url", ""),
                "title": item.get("title", ""),
                "markdown": item.get("markdown", "")[:500],  # truncate for stdout
            }
            for item in data
        ],
    }


def main():
    parser = argparse.ArgumentParser(description="Firecrawl web scraper for OpenClaw")
    parser.add_argument("--url", help="Target URL")
    parser.add_argument("--mode", choices=["scrape", "crawl", "map", "search"], default="scrape")
    parser.add_argument("--query", help="Search query (for search mode)")
    parser.add_argument("--depth", type=int, default=2, help="Crawl depth (for crawl mode)")
    parser.add_argument("--output", help="Save output to file instead of stdout")
    args = parser.parse_args()

    # Validate args
    if args.mode in ("scrape", "crawl", "map") and not args.url:
        result = {"ok": False, "error": f"--url is required for {args.mode} mode"}
    elif args.mode == "search" and not args.query:
        result = {"ok": False, "error": "--query is required for search mode"}
    else:
        # Execute
        if args.mode == "scrape":
            result = scrape(args.url)
        elif args.mode == "crawl":
            result = crawl(args.url, args.depth)
        elif args.mode == "map":
            result = map_site(args.url)
        elif args.mode == "search":
            result = search(args.query)

    output = json.dumps(result, indent=2, ensure_ascii=False)

    if args.output:
        os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output)
        print(json.dumps({"ok": True, "saved_to": args.output}))
    else:
        print(output)


if __name__ == "__main__":
    main()
