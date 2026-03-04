# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## API Keys

All API keys are configured in `openclaw.json` at workspace root (gitignored).

### Firecrawl

1. Sign up at [firecrawl.dev](https://firecrawl.dev) and get an API key
2. Edit `openclaw.json`, set `FIRECRAWL_API_KEY` value under `skills.entries.firecrawl-scraper.env`

**Status:** Configured.

## File Locations

When Jason says to save/put a file somewhere, use these mappings:

| What Jason says (EN/CN) | Path |
|---|---|
| "workspace" / "工作区" / "你那边" | `files/` (within this workspace) |
| "desktop" / "桌面" | `~/Desktop` |
| "downloads" / "下载" | `~/Downloads` |
| "Git" | `~/Git` |
| "documents" / "文档" | `~/Documents` |

**Workspace `files/` rules:**
- All generated files go into `files/` by default when saving to workspace
- Sub-categories are supported: "放到 data 里" → `files/data/`
- If the sub-folder doesn't exist, create it automatically
- Examples: `files/data/`, `files/reports/`, `files/drafts/`

**This workspace:** `~/Git/openclaw_workspace`

---

Add whatever helps you do your job. This is your cheat sheet.
