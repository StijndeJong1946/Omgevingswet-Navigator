# Claude Code Instructions for Omgevingswet Navigator

## Project Relationship

This project is a SIBLING to BAL Navigator (../BAL Navigator/).
DO NOT modify BAL Navigator files from this project.

## Current Phase

Phase 0: Discovery

## Source of Truth

Omgevingswet XML (BWBR0037885) from wetten.overheid.nl
Located at: `source/Omgevingswet.xml`

## Naming Convention

All IDs use `ow-` prefix:
- Definitions: `ow-def-{concept}`
- Modules: `ow-mod-ch{X}-{name}`
- Standards: `ow-std-{type}-{code}`

## Key Principles

1. Source XML is canonical - extract, don't interpret
2. Infrastructure first, modules second
3. Document discoveries in ERRATA.md
4. Validate coverage continuously

## Layer Model (adapted from BAL)

```
Layer -1: External Content (EU directives, AMvBs like BAL/Bkl/Bbl)
Layer  0: Integration/Adapter (external-systems.yaml)
Layer  1: Infrastructure (definitions, instruments, bevoegdheden)
Layer  2: Navigation (routing registry - TBD)
Layer  3: Legal Content (modules with procedural flows)
```
