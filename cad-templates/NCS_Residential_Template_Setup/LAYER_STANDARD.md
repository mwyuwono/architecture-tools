# Architectural Layer Standard for Residential Production

A comprehensive layer naming and property standard for residential construction document sets, based on NCS (National CAD Standard) conventions and UDS (Uniform Drawing System) alignment.

---

## Table of Contents

1. [Overview](#overview)
2. [Naming Convention](#naming-convention)
3. [Discipline Designators](#discipline-designators)
4. [Layer Property Requirements](#layer-property-requirements)
5. [Lineweight Hierarchy](#lineweight-hierarchy)
6. [Linetype Standards](#linetype-standards)
7. [Color Standards](#color-standards)
8. [Layer Categories](#layer-categories)
9. [Usage by Drawing Type](#usage-by-drawing-type)
10. [Best Practices](#best-practices)

---

## Overview

### Purpose

This standard provides a consistent, professional layer structure for residential architectural production. It supports:

- Full construction document sets (plans, sections, elevations, details)
- Demolition and existing conditions documentation
- Coordination with structural and MEP consultants
- Automated plotting with predictable lineweight output
- Small-office professional workflows

### Standards Basis

| Aspect | Reference |
|--------|-----------|
| Naming convention | NCS (National CAD Standard) inspired |
| Layer organization | UDS (Uniform Drawing System) aligned |
| Lineweights | AIA CAD Layer Guidelines |
| Compatibility | AutoCAD for Mac 2018+ |

### Scope

This standard covers residential projects including:
- Single-family homes
- Multi-family residential (up to 4 units)
- Additions and renovations
- ADUs (Accessory Dwelling Units)

---

## Naming Convention

### Layer Name Format

```
[Discipline]-[Major]-[Minor]-[Status]
```

| Component | Required | Description | Example |
|-----------|----------|-------------|---------|
| Discipline | Yes | Single letter code | A, S, C, V |
| Major | Yes | Primary category (4 characters) | WALL, DOOR, WIND |
| Minor | Optional | Subcategory (4 characters) | CORE, GLAZ, PATT |
| Status | Optional | Condition modifier | DEMO, EXST, OVER |

### Naming Rules

1. **All uppercase** - Layer names use uppercase letters only
2. **Hyphen separator** - Components separated by hyphens
3. **No spaces** - Never use spaces in layer names
4. **4-character groups** - Major and minor groups typically 4 characters
5. **Abbreviations** - Use standard NCS abbreviations

### Standard Abbreviations

| Abbreviation | Meaning |
|--------------|---------|
| WALL | Walls |
| DOOR | Doors |
| WIND | Windows |
| FLOR | Floor |
| CLNG | Ceiling |
| ROOF | Roof |
| STRS | Stairs |
| BEAM | Beams |
| COLS | Columns |
| FURN | Furniture |
| EQPM | Equipment |
| ANNO | Annotation |
| DIMS | Dimensions |
| TEXT | Text |
| NOTE | Notes |
| TAGS | Tags |
| SYMB | Symbols |
| LEAD | Leaders |
| SECT | Section |
| ELEV | Elevation |
| IDEN | Identification |
| GRID | Grid |
| PROP | Property |
| TOPO | Topography |
| ROAD | Roads |
| WALK | Walkways |
| VPRT | Viewport |
| TITL | Title |
| DEMO | Demolition |
| EXST | Existing |
| OVER | Overhead/above |
| CORE | Core/structure |
| INT | Interior |
| EXT | Exterior |
| FRM | Frame |
| PANL | Panel |
| SWNG | Swing |
| GLAZ | Glazing |
| SILL | Sill |
| PATT | Pattern |
| FIN | Finish |
| SOFF | Soffit |
| OPEN | Opening |
| EDGE | Edge |
| RIDG | Ridge |
| VALY | Valley |
| DOWN | Downspout |
| HAND | Handrail |
| FOOT | Footing |
| FNDN | Foundation |
| SLAB | Slab |
| FIXT | Fixture |
| CONC | Concrete |
| WOOD | Wood |
| INSL | Insulation |
| CUT | Cut line |

---

## Discipline Designators

Only the following discipline designators are permitted:

| Code | Discipline | Usage |
|------|------------|-------|
| **A** | Architectural | All architectural elements, annotation, finishes |
| **S** | Structural | Beams, columns, foundations, structural slabs |
| **C** | Civil/Coordination | Property lines, grids, topography, site elements |
| **M** | Mechanical | HVAC coordination only (minimal use) |
| **E** | Electrical | Electrical coordination only (minimal use) |
| **V** | Viewport/Sheet | Sheet-level utilities, viewports, title blocks |

### Discipline Usage Guidelines

**A - Architectural (Primary)**
- All building elements (walls, doors, windows, stairs)
- All annotation (dimensions, text, symbols)
- Interior finishes and patterns
- Furniture and fixtures

**S - Structural**
- Load-bearing elements only
- Beams, columns, foundations
- Structural slabs and footings
- Coordinate with structural engineer

**C - Civil/Coordination**
- Column grids and reference grids
- Property boundaries
- Site elements (roads, walks, topography)
- Survey reference information

**V - Viewport/Sheet**
- Viewport boundaries (non-plotting)
- Title block elements
- Sheet-level graphics

**M/E - MEP Coordination**
- Reserved for consultant coordination
- Minimal use in residential
- Background reference only

---

## Layer Property Requirements

Every layer must have these properties explicitly defined:

| Property | Description | Required |
|----------|-------------|----------|
| Color | ACI (AutoCAD Color Index) number | Yes |
| Linetype | Standard AutoCAD linetype | Yes |
| Lineweight | Millimeter value | Yes |
| Plot | On or Off | Yes |
| Description | Purpose and usage | Yes |

### Property Inheritance

When objects are set to "ByLayer":
- **Color** → Controls display and CTB pen assignment
- **Linetype** → Controls line pattern
- **Lineweight** → Controls plotted line thickness

---

## Lineweight Hierarchy

Lineweights create visual hierarchy and depth in drawings. This standard uses a 5-level hierarchy:

### Hierarchy Levels

| Level | Weight (mm) | Purpose | Typical Layers |
|-------|-------------|---------|----------------|
| **Heavy** | 0.50–0.60 | Primary cut elements | A-WALL, A-WALL-CORE |
| **Medium** | 0.30–0.40 | Secondary cut, major elements | A-DOOR, A-WIND, A-STRS, S-BEAM |
| **Light** | 0.18–0.25 | Annotation, furniture, minor elements | A-ANNO-*, A-FURN |
| **Very Light** | 0.13 | Hatching, patterns | A-HATCH-* |
| **Reference** | 0.25 | Grid lines, references (with dashed linetype) | C-GRID |

### Lineweight Assignment Logic

```
Plan Cut Elements (sectioned):
  Walls at cut → Heavy (0.50)
  Doors/Windows at cut → Medium (0.35)

Beyond Elements (not sectioned):
  Furniture, casework → Light (0.18)
  Floor patterns → Very Light (0.13)

Above Elements (overhead):
  Ceiling lines → Light (0.18) + Hidden linetype
  Roof overhangs → Light (0.18) + Dashed linetype

Annotation:
  Dimensions, text → Light (0.18)
  Symbols, leaders → Light (0.18)

Reference:
  Column grids → Reference (0.25) + Center linetype
```

---

## Linetype Standards

Only standard AutoCAD linetypes are permitted to ensure portability:

| Linetype | Usage |
|----------|-------|
| **Continuous** | Default for most elements |
| **Hidden** | Elements above cut plane, concealed items |
| **Center** | Grid lines, centerlines |
| **Phantom** | Future work, demolished items, property lines |

### Linetype by Element Type

| Element | Linetype |
|---------|----------|
| Walls (cut) | Continuous |
| Walls (above/beyond) | Hidden |
| Doors, windows | Continuous |
| Ceiling lines | Hidden |
| Grid lines | Center |
| Property lines | Phantom |
| Demolition | Phantom or Hidden |
| Existing to remain | Continuous |

---

## Color Standards

Colors serve two purposes:
1. **Screen display** - Visual differentiation while drafting
2. **Plot style** - CTB/STB mapping to pen weights

### Color-to-Lineweight Mapping (CTB)

| ACI Color | Screen Color | Plotted Weight | Usage |
|-----------|--------------|----------------|-------|
| 1 | Red | 0.50 mm | Primary cut (walls) |
| 2 | Yellow | 0.35 mm | Structural elements |
| 3 | Green | 0.35 mm | Roofs |
| 4 | Cyan | 0.35 mm | Stairs |
| 5 | Blue | 0.35 mm | Windows, glazing |
| 6 | Magenta | 0.25 mm | Section/elevation marks |
| 7 | White/Black | 0.18 mm | Annotation |
| 8 | Dark Gray | 0.18 mm | Furniture, minor elements |
| 9 | Light Gray | 0.25 mm | Grids (with center linetype) |
| 10 | Red (light) | 0.35 mm | Structural |
| 14 | Green (dark) | 0.13 mm | Demolition |
| 30 | Orange | 0.35 mm | Doors |
| 40 | Yellow-Orange | 0.35 mm | Windows |
| 252 | Light Gray | 0.13 mm | Hatches |
| 253 | Dark Gray | 0.18 mm | Existing conditions |

### Color Assignment by Category

| Category | Primary Color | Notes |
|----------|---------------|-------|
| Walls | 1 (Red) | Heavy weight |
| Doors | 30 (Orange) | Medium weight |
| Windows | 40 (Yellow-Orange) | Medium weight |
| Floors | 8 (Gray) | Light weight |
| Ceilings | 8 (Gray) | Light, hidden linetype |
| Roofs | 3 (Green) | Medium weight |
| Stairs | 4 (Cyan) | Medium weight |
| Structure | 10 (Red) | Medium-heavy weight |
| Grids | 9 (Light Gray) | Reference weight, center linetype |
| Annotation | 7 (White) | Light weight |
| Hatches | 252 (Light Gray) | Very light weight |
| Demolition | 14 (Green) | Phantom linetype |
| Existing | 253 (Dark Gray) | Distinguishes from new |
| Viewport | 8 (Gray) | Non-plotting |

---

## Layer Categories

### Walls (7 layers)

| Layer | Color | LT | LW | Plot | Description |
|-------|-------|----|----|------|-------------|
| A-WALL | 1 | Continuous | 0.50 | Yes | General wall lines |
| A-WALL-CORE | 1 | Continuous | 0.50 | Yes | Wall core/structure |
| A-WALL-INT | 1 | Continuous | 0.50 | Yes | Interior partition walls |
| A-WALL-EXT | 1 | Continuous | 0.50 | Yes | Exterior walls |
| A-WALL-DEMO | 14 | Phantom | 0.35 | Yes | Walls to be demolished |
| A-WALL-EXST | 253 | Continuous | 0.50 | Yes | Existing walls to remain |
| A-WALL-OVER | 1 | Hidden | 0.25 | Yes | Walls above cut plane |

### Doors (5 layers)

| Layer | Color | LT | LW | Plot | Description |
|-------|-------|----|----|------|-------------|
| A-DOOR | 30 | Continuous | 0.35 | Yes | Door outlines, general |
| A-DOOR-FRM | 30 | Continuous | 0.35 | Yes | Door frames |
| A-DOOR-PANL | 30 | Continuous | 0.25 | Yes | Door panels |
| A-DOOR-SWNG | 30 | Continuous | 0.18 | Yes | Door swings |
| A-DOOR-GLAZ | 5 | Continuous | 0.25 | Yes | Door glazing |

### Windows (4 layers)

| Layer | Color | LT | LW | Plot | Description |
|-------|-------|----|----|------|-------------|
| A-WIND | 40 | Continuous | 0.35 | Yes | Window outlines, general |
| A-WIND-FRM | 40 | Continuous | 0.35 | Yes | Window frames |
| A-WIND-GLAZ | 5 | Continuous | 0.25 | Yes | Window glazing |
| A-WIND-SILL | 40 | Continuous | 0.25 | Yes | Window sills |

### Floors (4 layers)

| Layer | Color | LT | LW | Plot | Description |
|-------|-------|----|----|------|-------------|
| A-FLOR | 8 | Continuous | 0.18 | Yes | Floor outlines, general |
| A-FLOR-PATT | 252 | Continuous | 0.13 | Yes | Floor patterns/finishes |
| A-FLOR-FIN | 8 | Continuous | 0.18 | Yes | Floor finish boundaries |
| A-FLOR-STRS | 4 | Continuous | 0.35 | Yes | Floor level stairs |

### Ceilings (4 layers)

| Layer | Color | LT | LW | Plot | Description |
|-------|-------|----|----|------|-------------|
| A-CLNG | 8 | Hidden | 0.18 | Yes | Ceiling lines |
| A-CLNG-GRID | 8 | Hidden | 0.13 | Yes | Ceiling grid |
| A-CLNG-SOFF | 8 | Hidden | 0.18 | Yes | Soffits |
| A-CLNG-OPEN | 8 | Hidden | 0.18 | Yes | Ceiling openings |

### Roofs (6 layers)

| Layer | Color | LT | LW | Plot | Description |
|-------|-------|----|----|------|-------------|
| A-ROOF | 3 | Continuous | 0.35 | Yes | Roof outlines, general |
| A-ROOF-EDGE | 3 | Continuous | 0.35 | Yes | Roof edges/eaves |
| A-ROOF-RIDG | 3 | Continuous | 0.35 | Yes | Ridges |
| A-ROOF-VALY | 3 | Continuous | 0.25 | Yes | Valleys |
| A-ROOF-OVER | 3 | Hidden | 0.18 | Yes | Roof overhangs (dashed in plan) |
| A-ROOF-DOWN | 3 | Continuous | 0.18 | Yes | Downspouts, drainage |

### Stairs and Ramps (4 layers)

| Layer | Color | LT | LW | Plot | Description |
|-------|-------|----|----|------|-------------|
| A-STRS | 4 | Continuous | 0.35 | Yes | Stair outlines, general |
| A-STRS-UP | 4 | Continuous | 0.35 | Yes | Stairs going up |
| A-STRS-DOWN | 4 | Hidden | 0.25 | Yes | Stairs going down (beyond) |
| A-STRS-HAND | 4 | Continuous | 0.25 | Yes | Handrails, guards |

### Structure (5 layers)

| Layer | Color | LT | LW | Plot | Description |
|-------|-------|----|----|------|-------------|
| S-BEAM | 10 | Continuous | 0.35 | Yes | Structural beams |
| S-COLS | 10 | Continuous | 0.50 | Yes | Structural columns |
| S-FOOT | 10 | Continuous | 0.35 | Yes | Footings |
| S-FNDN | 10 | Continuous | 0.50 | Yes | Foundation walls |
| S-SLAB | 10 | Continuous | 0.35 | Yes | Structural slabs |

### Grids (2 layers)

| Layer | Color | LT | LW | Plot | Description |
|-------|-------|----|----|------|-------------|
| C-GRID | 9 | Center | 0.25 | Yes | Column/reference grid lines |
| C-GRID-IDEN | 9 | Continuous | 0.18 | Yes | Grid bubbles/identifiers |

### Furniture and Equipment (3 layers)

| Layer | Color | LT | LW | Plot | Description |
|-------|-------|----|----|------|-------------|
| A-FURN | 8 | Continuous | 0.18 | Yes | Furniture |
| A-FURN-FIXT | 8 | Continuous | 0.18 | Yes | Fixtures (plumbing, etc.) |
| A-EQPM | 8 | Continuous | 0.18 | Yes | Equipment (appliances) |

### Annotation (6 layers)

| Layer | Color | LT | LW | Plot | Description |
|-------|-------|----|----|------|-------------|
| A-ANNO-DIMS | 7 | Continuous | 0.18 | Yes | Dimensions |
| A-ANNO-TEXT | 7 | Continuous | 0.18 | Yes | General text, notes |
| A-ANNO-NOTE | 7 | Continuous | 0.18 | Yes | Keynotes, general notes |
| A-ANNO-TAGS | 7 | Continuous | 0.18 | Yes | Door/window/room tags |
| A-ANNO-SYMB | 7 | Continuous | 0.18 | Yes | Symbols (north arrow, etc.) |
| A-ANNO-LEAD | 7 | Continuous | 0.18 | Yes | Leaders, callouts |

### Section and Elevation Markers (3 layers)

| Layer | Color | LT | LW | Plot | Description |
|-------|-------|----|----|------|-------------|
| A-SECT-IDEN | 6 | Continuous | 0.25 | Yes | Section identification marks |
| A-SECT-CUT | 6 | Continuous | 0.35 | Yes | Section cut lines |
| A-ELEV-IDEN | 6 | Continuous | 0.25 | Yes | Elevation identification marks |

### Hatches (4 layers)

| Layer | Color | LT | LW | Plot | Description |
|-------|-------|----|----|------|-------------|
| A-HATCH | 252 | Continuous | 0.13 | Yes | General hatching |
| A-HATCH-CONC | 252 | Continuous | 0.13 | Yes | Concrete hatch |
| A-HATCH-WOOD | 252 | Continuous | 0.13 | Yes | Wood hatch |
| A-HATCH-INSL | 252 | Continuous | 0.13 | Yes | Insulation hatch |

### Demolition (4 layers)

| Layer | Color | LT | LW | Plot | Description |
|-------|-------|----|----|------|-------------|
| A-DEMO | 14 | Phantom | 0.35 | Yes | General demolition |
| A-DEMO-WALL | 14 | Phantom | 0.35 | Yes | Walls to demolish |
| A-DEMO-DOOR | 14 | Phantom | 0.25 | Yes | Doors to demolish |
| A-DEMO-WIND | 14 | Phantom | 0.25 | Yes | Windows to demolish |

### Existing Conditions (3 layers)

| Layer | Color | LT | LW | Plot | Description |
|-------|-------|----|----|------|-------------|
| A-EXST-WALL | 253 | Continuous | 0.50 | Yes | Existing walls |
| A-EXST-DOOR | 253 | Continuous | 0.35 | Yes | Existing doors |
| A-EXST-WIND | 253 | Continuous | 0.35 | Yes | Existing windows |

### Site / Property (4 layers)

| Layer | Color | LT | LW | Plot | Description |
|-------|-------|----|----|------|-------------|
| C-PROP | 9 | Phantom | 0.25 | Yes | Property lines |
| C-TOPO | 9 | Continuous | 0.18 | Yes | Topography, contours |
| C-ROAD | 9 | Continuous | 0.25 | Yes | Roads, driveways |
| C-WALK | 9 | Continuous | 0.18 | Yes | Walkways, paths |

### Sheet / Viewport (2 layers)

| Layer | Color | LT | LW | Plot | Description |
|-------|-------|----|----|------|-------------|
| V-VPRT | 8 | Continuous | 0.18 | **No** | Viewport boundaries |
| V-TITL | 7 | Continuous | 0.18 | Yes | Title block elements |

### System Layers (2 layers)

| Layer | Color | LT | LW | Plot | Description |
|-------|-------|----|----|------|-------------|
| 0 | 7 | Continuous | Default | Yes | Default layer |
| Defpoints | 7 | Continuous | Default | No | System-managed |

---

## Usage by Drawing Type

### Floor Plan

**Primary layers:**
- A-WALL, A-WALL-CORE, A-WALL-INT, A-WALL-EXT
- A-DOOR, A-DOOR-FRM, A-DOOR-PANL, A-DOOR-SWNG
- A-WIND, A-WIND-FRM, A-WIND-GLAZ
- A-STRS, A-STRS-UP, A-STRS-DOWN, A-STRS-HAND
- A-FURN, A-FURN-FIXT, A-EQPM
- A-ANNO-DIMS, A-ANNO-TEXT, A-ANNO-TAGS

**Reference layers:**
- C-GRID, C-GRID-IDEN
- A-ROOF-OVER (shown as hidden lines above)
- A-CLNG (reflected ceiling reference)

**Example layer usage:**
```
New wall at cut plane      → A-WALL (Red, Continuous, 0.50)
Wall above cut plane       → A-WALL-OVER (Red, Hidden, 0.25)
Door opening              → A-DOOR (Orange, Continuous, 0.35)
Door swing arc            → A-DOOR-SWNG (Orange, Continuous, 0.18)
Window in plan            → A-WIND (Yellow-orange, Continuous, 0.35)
Dimension strings         → A-ANNO-DIMS (White, Continuous, 0.18)
Room names                → A-ANNO-TAGS (White, Continuous, 0.18)
```

### Reflected Ceiling Plan

**Primary layers:**
- A-CLNG, A-CLNG-GRID, A-CLNG-SOFF, A-CLNG-OPEN
- A-WALL-OVER (walls shown as reference)
- A-ANNO-DIMS, A-ANNO-TEXT, A-ANNO-SYMB

**Example layer usage:**
```
Ceiling outline           → A-CLNG (Gray, Hidden, 0.18)
Ceiling grid              → A-CLNG-GRID (Gray, Hidden, 0.13)
Soffit edges              → A-CLNG-SOFF (Gray, Hidden, 0.18)
Light fixtures            → A-FURN-FIXT (Gray, Continuous, 0.18)
```

### Roof Plan

**Primary layers:**
- A-ROOF, A-ROOF-EDGE, A-ROOF-RIDG, A-ROOF-VALY
- A-ROOF-DOWN
- A-ANNO-DIMS, A-ANNO-TEXT

**Example layer usage:**
```
Roof perimeter            → A-ROOF-EDGE (Green, Continuous, 0.35)
Ridge lines               → A-ROOF-RIDG (Green, Continuous, 0.35)
Valley lines              → A-ROOF-VALY (Green, Continuous, 0.25)
Downspout locations       → A-ROOF-DOWN (Green, Continuous, 0.18)
Slope arrows              → A-ANNO-SYMB (White, Continuous, 0.18)
```

### Building Section

**Primary layers:**
- A-WALL, A-WALL-CORE (cut elements heavy)
- A-FLOR, S-SLAB, S-FNDN (cut floor/structure)
- A-ROOF (cut roof structure)
- A-HATCH-CONC, A-HATCH-WOOD, A-HATCH-INSL (material hatches)
- A-ANNO-DIMS, A-ANNO-TEXT, A-ANNO-NOTE

**Example layer usage:**
```
Wall section cut          → A-WALL-CORE (Red, Continuous, 0.50)
Foundation cut            → S-FNDN (Red, Continuous, 0.50)
Concrete hatch            → A-HATCH-CONC (Lt Gray, Continuous, 0.13)
Insulation hatch          → A-HATCH-INSL (Lt Gray, Continuous, 0.13)
Dimension strings         → A-ANNO-DIMS (White, Continuous, 0.18)
```

### Demolition Plan

**Primary layers:**
- A-DEMO-WALL, A-DEMO-DOOR, A-DEMO-WIND
- A-EXST-WALL, A-EXST-DOOR, A-EXST-WIND
- A-WALL, A-DOOR, A-WIND (new work)
- A-ANNO-DIMS, A-ANNO-TEXT, A-ANNO-NOTE

**Layer visibility approach:**

| Phase | Existing | Demo | New |
|-------|----------|------|-----|
| Existing conditions | A-EXST-* visible | Off | Off |
| Demolition plan | A-EXST-* visible | A-DEMO-* visible | Off |
| New construction | A-EXST-* visible | Off | A-WALL, A-DOOR, etc. visible |

**Example layer usage:**
```
Existing wall to remain   → A-EXST-WALL (Dark gray, Continuous, 0.50)
Wall to be demolished     → A-DEMO-WALL (Green, Phantom, 0.35)
New wall                  → A-WALL (Red, Continuous, 0.50)
Demo note                 → A-ANNO-NOTE (White, Continuous, 0.18)
```

---

## Best Practices

### General Guidelines

1. **Always draw on the correct layer** - Set layer before drawing, not after
2. **Use ByLayer properties** - Never override color/linetype/lineweight on individual objects
3. **Keep layer 0 empty** - Only use for block definitions
4. **Freeze, don't turn off** - Frozen layers improve performance
5. **Use VP Freeze for sheets** - Control visibility per viewport

### Layer States

Create saved layer states for common view configurations:

| State Name | Description |
|------------|-------------|
| PLAN-ALL | All plan layers visible |
| PLAN-BASE | No furniture, no hatches |
| PLAN-DEMO | Demolition phase visibility |
| PLAN-EXIST | Existing conditions only |
| PLAN-NEW | New construction only |
| RCP | Reflected ceiling plan layers |
| ROOF | Roof plan layers |
| SECTION | Section/elevation layers |

### XREF Layer Management

When using external references:
- XREF layer names appear as `filename|layername`
- Control visibility via layer properties or VP Freeze
- Do not rename XREF layers

### Plotting Considerations

1. **V-VPRT is non-plotting** - Always place viewports here
2. **Use consistent CTB** - Map colors to lineweights consistently
3. **Test print at 100%** - Verify lineweights appear correctly
4. **Check layer plot setting** - Ensure no accidental "No" on plot layers

### Quality Control Checklist

Before submitting drawings:
- [ ] All objects on correct layers
- [ ] No objects on layer 0 (except in blocks)
- [ ] No color/LW/LT overrides on objects
- [ ] V-VPRT layer used for viewports
- [ ] Layer states saved for common views
- [ ] PURGE run (after drawing complete)
- [ ] AUDIT run with fixes

---

## Revision History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2024-XX | Initial standard based on NCS/UDS |

---

## Related Documents

- [LAYER_SCHEDULE.csv](LAYER_SCHEDULE.csv) - Complete layer definitions
- [Layer_Setup.scr](Layer_Setup.scr) - AutoCAD setup script
- [AUTOCAD_SCRIPTING_GUIDE.md](AUTOCAD_SCRIPTING_GUIDE.md) - Script syntax reference
