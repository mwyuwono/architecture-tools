# agent.md

Primary coding-agent instructions for this repository.
Designed to be discoverable by any coding agent (Claude, Cursor, Copilot, etc.).

Claude users: `CLAUDE.md` cross-references this file and adds Claude-specific loading behavior.

---

## Documentation Authority Chain

Use documentation in this order:

1. `PRACTICE_MASTER.md` — practice-wide documentation authority
2. `<project>/PROJECT_MASTER.md` — project documentation authority
3. `<project>/agent.md` — coding-agent execution protocol for that project

If files disagree, higher authority wins.

## Scope

- `PROJECT_MASTER.md` files hold project requirements, design decisions, and planning context.
- `agent.md` files hold only coding-agent workflow and execution rules.
- Avoid duplicating project narrative content inside `agent.md`.

## Git and Backup Behavior

Follow the git hygiene protocol in `PRACTICE_MASTER.md`.

Minimum required workflow:

1. `git fetch origin --prune`
2. `git status -sb`
3. Make scoped changes
4. `git add -A`
5. `git commit -m "<concise milestone message>"`
6. `git push origin <branch>`
7. `git status -sb`

Never run destructive git commands unless explicitly requested by the user.

## Working Style

- Be concise and direct.
- Prefer small, reviewable changes.
- Keep repository structure explicit and predictable.
- Update cross-references when files move or are renamed.

## Notes Ingestion Protocol

At the start of each session, before any other work:

### Step 1 — Scan
Check all `notes/` folders for files (ignore `.gitkeep`):
- `notes/` (practice-level)
- `<project>/notes/` for each project listed in the Project Index

If no notes are found, proceed normally.

### Step 2 — Interpret and Route
For each note file found, read the content and determine the appropriate target:

| Note Content | Typical Source | Target |
|---|---|---|
| Practice conventions, naming standards, documentation policy | `notes/` (root) | `PRACTICE_MASTER.md` |
| Design intent: massing, materials, style, site, orientation | `<project>/notes/` | `<project>/PROJECT_MASTER.md` → Design Intent or Decision Log |
| Technical systems: HVAC, structural, envelope, MEP | `<project>/notes/` | `<project>/PROJECT_MASTER.md` → relevant systems section, or new section |
| Code, zoning, jurisdiction, permitting | `<project>/notes/` | `<project>/PROJECT_MASTER.md` → Code Research Status, or new file in `Code_Research/` |
| Historic, commission, or client-facing significance | `<project>/notes/` | `<project>/PROJECT_MASTER.md` → Notes of Record (create section if absent) |
| Agent execution or workflow changes | any | root `agent.md` or `<project>/agent.md` |
| Ambiguous or no clean fit | any | Propose target and rationale to user |

Integration style:
- Decision Log entries: `- YYYY-MM-DD: [interpreted content]`
- Section body additions: integrated prose, no date prefix
- New sections: include proposed section name and full content in the batch summary

### Step 3 — Present Batch Summary
Before writing anything, present a single batch summary showing for each note:
- Note filename and raw content
- Proposed target file and section
- Proposed text to be added

Wait for explicit user confirmation before proceeding.

### Step 4 — Write and Archive
After confirmation:
1. Write the interpreted content to each target file.
2. Create `processed-notes/` adjacent to the source `notes/` folder if it does not exist.
3. Move each note file into `processed-notes/`.
4. Commit all changes per the git hygiene protocol with a message like `Process notes from YYYY-MM-DD session`.

## Repository Layout

- `PRACTICE_MASTER.md` — practice documentation authority
- `agent.md` — primary coding-agent instructions (this file)
- `CLAUDE.md` — Claude-specific supplement; cross-references this file
- `project-personal-cottage/` — active project folder
- `tools/` — shared tools/utilities

## Project Index

| Project | Agent File | Project Master |
|---|---|---|
| Personal Cottage | `project-personal-cottage/agent.md` | `project-personal-cottage/PROJECT_MASTER.md` |

## Change Log

- 2026-03-05: Established as primary coding-agent instructions file. `CLAUDE.md` reduced to Claude-specific supplement.
