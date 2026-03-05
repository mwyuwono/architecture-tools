# PROJECT_MASTER.md - Personal Cottage

## Project Scope and Authority
This file is the master documentation authority for the Personal Cottage project.

Cross-reference:
- Practice master: `../PRACTICE_MASTER.md`
- Coding-agent execution file: `agent.md` (execution behavior and QA protocol)

Documentation boundary:
- Project requirements, design intent, constraints, and decisions belong here.
- `agent.md` contains only coding-agent operational guidance and workflow protocol.

## Active Folders
Tier 1 (required) folders are initialized. No Tier 2 folders (Program, Site, Permits, Coordination, Meetings) have been created yet — create when first needed per `../PRACTICE_MASTER.md` → Documentation Strategy.

## Project Overview
- Project Name: Personal Cottage
- Location: Massachusetts, Vermont, or Connecticut (exact municipality pending)
- Square Footage Goal: 2,500 SF
- Occupancy Type: Single-family residential
- Site Context: Rural setting
- Construction Quality: High-end residential construction
- Architectural Style Priority: Greek Revival (high priority)

## Design Intent and Constraints
- Preserve classical Greek Revival character in massing and detail hierarchy.
- Finish materials should prioritize natural materials and avoid synthetic substitutes that do not age similarly.
- HVAC system is fully contained within the climate-controlled building envelope (no ducts in unconditioned attic or crawlspace).
- Additional dimensional/code constraints are to be added as design progresses.

## AutoCAD Documentation and Drafting Standard (Plain AutoCAD, 2D)
This project must use plain AutoCAD 2D drafting practices aligned to NCS/AIA-style conventions unless superseded by office standards or jurisdictional requirements.

Drafting outcomes must prioritize:
- consistency across sheets and phases
- predictable plotting and exports
- easy global edits
- clear coordination with consultants
- low-risk file management

AutoCAD must be treated as a drawing and documentation system, not BIM. Object metadata links are limited to blocks, attributes, fields, and data extraction workflows.

### Default Standards to Follow
1. Use NCS/AIA-style layer naming (discipline + major + minor) such as `A-WALL-FULL`, `A-DOOR`, `A-ANNO-TEXT`, `A-STRS`.
2. Use annotative scaling for text and dimensions where appropriate; otherwise enforce a consistent plotted text-height strategy.
3. Keep geometry in model space and sheets in paper space layouts with standardized viewport and plotting setups.
4. Use XREFs for coordinated backgrounds and SSM for multi-sheet metadata consistency.
5. Maintain CTB/STB plotting consistency so lineweights, screening, and linetypes remain predictable across all files.

### Decision Framework: When to Use What
#### XREFs
Use XREFs when the same base geometry appears on multiple sheets, when consultant coordination is required, or when recurring backgrounds are needed.

Required pattern:
- one model file per level (or zone when project scale requires)
- sheet files consume model XREFs
- relative paths and shared origin at `0,0,0`

Do not copy/paste model geometry between sheet files.

#### Dynamic Blocks
Use dynamic blocks for repeated symbols with controlled variation (doors, windows, stair symbols, markers, furniture/equipment placeholders).

Required pattern:
- visibility states for graphics
- stretch parameters for dimensional variants
- clean geometry and layer discipline

Do not over-parameterize one-off geometry.

#### Attributes
Use attributes when symbols require structured, extractable metadata (door/window marks, stair IDs, keynotes, equipment tags).

Required pattern:
- stable ALL CAPS attribute schema
- correct annotation layers (for example `A-ANNO-TAGS`)
- schedule generation via `DATAEXTRACTION`
- QA checks for duplicates, missing values, and out-of-range values

#### Fields + Sheet Set Manager (SSM)
Use fields and SSM for sheet numbers, titles, issue dates, revisions, and cross-references.

Required pattern:
- title block as a block with SSM field mapping
- one SSM per project

Avoid manual sheet metadata entry.

#### Data Extraction
Use data extraction for frequently changing schedules (doors, windows, finishes, equipment).

Required pattern:
- project-managed `.dxe` definition
- table layer standards (`A-TABL` or `A-ANNO-TABL` per office convention)
- refresh extraction before milestone and issue sets

#### Layer States
Use layer states for sheet-variant visibility (permit/DD/CD, life safety, furniture, consultant overlays), paired with viewport overrides when needed.

### Coordination Rules for Common Elements
#### Stairs
- Draft in 2D with explicit cut-vs-beyond conventions.
- Use a dedicated stair plan symbol block for treads/arrows/break lines.
- When scheduled, stair blocks must include attributes:
  - `STAIR_ID`, `WIDTH`, `RISERS`, `RISER_HT`, `TREAD_DP`, `LANDING_DP`
- Stair spec references remain keyed by note/keynote IDs.

#### Doors and Windows
- Use dynamic blocks plus attributes when schedules are required.
- Keep insertion points and scaling behavior consistent.
- Separate plan/elevation blocks where representation differs.

#### Grids, Levels, Section/Elevation Marks
- Use blocks consistently.
- Prefer attributes for IDs and fields for sheet/detail references when SSM is present.

### Folder Convention
See `../PRACTICE_MASTER.md` → Documentation Strategy for the full taxonomy and creation rules. CAD-specific subfolders (XREF, Sheets, Details, Library, Exports) are created inside `Drawings/` as the project scales.

If CAD subfolders are introduced, use relative paths and maintain shared drawing origin at `0,0,0`.

### Do This, Not That Defaults
- Use XREF backgrounds instead of copied geometry.
- Use dynamic blocks for repeated symbols instead of manual redraws.
- Use attributes plus data extraction for schedule-driven objects.
- Use SSM plus fields for sheet metadata instead of manual typing.
- Use layer states/viewport overrides for visibility control instead of duplicating content.

### Escalation Boundary (Plain AutoCAD vs BIM)
If bidirectional spec-object synchronization or model-driven intelligence is requested, treat it as out-of-scope for plain AutoCAD and evaluate BIM workflow adoption explicitly.
For spec linkage in plain AutoCAD, use keynote IDs, hyperlinks, and attribute-driven schedules.

## Data and Deliverables Structure
- Drawings: `Drawings/`
- Raw extracts: `Data_Raw/` (source of truth for schedule data)
- Generated schedules: `Schedules/`
- Material/assembly specs: `Specs/`
- Code and zoning notes: `Code_Research/`

Naming conventions:
- Raw data: `YYYY-MM-DD_<source>_<topic>.csv|json`
- Schedules: `<discipline>-schedule.md`
- Specs: `<system>-spec.md`
- Code notes: `<jurisdiction>-<code>-notes.md`

## Code Research Status
- Jurisdiction is not fixed; all code compliance checks are currently provisional.
- Once municipality is selected, create jurisdiction-specific notes in `Code_Research/` and update required code pathways.

## Decision Log
- 2026-03-05: State 000 scaffold initialized.
- 2026-03-05: State 001 initialized with location shortlist (MA/VT/CT), 2,500 SF target, and Greek Revival + natural-aging material priorities.
- 2026-03-05: Added occupancy (single-family), construction target (high-end), and rural site assumption.
- 2026-03-05: Migrated project-level documentation authority from `agent.md` to `PROJECT_MASTER.md`.
- 2026-03-05: Migrated AutoCAD drafting standards from `m3-design-v2/to-add.md` into this file as project policy authority; `agent.md` now retains execution-only CAD protocol.
