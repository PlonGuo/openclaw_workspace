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

## Obsidian

**Vault path:** `~/Desktop/Obsidian`
**CLI:** `obsidian-cli` (default vault already set)

**IMPORTANT: All Obsidian content (slides, mind maps, notes, graphs) MUST be written to `~/Desktop/Obsidian/`, NOT to this workspace. The vault is on the Desktop, not here.**

Directory structure (all paths relative to `~/Desktop/Obsidian/`):
- `Slides/` — presentations (**Advanced Slides** plugin, see rules below)
- `MindMaps/` — mind maps (**Mind Map** plugin, see rules below)
- `Notes/` — general notes
- `Canvas/` — `.canvas` JSON files for visual node diagrams
- `Graph/` — knowledge graphs via `[[wikilinks]]` (one topic per subfolder, one node per .md file)

Installed plugins: Advanced Slides (community), Mind Map (community), Dataview (community)

### PPT / Slides — use Advanced Slides plugin
- File location: `Slides/`
- Based on reveal.js; supports full Obsidian markdown syntax
- Horizontal slide separator: a line containing ONLY `---`, with a **blank line above and below**
- Vertical slide separator: a line containing ONLY `--`, with a **blank line above and below**
- Speaker notes: add `note:` block after slide content
- Preview: open command palette → "Advanced Slides: Preview"
- **Do NOT use the core Slides plugin** — always use Advanced Slides

**Slide generation rules:**
- File MUST start with YAML frontmatter setting a theme: `---\ntheme: league\n---`
- Each slide MUST have a heading (e.g. `##`)
- Max 5 bullet points per slide — prevent overflow
- Output raw Markdown directly — NEVER wrap content in code blocks (no ` ```markdown `)
- NEVER use ````mermaid` or other diagram code blocks inside slides
- No extra explanatory text — output only the slide content itself

**Advanced visual effects (use at least one per presentation, pick what fits the content):**
- **Full-screen backgrounds:** on cover or chapter slides, use HTML comment before the slide heading:
  `<!-- .slide: data-background-image="https://example.com/img.jpg" -->`
  or gradient: `<!-- .slide: data-background-gradient="linear-gradient(to right, #283b95, #17b2c3)" -->`
- **Fragment animations:** for sequential reveal of list items, append after each item:
  `- Point one <!-- .element: class="fragment" -->`
- **Multi-column layout:** for comparison/side-by-side content, use HTML grid:
  `<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;"><div>Left</div><div>Right</div></div>`
- **Highlighted text:** use `<span>` with color for key data:
  `<span style="color: #ff6347;">important number</span>`

### Mind Map — use Mind Map plugin (Markmap)
- File location: `MindMaps/`
- Uses markdown headings (`#`, `##`, `###`, etc.) as hierarchy levels — each heading becomes a node
- Leaf nodes use unordered lists (`-` or `*`)
- Supports links, **bold**, *italic*, `code`, math within nodes
- Preview: open command palette → "Mind Map: Preview the current note as a Mind Map"
- **Do NOT use other mind map plugins** — always use Mind Map (Markmap)

**Mind map generation rules:**
- `#` = center topic, `##` = main branches, `###` and deeper = sub-branches
- Leaf detail uses unordered lists (`-` or `*`), NOT deeper headings
- NEVER use ````mermaid` or ````markmap` code blocks — output raw heading-based Markdown only
- NEVER wrap content in any code block (no ` ```markdown `)
- No extra explanatory text — output only the mind map content itself

Graph rules:
- `Graph/` contains ONLY node files (one .md per entity). No guides, indexes, or dashboards inside Graph/.
- Dashboards and query files go in `Notes/` (e.g., `Notes/中东局势仪表板.md`).
- Each node .md should have `**最近活动时间**: YYYY-MM-DD` for Dataview filtering.
- Use `[[wikilinks]]` between nodes to build relationships.
- Graph View filter bar: use `path:Graph/中东局势` to scope the view. Custom filter buttons cannot be added (built-in only: Tag, Attachment, Orphan, Existing files only).

---

Add whatever helps you do your job. This is your cheat sheet.
