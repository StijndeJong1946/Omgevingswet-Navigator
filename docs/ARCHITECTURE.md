# Omgevingswet Navigator - Architecture

## Overview

The Omgevingswet Navigator extracts and structures the Dutch Environment and Planning Act (Omgevingswet) for navigation and legal analysis.

## Source Document

- **BWB ID**: BWBR0037885
- **Entry into force**: 2024-01-01
- **Source file**: `source/Omgevingswet.xml` (original, 4.25 MB)
- **Clean file**: `source/Omgevingswet_clean.xml` (stripped, 1.63 MB, -61.7%)

## Structure Analysis

### Summary

| Metric | Value |
|--------|-------|
| Chapters (Hoofdstukken) | 23 |
| Articles (Artikelen) | 724 |
| Has Bijlage (definitions) | Yes |

### Chapters (Hoofdstukken)

| Nr | Title | Articles | Content Type |
|----|-------|----------|--------------|
| 1 | Algemene bepalingen | 9 | Definitions, scope, goals |
| 2 | Taken en bevoegdheden van bestuursorganen | 53 | Competencies |
| 3 | Omgevingsvisies en programma's | 20 | Instruments |
| 4 | Algemene regels over activiteiten | 43 | General rules |
| 5 | De omgevingsvergunning en het projectbesluit | 65 | Permits |
| 6 | *Gereserveerd* | 0 | - |
| 7 | *Gereserveerd* | 0 | - |
| 8 | Aanvullende regels populatiebeheer, schadebestrijding en jacht | 5 | Wildlife |
| 9 | Voorkeursrecht | 21 | Pre-emption rights |
| 10 | Gedoogplichten | 44 | Tolerance obligations |
| 11 | Onteigening | 21 | Expropriation |
| 12 | Bijzondere instrumenten voor het inrichten van gebieden | 47 | Area development |
| 13 | Financiële bepalingen | 34 | Financial |
| 14 | *Gereserveerd* | 0 | - |
| 15 | Schade | 53 | Damages/compensation |
| 16 | Procedures | 174 | **Largest: procedural rules** |
| 17 | Adviesorganen en adviseurs | 11 | Advisory bodies |
| 18 | Handhaving en uitvoering | 34 | Enforcement |
| 19 | Bevoegdheden in bijzondere omstandigheden | 24 | Emergency powers |
| 20 | Monitoring en informatie | 31 | Monitoring |
| 21 | *Gereserveerd* | 0 | - |
| 22 | Overgangsrecht | 21 | Transitional law |
| 23 | Overige en slotbepalingen | 14 | Final provisions |

### Key Observations

1. **Chapter 16 (Procedures)** is the largest with 174 articles - core procedural logic
2. **Chapters 6, 7, 14, 21** are reserved (gereserveerd) - empty placeholders
3. **Bijlage** contains all begripsbepalingen (definitions) - referenced by Art. 1.1
4. **Chapter 5** covers omgevingsvergunning - key instrument, 65 articles

## Layer Model

```
Layer -1: External Content (EU, AMvBs: BAL, Bkl, Bbl)
Layer  0: Integration (external-systems.yaml)
Layer  1: Infrastructure (definitions, instruments, bevoegdheden)
Layer  2: Navigation (registry - TBD)
Layer  3: Legal Content (modules)
```

## Key Differences from BAL

| Aspect | BAL | Omgevingswet |
|--------|-----|--------------|
| Content type | Technical rules | Framework/procedures |
| Routing logic | Activity → Threshold → Rule | Instrument → Bevoegdheid → Procedure |
| Module granularity | Paragraph-level (374 modules) | TBD - likely chapter/afdeling level |
| Primary chapter | Chapter 3 (activities) | Chapter 16 (procedures) |
| Definitions location | Chapter 1 inline | Bijlage (appendix) |

## File Structure

```
source/
├── Omgevingswet.xml         # Original BWB XML
└── Omgevingswet_clean.xml   # Metadata-stripped version

infra/
├── definitions.yaml         # From Bijlage (TODO)
├── instruments.yaml         # Omgevingsplan, -vergunning, etc. (TODO)
├── bevoegdheden.yaml        # Competency mappings (TODO)
└── external-systems.yaml    # Links to AMvBs

scripts/
└── strip_metadata.py        # Metadata stripping tool
```
