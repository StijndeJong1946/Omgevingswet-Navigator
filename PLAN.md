# Omgevingswet Navigator - Master Plan

## Vision

Build a structured navigation system for the Omgevingswet that enables:
1. **Question-driven routing**: "Do I need a permit?" → Art. 5.1 → relevant rules
2. **Actor-aware navigation**: Different paths for gemeente, provincie, rijk, waterschap
3. **AMvB integration**: Seamless handoff to Bal/Bkl/Bbl when Ow delegates
4. **Procedural tracing**: Follow complete flows from aanvraag → besluit → rechtsbescherming

## Current State

### Completed ✓
- [x] Source XML obtained (Omgevingswet.xml, 4.25 MB)
- [x] Clean XML created (stripped metadata, 1.63 MB)
- [x] Instruments extracted (7 instruments in instruments.yaml)
- [x] Chapter 2 structure mapped (bevoegdheden.yaml)
- [x] Definitions extracted (262 begrippen in definitions.yaml)
- [x] External systems mapped (473 refs to 59 laws in external-systems.yaml)
- [x] Cross-reference analysis complete (hub articles, chapter links)
- [x] General mapping guide created (docs/GENERAL_MAPPING_GUIDE.md)

### In Progress
- [ ] Chapter skeletons (ch2, ch3, ch5 started)
- [ ] Unknown BWB ID identification (52 remaining)

---

## Architecture

### Layer Model

```
┌─────────────────────────────────────────────────────────────────────┐
│ Layer 3: LEGAL CONTENT                                              │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐    │
│ │ ch5-afd5.1  │ │ ch16-afd... │ │ ch4-afd4.1  │ │ ch2-afd2.5  │    │
│ │ Vergunning  │ │ Procedures  │ │ Regels      │ │ Instructies │    │
│ └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘    │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│ Layer 2: NAVIGATION                                                 │
│ ┌─────────────────────────────────────────────────────────────────┐ │
│ │ routing-registry.yaml                                           │ │
│ │ - Question → Entry point mapping                                │ │
│ │ - Actor-based route selection                                   │ │
│ │ - Cross-chapter flow definitions                                │ │
│ └─────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│ Layer 1: INFRASTRUCTURE                                             │
│ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌─────────────┐ │
│ │ definitions  │ │ instruments  │ │ bevoegdheden │ │ external-   │ │
│ │ .yaml        │ │ .yaml        │ │ .yaml        │ │ systems.yaml│ │
│ │ (262 terms)  │ │ (7 instrum.) │ │ (Ch2 struct) │ │ (59 laws)   │ │
│ └──────────────┘ └──────────────┘ └──────────────┘ └─────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│ Layer 0: INTEGRATION                                                │
│ ┌─────────────────────────────────────────────────────────────────┐ │
│ │ Links to: BAL Navigator, Bkl, Bbl, Or, Awb                      │ │
│ └─────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│ Layer -1: EXTERNAL CONTENT                                          │
│ Bal (activity rules) │ Bkl (quality rules) │ Bbl (building rules)  │
│ Awb (procedures)     │ EU Directives       │ International treaties│
└─────────────────────────────────────────────────────────────────────┘
```

### Hub Article Strategy

Navigation routes through these critical articles:

| Hub Article | Refs | Function | Routes To |
|-------------|------|----------|-----------|
| **Art. 4.3** | 45 | Gateway to AMvB rules | Bal, Bkl, Bbl |
| **Art. 2.3** | 37 | Subsidiariteit (actor routing) | Gemeente/Prov/Rijk |
| **Art. 5.1** | 25 | Vergunningplicht determination | Ch5 or Ch4 |
| **Art. 5.18** | 21 | Beoordelingsregels | Decision framework |
| **Art. 2.24** | 17 | Instructieregels | Governance mechanism |

---

## Phased Approach

### Phase 0: Discovery ✓ COMPLETE
- Obtain and analyze source XML
- Extract infrastructure data
- Map cross-references and linkages
- Document architecture

### Phase 1: Core Skeleton Mapping
**Goal**: Map decision logic for permit and rules chapters

**Priority Afdelingen**:
1. **H5 Afd 5.1** (49 art) - Omgevingsvergunning → CRITICAL
2. **H4 Afd 4.1** (14 art) - Algemene regels → CRITICAL
3. **H4 Afd 4.3** (26 art) - Bijzondere regels → HIGH
4. **H16 Afd 16.5** (17 art) - Vergunningprocedure → HIGH
5. **H2 Afd 2.5** (18 art) - Instructieregels → HIGH

**Deliverables**:
- ch5-skeleton.yaml (complete)
- ch4-skeleton.yaml
- ch16-skeleton.yaml (Afd 16.5 focus)
- ch2-skeleton.yaml (complete)

### Phase 2: Navigation Registry
**Goal**: Build routing logic that answers user questions

**Key Routes**:
```yaml
routes:
  permit_required:
    question: "Heb ik een vergunning nodig?"
    entry: "art_5.1"
    actor_split:
      default: gemeente
      exceptions: [art_5.10, art_5.12, art_5.14]
    exit_to: [ch16_procedure, ch4_rules]

  who_decides:
    question: "Wie is bevoegd gezag?"
    entry: "art_2.3"
    routing_table: "art_5.8_to_5.16"

  what_rules:
    question: "Welke regels gelden?"
    entry: "art_4.1"
    delegation: [bal, bkl, bbl, omgevingsplan]
```

**Deliverables**:
- routing-registry.yaml
- question-mapping.yaml

### Phase 3: Full Module Extraction
**Goal**: Extract complete decision flows for all afdelingen

**By Chapter Cluster**:

| Cluster | Chapters | Priority | Modules |
|---------|----------|----------|---------|
| Core Triangle | 2, 4, 5 | P1 | ~8 modules |
| Procedures | 16, 17 | P1 | ~14 modules |
| Policy | 3 | P2 | 2 modules |
| Land Dev | 9, 10, 11, 12 | P2 | ~10 modules |
| Finance | 13, 15 | P2 | ~6 modules |
| Support | 18, 19, 20 | P3 | ~6 modules |
| Transition | 22, 23 | P3 | ~4 modules |

**Deliverables**:
- Complete module set (~50 modules)
- Chapter coverage report

### Phase 4: Integration
**Goal**: Connect to BAL Navigator and test navigation

**Tasks**:
1. Map Art. 4.3 → BAL chapter 3 entries
2. Map Art. 5.1 activities → BAL activity modules
3. Build cross-navigator links
4. Create test cases for common questions
5. Validate coverage

**Deliverables**:
- bal-integration.yaml
- test-cases.yaml
- coverage-report.md

---

## Module Schema

Each module follows the skeleton schema (see SKELETON_MAPPING_GUIDE.md):

```yaml
_metadata:
  id: ow-mod-ch5-afd5.1
  chapter: 5
  afdeling: "5.1"
  title: "De omgevingsvergunning"
  article_range: "5.1 - 5.43"

skeleton:
  artikel_5.1:
    roles: [trigger, definition]
    determines: "Welke activiteiten vergunningplichtig zijn"
    routes_to:
      - target: "artikel 5.4"
        condition: "bepaling bevoegd gezag"
    delegates_to:
      - target: "Bal"
        for: "vergunningplichtige milieubelastende activiteiten"
    complexity:
      leden_count: 2
      has_exceptions: true

clusters:
  vergunningplicht:
    articles: ["5.1", "5.2", "5.3", "5.4"]
    entry_points: ["5.1"]
    exit_points: ["5.4"]
```

---

## Key Navigation Questions

The navigator must answer these core questions:

| # | Question | Entry | Key Flow |
|---|----------|-------|----------|
| 1 | Valt dit onder de Omgevingswet? | Art. 1.2 | Ch1 scope check |
| 2 | Welke regels gelden voor mijn activiteit? | Art. 4.1 | Ch4 → Bal/Bkl/Bbl |
| 3 | Heb ik een vergunning nodig? | Art. 5.1 | Ch5 Afd 5.1 |
| 4 | Wie is bevoegd gezag? | Art. 2.3 | Ch5 Art 5.4-5.16 |
| 5 | Welke procedure geldt? | Art. 16.1 | Ch16 Afd 16.5/16.7 |
| 6 | Kan ik afwijken van de regels? | Art. 4.5-4.7 | Maatwerk flow |
| 7 | Wat zijn de beoordelingscriteria? | Art. 5.18 | Ch5 + Bkl |
| 8 | Kan ik bezwaar/beroep maken? | Art. 16.85 | Ch16 + Awb |
| 9 | Wat kost het? | Art. 13.1 | Ch13 leges/kostenverhaal |
| 10 | Wie handhaaft? | Art. 18.1 | Ch18 handhaving |

---

## Validation Strategy

### Coverage Metrics
- % of articles with skeleton mapping
- % of cross-references resolved
- % of delegations mapped to target

### Quality Checks
1. Every article has assigned role(s)
2. Every delegation has target AMvB/verordening
3. No orphan articles (unreachable from entry points)
4. All hub articles have complete routing
5. Definitions used exist in definitions.yaml

### Test Cases
For each navigation question:
1. Define expected routing path
2. Trace through modules
3. Verify terminus (answer or handoff)
4. Check actor-specific variations

---

## Timeline (Suggested)

| Phase | Duration | Deliverables |
|-------|----------|--------------|
| Phase 1 | 2-3 sessions | Core skeletons (Ch2, Ch4, Ch5, Ch16 partial) |
| Phase 2 | 1-2 sessions | Routing registry, question mapping |
| Phase 3 | 4-6 sessions | Complete module set |
| Phase 4 | 2-3 sessions | BAL integration, testing |

---

## Open Questions

1. **Granularity**: Should modules be per-afdeling or per-cluster?
2. **Transition law**: How to handle Ch22 in routing (tijdelijk omgevingsplan)?
3. **AMvB depth**: How deep to trace delegations into Bal/Bkl/Bbl?
4. **UI layer**: What's the consumption target (CLI, web, API)?

---

## Files Reference

```
Omgevingswet Navigator/
├── CLAUDE.md              # Claude instructions
├── PLAN.md                # This file
├── source/
│   ├── Omgevingswet.xml   # Original (4.25 MB)
│   └── Omgevingswet_clean.xml  # Stripped (1.63 MB)
├── infra/
│   ├── definitions.yaml   # 262 begrippen ✓
│   ├── instruments.yaml   # 7 instruments ✓
│   ├── bevoegdheden.yaml  # Ch2 structure ✓
│   └── external-systems.yaml  # 59 laws, 473 refs ✓
├── modules/
│   ├── ch2-skeleton.yaml  # In progress
│   ├── ch3-skeleton.yaml  # In progress
│   ├── ch5-skeleton.yaml  # In progress
│   └── ch{X}-afd{X.Y}/    # Full modules (TBD)
├── scripts/
│   ├── extract_definitions.py
│   ├── extract_instruments.py
│   ├── extract_bevoegdheden.py
│   ├── extract_crossrefs.py
│   └── validate_*.py
└── docs/
    ├── ARCHITECTURE.md
    ├── METHODOLOGY.md
    ├── GENERAL_MAPPING_GUIDE.md  # Linkage analysis
    ├── SKELETON_MAPPING_GUIDE.md
    ├── MODULE_TEMPLATE.md
    └── ERRATA.md
```
