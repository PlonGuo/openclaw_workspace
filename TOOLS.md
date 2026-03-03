# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## Firecrawl

**Setup:**
1. Sign up at [firecrawl.dev](https://firecrawl.dev) and get an API key
2. Set `FIRECRAWL_API_KEY` in your environment:
   ```bash
   export FIRECRAWL_API_KEY=fc-...
   ```
   Or add to your shell profile (`~/.zshrc`).
3. Alternatively, configure via `openclaw.json`:
   ```json
   {
     "skills": {
       "entries": {
         "firecrawl-scraper": {
           "env": { "FIRECRAWL_API_KEY": "fc-..." }
         }
       }
     }
   }
   ```

**Status:** Not yet configured — API key needed.

---

Add whatever helps you do your job. This is your cheat sheet.
