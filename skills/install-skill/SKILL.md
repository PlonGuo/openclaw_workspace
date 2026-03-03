---
name: install-skill
description: "Find, search, discover, and install agent skills from ClawHub, skills.sh, or GitHub into this workspace. Use when the user says: 'find a skill for X', 'search for skills', 'install a skill', 'add a skill from ClawHub', 'is there a skill for X', 'search clawhub', 'search skills.sh', 'discover skills', 'extend capabilities', or any request to browse or add new skills to the workspace."
---

# Install Skill

## Workflow

Follow these steps in order. Do not skip the approval step.

### 1. Search

Try sources in this order, stop when results are found:

```bash
# Preferred: ClawHub
clawhub search "<query>"

# Fallback: skills.sh
npx skills find "<query>"
```

If neither CLI is available, use the `firecrawl-scraper` skill to scrape `https://clawhub.com` or search `https://github.com/openclaw/skills`.

### 2. Present Results

Show the user a list:
- Skill name
- One-line description
- Source (ClawHub / skills.sh / GitHub)
- Link to learn more

### 3. Wait for Approval

Ask which skill(s) to install. **Do not proceed without explicit confirmation.**

### 4. Install

Install to workspace `skills/<skill-name>/` directory. Never install globally (`-g`).

```bash
# ClawHub
clawhub install <slug> --dir skills/

# skills.sh
npx skills add <package>
# Then move from global to workspace skills/ if needed
```

If the skill already exists in `skills/`, stop and tell the user.

### 5. Verify

Confirm `skills/<name>/SKILL.md` exists and has valid YAML frontmatter.

### 6. Preview

Read the installed SKILL.md. Send the user a summary:
- What the skill does
- Commands or workflows it provides
- Required env vars or binaries (from metadata)
- Any setup steps needed

### 7. Log

Append to `memory/YYYY-MM-DD.md`:
```
- Installed skill: <name> from <source>. <one-line description>.
```
