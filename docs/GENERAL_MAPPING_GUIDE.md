# Omgevingswet General Mapping Guide

## Purpose

Map the **macro-level legal structure** of the Omgevingswet before detailed skeleton extraction. This guide identifies chapter types, cross-cutting concepts, and the relationships that navigation must support.

## Chapter Taxonomy

### Functional Classification

| Type | Chapters | Purpose | Priority |
|------|----------|---------|----------|
| **Framework** | 1, 2 | Scope, definitions, competencies | P0 (infra) |
| **Strategic Instruments** | 3 | Omgevingsvisie, programma | P2 |
| **Rules** | 4 | General rules about activities | P1 |
| **Operational Instruments** | 5 | Omgevingsvergunning, projectbesluit | P1 |
| **Domain-Specific** | 8, 9, 10, 11, 12 | Nature, property, land, expropriation | P3 |
| **Support Systems** | 13, 15, 16, 17, 18 | Finance, damages, procedures, enforcement | P1 (16), P2 (rest) |
| **Special Regimes** | 19, 20, 22, 23 | Emergencies, monitoring, transition | P3 |
| **Reserved** | 6, 7, 14, 21 | Future use (empty) | N/A |

### Chapter Dependency Graph

```
                    ┌─────────────────────────────────────────────────────────┐
                    │                  CHAPTER 1: Begrippen                   │
                    │        (Scope, definitions, zorgplicht, doelen)         │
                    └─────────────────────────────────────────────────────────┘
                                               │
                    ┌──────────────────────────┼──────────────────────────────┐
                    │                          │                              │
                    ▼                          ▼                              ▼
         ┌──────────────────┐      ┌──────────────────┐           ┌──────────────────┐
         │   CHAPTER 2      │      │   CHAPTER 3      │           │   CHAPTER 4      │
         │   Bevoegdheden   │◄────►│   Instrumenten   │           │   Regels         │
         │   (Who decides)  │      │   (Policy tools) │           │   (What's allowed)│
         └──────────────────┘      └──────────────────┘           └──────────────────┘
                    │                          │                              │
                    │              ┌───────────┴───────────┐                  │
                    │              ▼                       ▼                  │
                    │   ┌──────────────────┐    ┌──────────────────┐          │
                    │   │ Omgevingsvisie   │    │ Programma        │          │
                    │   └──────────────────┘    └──────────────────┘          │
                    │                                                         │
                    └─────────────────────────┬───────────────────────────────┘
                                              │
                                              ▼
                    ┌─────────────────────────────────────────────────────────┐
                    │                     CHAPTER 5                           │
                    │         Omgevingsvergunning & Projectbesluit            │
                    │              (Concrete permissions)                     │
                    └─────────────────────────────────────────────────────────┘
                                              │
                    ┌─────────────────────────┼─────────────────────────────┐
                    │                         │                             │
                    ▼                         ▼                             ▼
         ┌──────────────────┐     ┌──────────────────────┐      ┌──────────────────┐
         │   CHAPTER 16     │     │   CHAPTERS 8-12      │      │   CHAPTER 18     │
         │   Procedures     │     │   Domain-Specific    │      │   Handhaving     │
         │   (How to apply) │     │   (Special cases)    │      │   (Enforcement)  │
         └──────────────────┘     └──────────────────────┘      └──────────────────┘
                    │                                                       │
                    ▼                                                       │
         ┌──────────────────┐                                               │
         │   CHAPTER 17     │                                               │
         │   Adviesorganen  │◄──────────────────────────────────────────────┘
         └──────────────────┘
                    │
         ┌──────────┴──────────┐
         ▼                     ▼
┌──────────────────┐  ┌──────────────────┐
│   CHAPTER 13     │  │   CHAPTER 15     │
│   Financiën      │  │   Schade         │
└──────────────────┘  └──────────────────┘
```

## Cross-Cutting Concepts

### 1. Instrumenten (Legal Instruments)

| Instrument | Owner | Chapter | Purpose |
|------------|-------|---------|---------|
| **Omgevingsplan** | Gemeente | 2.4 | Rules for municipal territory |
| **Omgevingsverordening** | Provincie | 2.3 | Provincial rules |
| **Waterschapsverordening** | Waterschap | 2.5 | Water authority rules |
| **Omgevingsvisie** | Alle | 3.1 | Strategic vision |
| **Programma** | Alle | 3.2 | Action program |
| **Omgevingsvergunning** | BG | 5.1 | Activity permit |
| **Projectbesluit** | Rijk/Prov | 5.2 | Major project decision |

### 2. Actors (Bestuursorganen)

| Actor | Shortcode | Instruments | Primary Chapters |
|-------|-----------|-------------|------------------|
| **Rijk** | `rijk` | AMvBs, projectbesluit | 2, 4 (via Bal/Bkl) |
| **Provincie** | `prov` | Omgevingsverordening, projectbesluit | 2, 3, 5 |
| **Gemeente** | `gem` | Omgevingsplan | 2, 3, 5 |
| **Waterschap** | `ws` | Waterschapsverordening | 2 |

### 3. Governance Mechanisms

| Mechanism | From → To | Definition | Purpose |
|-----------|-----------|------------|---------|
| **Instructie** | Rijk/Prov → Decentraal | Art. 2.33-2.34 | One-time order |
| **Instructieregel** | Rijk/Prov → Decentraal | Art. 2.24-2.32 | Standing order |
| **Omgevingswaarde** | Any level | Art. 2.9-2.17 | Quality target |
| **Maatwerkregel** | Verordening | Art. 4.6 | Local deviation from Bal/Bkl |
| **Maatwerkvoorschrift** | BG → Initiator | Art. 4.5 | Case-specific deviation |
| **Gelijkwaardige maatregel** | Initiator | Art. 4.7 | Alternative compliance |

### 4. External References (Layer -1)

| AMvB | BWB ID | Primary Content | Referenced In |
|------|--------|-----------------|---------------|
| **Omgevingsbesluit (Ob)** | BWBR0044923 | Procedural details | Ch. 16, 17 |
| **Besluit kwaliteit leefomgeving (Bkl)** | BWBR0044924 | Quality rules, instructieregels | Ch. 2, 4 |
| **Besluit activiteiten leefomgeving (Bal)** | BWBR0044925 | Activity rules | Ch. 4, 5 |
| **Besluit bouwwerken leefomgeving (Bbl)** | BWBR0044926 | Building rules | Ch. 4, 5 |
| **Omgevingsregeling (Or)** | BWBR0045386 | Technical standards | scattered |

## Navigation Patterns

### Pattern 1: "What permit do I need?" (Activity → Permit Flow)

```
Activiteit → Ch4 (Is it regulated?) → Ch5 Afd5.1 (Vergunningplichtig?)
                                      ├─ Yes → Ch5 (Procedure via Ch16)
                                      └─ No → General rules apply (Ch4/Bal/Bbl)
```

**Key articles**: 4.1-4.7 (algemene regels), 5.1 (vergunningplicht), 5.4-5.16 (bevoegd gezag)

### Pattern 2: "Who decides?" (Bevoegd Gezag Routing)

```
Activiteit → Ch5 Art 5.4-5.16 (BG bepaling)
             ├─ Default: Gemeente (5.8-5.9)
             ├─ Province cases: 5.12-5.13
             ├─ Rijk cases: 5.10-5.11
             └─ Waterschap cases: 5.14
```

### Pattern 3: "What's the procedure?" (Procedure Flow)

```
Aanvraag/Besluit → Ch16 Afd16.1 (Algemeen)
                   ├─ Reguliere procedure (16.64-16.66)
                   └─ Uitgebreide procedure (16.65)

                   → Participatie (16.55-16.63)
                   → M.e.r. if applicable (16.43-16.54)
                   → Rechtsbescherming (16.85-16.87)
```

### Pattern 4: "Subsidiariteitsbeginsel" (Decentraal, tenzij)

```
Taak/Bevoegdheid → Default: Gemeente/Waterschap
                   ├─ Unless: Bovengemeentelijk belang → Provincie
                   └─ Unless: Nationaal belang → Rijk

Governed by: Art. 2.3 (algemene regel), specific articles per instrument
```

## Module Granularity Strategy

### Recommendation by Chapter Type

| Type | Granularity | Reasoning |
|------|-------------|-----------|
| **Chapter 1** | Single infra file | Definitions are atomic, cross-referenced everywhere |
| **Chapter 2** | Per afdeling | Clear functional separation (instruments, omgevingswaarden, instructies) |
| **Chapter 3-5** | Per afdeling | Each instrument gets its own module |
| **Chapter 8-12** | Per chapter | Domain-specific, less interconnected |
| **Chapter 16** | Per afdeling | Large chapter, clear procedural clusters |
| **Rest** | Per chapter | Support functions, moderate size |

## Extraction Priorities

### Phase 0: Infrastructure (Current)
1. ✅ Definitions (Bijlage → `definitions.yaml`)
2. ✅ Instruments (Ch2 afdelingen → `instruments.yaml`)
3. ✅ Bevoegdheden mapping (Ch2/Ch5 → `bevoegdheden.yaml`)
4. ✅ External references (→ `external-systems.yaml`)

### Phase 1: Core Navigation
1. Chapter 5 skeleton (vergunningplicht flow)
2. Chapter 4 skeleton (algemene regels routing)
3. Chapter 16 Afd 16.1 (procedural basics)

### Phase 2: Full Workflows
1. Complete Ch5 modules
2. Ch16 procedure modules
3. Ch2 instructie flows

### Phase 3: Domain Extensions
1. Chapters 8-12 (domain-specific)
2. Chapters 13, 15, 18 (support systems)
3. Chapters 19-23 (special/transitional)

## Key Questions for Navigation

Each module should answer one of these navigation questions:

| Question | Answer Location |
|----------|-----------------|
| "Valt mijn activiteit onder de Omgevingswet?" | Ch1 (scope) + Ch4 (activities) |
| "Welke regels gelden voor mijn activiteit?" | Ch4 → Bal/Bkl/Bbl |
| "Heb ik een vergunning nodig?" | Ch5 Afd5.1 |
| "Wie is bevoegd gezag?" | Ch5 Art 5.4-5.16 |
| "Welke procedure geldt?" | Ch16 |
| "Kan ik bezwaar maken?" | Ch16 Afd16.5 |
| "Wat zijn de financiële gevolgen?" | Ch13, Ch15 |
| "Wie handhaaft?" | Ch18 |

## Linkage Schema

### Internal References

```yaml
# Reference format within Omgevingswet
internal_ref:
  article: "5.1"
  lid: 1
  onderdeel: "a"
  full: "artikel 5.1, eerste lid, onderdeel a"
```

### External References

```yaml
# Reference to AMvB
external_ref:
  target: "Bal"  # or Bkl, Bbl, Ob, Or
  article: "3.10"
  topic: "milieubelastende activiteit"
```

### Instrument References

```yaml
# Reference to local instrument
instrument_ref:
  type: "omgevingsplan"
  owner: "gemeente"
  article_basis: "2.4"  # Omgevingswet grondslag
```

## Validation Rules

1. **Every article must have a role** (from skeleton schema)
2. **Every delegation must have a target** (AMvB or verordening)
3. **Every procedure article must link to Ch16**
4. **Every BG-related article must map to bevoegdheden.yaml**
5. **Definitions used must exist in definitions.yaml**

---

## Chapter Linkage Analysis (Extracted from Source)

### Cross-Chapter Reference Heatmap

| From ↓ / To → | H2 | H3 | H4 | H5 | H9 | H10 | H12 | H13 | H15 | H16 | H18 | H19 | H20 |
|---------------|----|----|----|----|----|----|-----|-----|-----|-----|-----|-----|-----|
| **H2** | - | 3 | 8 | 4 | - | - | - | - | - | 2 | - | - | 3 |
| **H3** | 10 | - | - | - | - | - | 1 | - | - | - | - | - | 3 |
| **H4** | 19 | - | - | 4 | - | - | - | - | - | - | - | - | - |
| **H5** | 15 | - | 6 | - | - | - | - | - | - | 7 | 1 | - | - |
| **H10** | 4 | 2 | 2 | 2 | - | - | 6 | - | - | - | - | - | - |
| **H12** | - | - | - | - | - | 1 | - | 1 | 1 | 3 | - | - | - |
| **H13** | - | - | - | 12 | - | 4 | 4 | - | 9 | 4 | - | - | - |
| **H15** | - | - | 5 | 3 | - | 9 | - | - | - | - | - | 3 | - |
| **H16** | 7 | - | - | 17 | 6 | - | 15 | 5 | - | - | - | - | - |
| **H18** | 1 | - | 12 | 12 | - | - | - | - | - | 1 | - | 2 | - |
| **H20** | 9 | 8 | - | - | - | - | - | - | - | 5 | - | - | - |
| **H22** | 9 | 1 | 3 | 4 | - | - | - | - | 2 | - | - | - | - |

### Hub Articles (Most Referenced)

These are the routing nexus points - critical for navigation:

| Article | Refs | Topic | Navigation Role |
|---------|------|-------|-----------------|
| **4.3** | 45 | Rijksregels over activiteiten | Gateway to Bal/Bkl/Bbl |
| **2.3** | 37 | Toedeling taken (subsidiariteit) | Actor routing |
| **5.1** | 25 | Vergunningplichtige activiteiten | Permit determination |
| **5.18** | 21 | Beoordelingsregels | Decision framework |
| **2.24** | 17 | Instructieregels | Governance mechanism |
| **5.3** | 12 | Meervoudige aanvraag | Procedure integration |
| **16.16** | 12 | Termijnen | Procedural timing |
| **16.7** | 12 | Aanvraagvereisten | Application rules |
| **13.14** | 12 | Kostenverhaal | Financial provisions |
| **2.22** | 11 | Omgevingsplan (gemeente) | Core instrument |
| **4.1** | 11 | Algemene regels | Rules framework |
| **16.43** | 11 | M.e.r.-plicht | Environmental assessment |
| **9.1** | 11 | Voorkeursrecht | Pre-emption trigger |
| **15.1** | 11 | Nadeelcompensatie | Damages entry |

### Structural Clusters

Based on cross-references, the law forms these logical clusters:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                          CORE TRIANGLE (Chapters 2-4-5)                        │
│                                                                                 │
│    ┌──────────────┐         19 refs        ┌──────────────┐                    │
│    │  Chapter 2   │◄───────────────────────│  Chapter 4   │                    │
│    │ Bevoegdheden │                        │   Regels     │                    │
│    └──────┬───────┘                        └──────┬───────┘                    │
│           │                                       │                            │
│      15   │   ┌───────────────────────────────────┘  4 refs                    │
│      refs │   │                                                                │
│           │   │                                                                │
│           ▼   ▼                                                                │
│    ┌──────────────┐                                                            │
│    │  Chapter 5   │ ◄─── CENTRAL: Vergunning & Projectbesluit                  │
│    └──────────────┘                                                            │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│                      PROCEDURE CLUSTER (Chapters 5-16-17-18)                   │
│                                                                                 │
│         Chapter 5                  Chapter 16                Chapter 18        │
│    ┌──────────────┐           ┌──────────────┐           ┌──────────────┐     │
│    │   Permits    │──17 refs─►│  Procedures  │◄──1 ref───│ Enforcement  │     │
│    └──────────────┘           └──────────────┘           └──────────────┘     │
│           │                          │                          │              │
│           │                          │                          │              │
│           └──────────────────────────┼──────────────────────────┘              │
│                                      ▼                                         │
│                              ┌──────────────┐                                  │
│                              │  Chapter 17  │                                  │
│                              │  Adviseurs   │                                  │
│                              └──────────────┘                                  │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│                    LAND DEVELOPMENT CLUSTER (Chapters 9-12)                    │
│                                                                                 │
│    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌────────────┐ │
│    │  Chapter 9   │    │  Chapter 10  │───►│  Chapter 12  │───►│ Chapter 15 │ │
│    │ Voorkeursrec │    │ Gedoogplicht │    │ Landinricht. │    │   Schade   │ │
│    └──────────────┘    └──────────────┘    └──────────────┘    └────────────┘ │
│           │                   │                   │                   ▲        │
│           │                   └───────────────────┼───────────────────┘        │
│           │                         6 refs        │                            │
│           │                                       │                            │
│           └────────────► Chapter 16 (procedures) ◄┘                            │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│                         FINANCE CLUSTER (Chapters 13-15)                       │
│                                                                                 │
│                              ┌──────────────┐                                  │
│                              │  Chapter 13  │                                  │
│                              │  Financieel  │                                  │
│                              └──────┬───────┘                                  │
│                                     │ 9 refs                                   │
│                                     ▼                                          │
│                              ┌──────────────┐                                  │
│                              │  Chapter 15  │                                  │
│                              │    Schade    │                                  │
│                              └──────────────┘                                  │
│                                     │                                          │
│                Links to: Ch5 (12), Ch10 (4), Ch12 (4), Ch16 (4)               │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### External Law Dependencies

| External Law | BWB ID | References | Key Articles Linking |
|--------------|--------|------------|---------------------|
| **Awb** | BWBR0005537 | 192 | 16.77b, 15.1, 16.82b, 16.110 |
| **Wet milieubeheer** | BWBR0003245 | 11 | 16.67, 10.6, 18.10, 23.3 |
| **Erfgoedwet** | BWBR0037521 | 9 | 5.2, 16.58, 19.8 |
| **Wet luchtvaart** | BWBR0005555 | 9 | 2.29, 10.7 |
| **Mijnbouwwet** | BWBR0014168 | 9 | 18.5a, 10.14, 10.9 |

**Note**: 52 unknown BWB IDs need identification for complete mapping.

### Linkage Implications for Navigator

1. **Chapter 2 is THE hub** - almost all chapters route through it for competencies
2. **Chapter 5 bridges** rules (Ch4) to procedures (Ch16) to enforcement (Ch18)
3. **Land development** forms a semi-autonomous cluster (9-10-11-12-15) but connects to core via Ch16
4. **Finance** (Ch13-15) heavily references permits (Ch5) for cost recovery
5. **Awb** is the procedural backbone - 192 references means deep Awb integration needed

### Navigation Entry Points

Based on linkage analysis, prioritize these entry points:

| User Question | Entry Point | Key Links |
|--------------|-------------|-----------|
| "What can I do?" | Art. 4.3 → Bal/Bkl | Ch4 → AMvBs |
| "Do I need a permit?" | Art. 5.1 | Ch5 → Ch4 → Ch16 |
| "Who decides?" | Art. 2.3 | Ch2 ↔ Ch5 |
| "What's the procedure?" | Art. 16.7 | Ch16 → Awb |
| "Can I be compensated?" | Art. 15.1 | Ch15 ← Ch5, Ch10 |
| "What if I don't comply?" | Art. 18.1 | Ch18 → Ch5, Ch4 |

---

## Delegation Patterns (Where Ow Routes Outward)

| Pattern | Count | Top Chapters | Implication |
|---------|-------|--------------|-------------|
| **bij AMvB** | 129 | H16(28), H5(19), H2(16) | Procedures & permits route to Bal/Bkl/Bbl |
| **bij ministeriële regeling** | 37 | H20(14), H2(7) | Monitoring/technical standards → Or |
| **bij verordening** | 20 | H2(13) | Competencies delegate to local level |
| **bij omgevingsplan** | 6 | H2(2), H3(2) | Strategic → local implementation |

**Key insight**: Chapter 16 has the most AMvB delegations (28) - procedural details are in Omgevingsbesluit.

---

## Actor Distribution Analysis

| Actor | Total | Top Chapters | Navigator Role |
|-------|-------|--------------|----------------|
| **Rijk** (minister) | 259 | H2(70), H5(39), H10(24) | National competencies, gedoogplichten |
| **Provincie** (GS) | 254 | H16(58), H2(43), H5(23) | Procedures, competencies, permits |
| **Gemeente** (B&W) | 180 | H16(40), H2(24), H19(17) | Procedures, competencies, emergencies |
| **Waterschap** | 78 | H2(26), H5(11), H3(10) | Competencies, permits, programma's |

**Key insight**: Actors cluster around Ch2 (competencies), Ch5 (permits), Ch16 (procedures).

---

## Instrument Distribution Analysis

| Instrument | Total | Primary Chapters | Coverage |
|------------|-------|------------------|----------|
| **Omgevingsvergunning** | 273 | H5(100), H16(88), H13(26) | Permits, procedures, finance |
| **Omgevingsplan** | 170 | H16(32), H22(30), H4(27) | Procedures, transition, rules |
| **Programma** | 137 | H3(52), H16(46), H22(13) | Policy, procedures, transition |
| **Projectbesluit** | 129 | H5(50), H16(37), H4(12) | Permits, procedures, rules |
| **Omgevingsverordening** | 81 | H2(30), H4(13), H5(11) | Competencies, rules, permits |
| **Waterschapsverordening** | 36 | H2(9), H5(8), H4(6) | Competencies, permits, rules |
| **Omgevingsvisie** | 21 | H3(7), H16(5), H9(3) | Policy, procedures, voorkeursrecht |
| **Maatwerkvoorschrift** | 7 | H4(3), H2(2), H12(1) | Limited use - case-specific |

**Key insight**: Omgevingsvergunning dominates (273 mentions). Chapter 22 (transition) mentions instruments heavily - important for current practice.

---

## Conditional Logic Hotspots (Decision Points)

| Marker | Count | Top Chapters | Navigation Use |
|--------|-------|--------------|----------------|
| **voor zover** | 164 | H16(27), H2(24), H5(18) | Scope limitations |
| **in afwijking van** | 66 | H16(20), H5(12), H2(8) | Exception handling |
| **tenzij** | 60 | H16(14), H5(7), H15(7) | Exception triggers |
| **onverminderd** | 14 | H2, H5, H15 (2 each) | Cumulative rules |

**Key insight**: Chapters 2, 5, 16 contain the most decision logic - these need careful skeleton mapping.

---

## Procedural Action Distribution

| Action | Count | Top Chapters | Module Relevance |
|--------|-------|--------------|------------------|
| **besluit/beslist** | 332 | H16(140), H5(40), H2(26) | Decision procedures |
| **aanvraag** | 206 | H16(111), H5(49), H15(16) | Application flows |
| **termijn** | 104 | H16(42), H9(13), H2(10) | Timing rules |
| **wijzig** | 102 | H16(37), H5(18), H4(8) | Modification procedures |
| **beroep** | 81 | H16(60), H11(6), H12(4) | Legal remedies |
| **intrek** | 33 | H16(12), H9(7), H5(6) | Revocation |
| **verleen** | 27 | H5(14), H2(2), H4(2) | Granting permits |

**Key insight**: Chapter 16 dominates all procedural actions - it's the procedural engine.

---

## Bijlage (Definitions Appendix) Structure

| Section | Count | Content |
|---------|-------|---------|
| **A - Begrippen** | 183 | Core legal definitions |
| **B - EU/International** | 79 | EU directives/regulations references |
| **Total** | 262 | All begripsbepalingen |

**Sample definitions** (navigation-critical):
- afvalstoffen, afvalwater (environmental)
- archeologisch monument (heritage)
- autosnelweg, autoweg (infrastructure)
- alarmeringswaarde (thresholds)

**Implication**: definitions.yaml must capture all 262 terms with cross-references to source articles.

---

## Bevoegd Gezag Determination Patterns

| Pattern | Articles | Key Examples |
|---------|----------|--------------|
| **Gedeputeerde Staten** | 98 | H2, H5, H12, H16 |
| **Minister** | 101 | H2, H10, H18, H19 |
| **B&W (gemeente)** | 37 | H2, H3, H5, H9 |
| **Waterschap** | 21 | H2, H5, H10 |
| **"bevoegd gezag is..."** | 11 | Art. 4.10-4.13a |

**Critical articles for BG routing**: 4.10, 4.11, 4.12, 4.13, 4.13a, 5.8-5.16

---

## Vergunningplicht Triggers

| Pattern | Count | Articles |
|---------|-------|----------|
| **verboden zonder vergunning** | 3 | 5.1, 5.3, 5.4 |
| **vergunningplicht** | 5 | 5.1, 5.2, 5.3, 5.4, 5.36b |
| **melding** | 21 | 4.4, 4.7, 4.8, 4.9, 4.14, 10.3, 12.24, 13.4b |

**Key insight**: Vergunningplicht is highly concentrated in Art. 5.1-5.4. Meldingsplicht is scattered.

---

## Afdeling Structure Summary

### High-Priority Afdelingen (by article count & centrality)

| Afdeling | Articles | Topic | Priority |
|----------|----------|-------|----------|
| **H5 Afd 5.1** | 49 | Omgevingsvergunning | P0 |
| **H15 Afd 15.3** | 35 | Schadeloosstelling onteigening | P2 |
| **H16 Afd 16.3** | 29 | Totstandkomingsprocedures | P0 |
| **H4 Afd 4.3** | 26 | Bijzondere regels activiteiten | P1 |
| **H16 Afd 16.4** | 24 | Milieueffectrapportage | P1 |
| **H16 Afd 16.9** | 24 | Onteigeningsprocedure | P2 |
| **H10 Afd 10.3** | 22 | Gedoogplichten bij beschikking | P2 |
| **H16 Afd 16.7** | 22 | Beslistermijn, bekendmaking | P1 |
| **H12 Afd 12.4** | 22 | Herverkaveling | P3 |

### Afdeling Clusters

```
PERMIT CLUSTER (Core Navigation)
├── H5 Afd 5.1 (49 art) - Omgevingsvergunning
├── H16 Afd 16.5 (17 art) - Vergunningprocedure
└── H16 Afd 16.7 (22 art) - Beslistermijn

RULES CLUSTER
├── H4 Afd 4.1 (14 art) - Algemene bepalingen
└── H4 Afd 4.3 (26 art) - Bijzondere bepalingen

PROCEDURE CLUSTER
├── H16 Afd 16.2 (18 art) - Coördinatie
├── H16 Afd 16.3 (29 art) - Totstandkoming
└── H16 Afd 16.4 (24 art) - M.e.r.

COMPETENCY CLUSTER
├── H2 Afd 2.4 (7 art) - Taaktoedeling
└── H2 Afd 2.5 (18 art) - Instructieregels
```

---

## Unknown BWB IDs to Identify

| BWB ID | Refs | Likely Law | From Articles |
|--------|------|------------|---------------|
| BWBR0005645 | 24 | Provinciewet | 13.10, 2.37, 16.137 |
| BWBR0005416 | 12 | Waterschapswet | 22.4, 2.34, 13.1a |
| BWBR0004287 | 12 | Woningwet | 16.139, 16.29, 22.5 |
| BWBR0005108 | 10 | Gemeentewet | 2.18, 22.15, 13.1a |
| BWBR0005290 | 10 | BW Boek 3 | 9.8, 16.131, 15.5 |
| BWBR0013798 | 9 | Wro | 5.40, 4.19b, 5.31 |
| BWBR0001827 | 9 | Rv | 16.90, 15.30, 15.37 |
| BWBR0008159 | 9 | Kaderwet adviescolleges | 17.2, 17.4, 17.5 |

**Action**: Verify these mappings and add to external-systems.yaml

---

## Emergent Insights (From Atomic Extraction)

### Paragraaf 5.1.1 Extraction (2026-01-28)

**Source observation**: The verbodsbepalingen (5.1-5.6) reveal:

| Artikel | Function | Pattern |
|---------|----------|---------|
| 5.1 | Core prohibition | "verboden... tenzij/voor zover AMvB" |
| 5.2 | Scope limitation | References 5.1 + 2.3 (subsidiariteit) |
| 5.3 | Decentrale plicht | "wanneer waterschapsverordening bepaalt" |
| 5.4 | Decentrale plicht | "wanneer omgevingsverordening bepaalt" |
| 5.5 | Enforcement hook | References 5.3, 5.4 |
| 5.6 | Specific prohibition | Standalone (instandlating) |

**Structural pattern**:
```
5.1 ─────┬──── 5.2 (begrenzing via 2.3)
         │
         ├──── 5.3 ────┬──── 5.5 (handhaving)
         │             │
         └──── 5.4 ────┘

5.6 (standalone)
```

**Delegation pattern discovered**:
- **Ow sets FRAMEWORK** (wat is verboden)
- **AMvB/verordening provides SPECIFICS** (welke gevallen)
- **Lid 1 logic**: DEFAULT verboden, TENZIJ AMvB vrijstelt
- **Lid 2 logic**: verboden VOOR ZOVER AMvB aanwijst

**Mapping implication**:
- PARAGRAAF boundaries are **meaningful** - legislator grouped intentionally
- Modules should respect paragraaf structure as primary unit
- Reference chains confirm logical groupings within paragraaf

### Paragraaf 5.1.2 Extraction (2026-01-28)

**Source observation**: The bevoegd gezag artikelen (5.7-5.16) form a DECISION TABLE:

| Artikel | Function | Pattern |
|---------|----------|---------|
| 5.7 | Reikwijdte aanvraag | "naar keuze aanvrager" + AMvB wateractiviteiten |
| 5.8 | **DEFAULT RULE** | "B&W beslist, TENZIJ 5.9/5.10/5.11/5.13" |
| 5.9 | Water exception | "dagelijks bestuur/GS/Minister bij AMvB" |
| 5.10 | Provincie exception | "GS bij AMvB, grenzen art. 2.3 lid 2" |
| 5.11 | Rijk exception | "Minister bij AMvB, grenzen art. 2.3 lid 3" |
| 5.12 | Meervoudige aanvraag | Routing via subsidiariteitsladder |
| 5.13 | Continuïteit | "eens bevoegd, altijd bevoegd" |
| 5.14 | Grensoverschrijdend | Zwaartepunt bepaalt |
| 5.15 | Scope koppeling | Wie verleent = wie wijzigt/intrekt |
| 5.16 | Flexibiliteit | Overdracht bij instemming |

**Decision tree discovered**:
```
Aanvraag → 5.8 (gemeente DEFAULT)
              │
              ├── TENZIJ 5.9 → wateractiviteit
              ├── TENZIJ 5.10 → provinciaal belang
              ├── TENZIJ 5.11 → nationaal belang
              └── TENZIJ 5.13 → eerder verleend

Meervoudig? → 5.12 (subsidiariteitsladder)
Grensoverschrijdend? → 5.14 (zwaartepunt)
```

**Key reference: Art. 2.3** (subsidiariteit) - referenced 4x as boundary condition

**Delegation pattern**:
- **Ow sets ROUTING LOGIC** (default + exceptions)
- **AMvB provides CASE LISTS** (welke gevallen)

**Connection to 5.1.1**:
- 5.1.1 = WAT heeft vergunningplicht
- 5.1.2 = WIE beslist op aanvraag

### Paragraaf 5.1.3 Extraction (2026-01-28)

**Source observation**: The beoordeling artikelen (5.17-5.33a) form a HUB-AND-SPOKE pattern:

| Artikel | Function | Pattern |
|---------|----------|---------|
| 5.17 | *ingetrokken* | - |
| 5.18 | **CENTRAL HUB** | "Bij AMvB worden regels gesteld over verlenen/weigeren" |
| 5.19 | Provincial extension | "Bij omgevingsverordening kunnen regels..." |
| 5.20 | Spoke: bouwactiviteit | → 5.18 + veiligheid, gezondheid, duurzaamheid |
| 5.21 | Spoke: omgevingsplanactiviteit | → 5.18 + toetsing aan omgevingsplan |
| 5.22 | Spoke: rijksmonumentenactiviteit | → 5.18 + cultureel erfgoed |
| 5.23 | Spoke: ontgrondingsactiviteit | → 5.18 |
| 5.24 | Spoke: wateractiviteit | → 5.18 + waterbeheer |
| 5.25 | *ingetrokken* | - |
| 5.26 | Spoke: milieubelastende activiteit | → 5.18 + BBT |
| 5.27 | Spoke: mijnbouwlocatieactiviteit | → 5.18 |
| 5.28 | Spoke: beperkingengebiedactiviteit | → 5.18 |
| 5.29 | Spoke: Natura 2000 / flora-fauna | → 5.18 + natuurbescherming |
| 5.29a | Spoke: jacht-gerelateerd | → 5.18 |
| 5.30 | Decentrale activiteiten | Gronden uit verordening (5.3/5.4) |
| 5.31-5.32 | Weigeringsgronden | Bibob + gezondheid (facultatief: "kan") |
| 5.33-5.33a | Special cases | Instemming + gedeeltelijke verlening |

**Hub-and-spoke structure**:
```
                    ┌─── 5.20 bouw
                    ├─── 5.21 omgevingsplan
                    ├─── 5.22 rijksmonument
        ┌───────────┼─── 5.23 ontgronding
        │           ├─── 5.24 water
5.18 ───┤           ├─── 5.26 milieu
 HUB    │           ├─── 5.27 mijnbouw
        │           ├─── 5.28 beperkingengebied
        │           ├─── 5.29 natuur
        └───────────└─── 5.29a jacht
```

**Activity mapping discovered**:
The spokes (5.20-5.29a) **mirror** the activity list in Art. 5.1:
- Navigator can route: activity type → 5.1 verbod → 5.20-5.29a assessment

**Delegation pattern**:
- **Ow (5.18)**: sets WHAT to assess
- **AMvB (Bkl)**: sets HOW to assess
- **Verordening (5.19, 5.30)**: provincial/local additions

### Paragraaf 5.1.4 + 5.1.5 Extraction (2026-01-28)

**Paragraaf 5.1.4 - Inhoud en werking** (5.34-5.37a):

| Artikel | Function | Key Concept |
|---------|----------|-------------|
| 5.34 | Voorschriften | Links beoordelingsregels → permit content |
| 5.36 | Termijnstelling | Voortdurend vs aflopend |
| 5.37 | Normadressaat | "degene die activiteit verricht" |
| 5.37a | Verantwoordelijkheidsverdeling | "in afwijking van 5.37" |

**Paragraaf 5.1.5 - Lifecycle** (5.38-5.43):

| Artikel | Function | Key Pattern |
|---------|----------|-------------|
| 5.38 | Actualisering | Periodieke review |
| 5.39 | Verplichting wijziging/intrekking | **MOET** (imperatief) |
| 5.40 | Bevoegdheid wijziging/intrekking | **KAN** (facultatief) |
| 5.41 | Op verzoek instemmingsorgaan | Via 16.16 |
| 5.43 | Revisievergunning | Consolidatie |

---

## AFDELING 5.1 COMPLETE - Summary

**Complete flow discovered**:
```
5.1.1 WAT is vergunningplichtig?
    │   └── verbod + tenzij/voor zover AMvB
    ▼
5.1.2 WIE beslist?
    │   └── gemeente DEFAULT, tenzij 5.9/5.10/5.11/5.13
    ▼
5.1.3 HOE wordt beoordeeld?
    │   └── 5.18 hub → 5.20-5.29a spokes
    ▼
5.1.4 WAT bevat de vergunning?
    │   └── voorschriften uit beoordelingsregels
    ▼
5.1.5 HOE verandert de vergunning?
        └── 5.39 (moet) vs 5.40 (kan)
```

**Key patterns confirmed**:
1. **Default + tenzij**: gemeente/verboden als default, expliciet genoemde uitzonderingen
2. **Hub-and-spoke**: centrale regel + activity-specific uitwerkingen
3. **Imperatief vs facultatief**: "wijzigt/trekt in" vs "kan wijzigen/kan intrekken"
4. **Delegation**: Ow = framework, AMvB = specifics

**Cross-chapter connections**:
- → Ch2: subsidiariteit (2.3), omgevingsplan (2.22), instructieregels (2.24)
- → Ch13: financiële zekerheid (13.5, 13.6)
- → Ch16: instemming (16.16), procedures
- → Ch18: handhaving (18.10)

### Afdeling 5.2 Extraction (2026-01-28)

**Source observation**: Projectprocedure (5.44-5.55) is for HIGHER LEVELS only:

| Paragraaf | Articles | Function |
|-----------|----------|----------|
| 5.2.1 | 5.44-5.46 | Bevoegd gezag + verplichting hoofdinfrastructuur |
| 5.2.2 | 5.47-5.50 | Voornemen → verkenning → voorkeursbeslissing |
| 5.2.3 | 5.51-5.54 | Inhoud + integraal karakter projectbesluit |
| 5.2.4 | 5.55 | Gemeentelijke route (via omgevingsplan) |

**Actor exclusion discovered**:
```
Projectbesluit (5.44): waterschap / GS / Minister
                       ↑
                 GEEN GEMEENTE
                       ↓
Gemeente (5.55): gebruikt projectprocedure-elementen
                 via OMGEVINGSPLAN
```

**Integraal besluit** (5.52):
- Wijzigt omgevingsplan (lid 1)
- Geldt als omgevingsvergunning (lid 2)
- Vervangt separate besluiten

**Connection to Afd 5.1**: Art. 5.53 maakt 5.1.3-5.1.5 van toepassing op projectbesluit.

---

## CHAPTER 5 COMPLETE

| Afdeling | Function | Bevoegd Gezag | Key Pattern |
|----------|----------|---------------|-------------|
| **5.1** | Omgevingsvergunning | Alle niveaus (default gemeente) | Regulier |
| **5.2** | Projectbesluit | Alleen hogere overheden | Integraal |

**Relationship**:
- Afd 5.1 = INDIVIDUAL permits for activities
- Afd 5.2 = INTEGRATED decision for major projects
- Afd 5.2 uses Afd 5.1 assessment framework (via 5.53)

---

## CHAPTER 4 COMPLETE (2026-01-28)

### Structure

| Afdeling | Articles | Function | Key Pattern |
|----------|----------|----------|-------------|
| **4.1** | 4.1-4.14 | WAT/HOE/WIE voor regels | 4.3 hub, 4.9 default+tenzij |
| **4.2** | 4.15-4.19b | Voorbereidingsbescherming | Tijdelijke bescherming |
| **4.3** | 4.20-4.43 | Bijzondere bepalingen | Hub-and-spoke (4.3 → 4.21-4.34) |

### Key Discovery: Ch4 and Ch5 are PARALLEL

```
CHAPTER 4 (Regels)              CHAPTER 5 (Vergunning)
──────────────────              ──────────────────────
4.1-4.3  WAT regels         ↔   5.1.1  WAT vergunningplichtig
4.4-4.7  HOE instrumenten   ↔   5.1.3  HOE beoordelen
4.8-4.14 WIE bevoegd gezag  ↔   5.1.2  WIE beslist
4.21-4.34 per activiteit    ↔   5.20-5.29a per activiteit
```

### Activity Alignment Discovered

The activities in **4.3 lid 1** MATCH the activities in **5.1 lid 1/2**:

| Art. 4.3 | Activity | Art. 5.1 |
|----------|----------|----------|
| 1a | bouwactiviteiten | 2a |
| 1b | milieubelastende activiteiten | 2b |
| 1c | lozingsactiviteiten | 2c |
| 1d | wateronttrekkingsactiviteiten | 2d |
| 1e | mijnbouwlocatieactiviteiten | 2e |
| 1f | beperkingengebiedactiviteiten | 2f |
| 1j | Natura 2000-activiteiten | 1e |
| 1k | flora- en fauna-activiteiten | 2g |

### Hub Articles Confirmed

| Chapter | Hub | Function | Refs |
|---------|-----|----------|------|
| **Ch4** | 4.3 | Gateway to Bal/Bkl/Bbl | 45 |
| **Ch4** | 4.9 | Default gemeente (tenzij) | - |
| **Ch5** | 5.8 | Default gemeente (tenzij) | - |
| **Ch5** | 5.18 | Assessment rules hub | 21 |

### Implication for Navigation

```
User: "What rules apply to my activity?"
  → Ch4: 4.3 (grondslag) → 4.21-4.34 (criteria) → Bal/Bkl/Bbl

User: "Do I need a permit?"
  → Ch5: 5.1 (vergunningplicht) → 5.20-5.29a (beoordeling) → Bkl

SAME ACTIVITIES, PARALLEL STRUCTURES, SAME AMvB DELEGATION
```

---

## CHAPTER 16 - PROCEDURES (Extraction 2026-01-28)

### Structure Overview

| Afdeling | Articles | Function | Priority |
|----------|----------|----------|----------|
| **16.1** | 16.1-16.6 | Algemene bepalingen | P2 |
| **16.2** | 16.7-16.21 | Coördinatie | P1 |
| **16.3** | 16.22-16.33l | Totstandkomingsprocedures | P2 |
| **16.4** | 16.34-16.53b | M.e.r. | P1 |
| **16.4a** | 16.53c | Strategische milieubeoordeling | P2 |
| **16.5** | 16.54-16.68 | **Omgevingsvergunning** | **P0** |
| **16.6** | 16.70-16.74 | Projectbesluit | P1 |
| **16.6a** | 16.75-16.76 | Bijzondere bepalingen | P2 |
| **16.7** | 16.77-16.90 | **Beslistermijn, inwerkingtreding, beroep** | **P0** |
| **16.8** | 16.91-16.92 | Gedoogplicht | P2 |
| **16.9** | 16.93-16.116 | Onteigening | P3 |
| **16.10** | 16.117-16.121 | Voorkeursrecht | P2 |
| **16.11** | 16.122-16.123 | Geldelijke regelingen | P3 |
| **16.12** | 16.124-16.137 | Landinrichting | P3 |
| **16.13** | 16.138 | Kavelruil | P3 |
| **16.14** | 16.139-16.140 | Bevoegdheidsoverdracht | P2 |

### Afdeling 16.5 - Omgevingsvergunning Procedures

**Key discovery: DEFAULT + TENZIJ pattern (identical to 4.9, 5.8)**

```
Art. 16.62: "Deze paragraaf [16.5.2 regulier] is van toepassing...
            TENZIJ paragraaf 16.5.3 [uitgebreid] daarop van toepassing is"
```

| Paragraaf | Function | Procedure Type |
|-----------|----------|----------------|
| 16.5.1 | Algemeen (indiening, ontvangst) | - |
| **16.5.2** | Reguliere procedure | **DEFAULT** |
| **16.5.3** | Toepassing Awb 3.4 | **TENZIJ** |
| 16.5.4 | Exploitatievoorschriften | Vervallen |

**Termijn structure:**

| Procedure | Beslistermijn | Verlenging |
|-----------|--------------|------------|
| Regulier | 8 weken | +6 weken (eenmaal) |
| Regulier + instemming | 12 weken | +6 weken (eenmaal) |
| Uitgebreid (Awb 3.4) | Awb termijnen | +6 weken (eenmaal) |

**Loketfunctie** (Art. 16.54):
```
Aanvraag INDIENEN bij: gemeente / waterschap
                       ↓ (ook als niet BG)
Loket DOORSTUURT naar: bevoegd gezag
                       ↓
Ontvangstdatum bij LOKET = startdatum termijn
```

**Lex silencio EXCLUSION** (Art. 16.64 lid 4):
- Awb paragraaf 4.1.3.3 is NIET van toepassing
- Geen vergunning van rechtswege bij termijnoverschrijding
- Critical design decision in Omgevingswet

**Connection to Ch5**:
```
Ch5  = WAT (vergunningplicht) + WIE (bevoegd gezag) + WAARAAN (beoordelen)
Ch16 = HOE (procedure verloopt)

Specifieke koppelingen:
- 16.55 → 5.3, 5.4 (decentrale vergunningen)
- 16.56 → 5.38, 5.42 (actualisering/wijziging)
```

### Afdeling 16.7 - Beslistermijn, Inwerkingtreding, Beroep

**Inwerkingtreding spectrum discovered:**

| Besluittype | Inwerkingtreding | Termijn |
|-------------|------------------|---------|
| **Omgevingsvergunning** (default) | dag NA bekendmaking | direct |
| **Omgevingsvergunning** (onomkeerbaar) | 4 weken na bekendmaking | + voorlopige voorziening schorst |
| **Omgevingsplan** | 4 weken na bekendmaking | vast |
| **Projectbesluit** | 4 weken na bekendmaking | of eerder bij spoed |
| **Projectbesluit waterschap** | 4 weken na goedkeuring GS | goedkeuringsvereiste |
| **Gebiedsinrichting** | na beroepstermijn/uitspraak | wacht op rechtskracht |

**Critical choice in 16.79:**
```
Omgevingsvergunning = dag na bekendmaking (SNEL!)
    ↓
TENZIJ onomkeerbare gevolgen (lid 2):
    a. wijziging bestaande toestand die niet kan worden hersteld
    b. regels strekken tot bescherming die toestand
    ↓
4 weken + voorlopige voorziening schorst (lid 4)
```

**Rechtsbescherming differentiatie:**

| Besluit | Rechter | Bijzonderheden |
|---------|---------|----------------|
| Standaard | Rechtbank → ABRvS | - |
| Projectbesluit | ABRvS (6 maanden) | Versnelde behandeling |
| Ruilbesluit | Civiele rechter | Geen hoger beroep, wel cassatie |
| Jachtgeweer | Minister J&V | Administratief beroep |

**Key insight**: Art. 16.87 verplicht ABRvS om binnen 6 maanden te beslissen op beroep tegen projectbesluit.

### Key Patterns from Chapter 16

1. **Default + tenzij** (consistent throughout Ow):
   - 16.62: regulier TENZIJ 16.5.3
   - Same pattern as 4.9 (gemeente TENZIJ), 5.8 (gemeente TENZIJ)

2. **Heavy Awb integration**:
   - 192 Awb-references in Omgevingswet
   - Ch16 builds on Awb 3.4 (uitgebreide procedure)
   - Awb as procedural backbone

3. **Termijn architecture**:
   - Opschorting (16.77): internationale verplichtingen
   - Beslistermijn (16.64): 8/12 weken
   - Inwerkingtreding (16.79): dag na / 4 weken
   - Rechterlijke termijn (16.87): 6 maanden

4. **Connection Ch5 ↔ Ch16**:
   ```
   Ch5 Afd 5.1 (Vergunning)    Ch16 Afd 16.5 (Procedure)
   ─────────────────────       ─────────────────────────
   5.1-5.6  WAT verboden   →   16.54-16.56  Indiening
   5.7-5.16 WIE beslist    →   16.62-16.64  Termijnen
   5.18-5.33 HOE beoordelen →  16.65-16.68  Uitgebreid
   5.34-5.43 INHOUD/LIFECYCLE → 16.79-16.82 Inwerkingtreding
   ```

### Navigation Update

| User Question | Primary | Procedural |
|---------------|---------|------------|
| "How do I apply?" | Ch5 5.1-5.6 | Ch16 16.54 |
| "How long will it take?" | - | Ch16 16.64 (8/12 weken) |
| "When can I start?" | - | Ch16 16.79 (dag na / 4 weken) |
| "Can I appeal?" | - | Ch16 16.83-16.90 |

---

## Cross-Chapter Pattern Confirmation

After extracting Ch4, Ch5, and Ch16, the following patterns are confirmed as **STRUCTURAL** (not coincidental):

### Pattern 1: DEFAULT + TENZIJ

| Article | Default | Exceptions Listed |
|---------|---------|-------------------|
| 4.9 | Gemeente BG | 4.10, 4.11, 4.12, 4.13 |
| 5.8 | Gemeente BG | 5.9, 5.10, 5.11, 5.13 |
| 16.62 | Reguliere procedure | 16.5.3 |

**Navigation implication**: Always check for TENZIJ articles when routing.

### Pattern 2: HUB-AND-SPOKE

| Chapter | Hub | Spokes | AMvB Target |
|---------|-----|--------|-------------|
| Ch4 | 4.3 | 4.21-4.34 | Bal/Bkl/Bbl |
| Ch5 | 5.18 | 5.20-5.29a | Bkl |

**Navigation implication**: Hub articles are gateways; spokes elaborate per activity.

### Pattern 3: IMPERATIEF vs FACULTATIEF

| Type | Examples | Signals |
|------|----------|---------|
| Imperatief (MOET) | 5.39, 16.64 lid 1 | "wijzigt", "beslist binnen", "worden gesteld" |
| Facultatief (KAN) | 5.40, 16.65 lid 4 | "kan wijzigen", "kan bepalen" |

### Pattern 4: DELEGATION CHAIN

```
Omgevingswet (framework)
    ↓ bij AMvB
Bal/Bkl/Bbl (specifics)
    ↓ kan maatwerkruimte bieden
Verordening (maatwerkregel via 4.6)
    ↓ kan individuele ruimte bieden
BG-besluit (maatwerkvoorschrift via 4.5)
```

---

## Module Status Summary

| Module | Status | Key Patterns Discovered |
|--------|--------|------------------------|
| ch5-par5.1.1-atomic.yaml | ✅ Complete | verbod + tenzij/voor zover |
| ch5-par5.1.2-atomic.yaml | ✅ Complete | default + tenzij decision tree |
| ch5-par5.1.3-atomic.yaml | ✅ Complete | hub-and-spoke (5.18 → 5.20-5.29a) |
| ch5-par5.1.4-5.1.5-v2-atomic.yaml | ✅ Complete V2 | imperatief vs facultatief, lifecycle pattern |
| ch5-afd5.2-v2-atomic.yaml | ✅ Complete V2 | projectbesluit = integraal, hiërarchie, doorbreking |
| ch4-afd4.1-atomic.yaml | ✅ Complete | 4.3 hub, 4.9 default+tenzij |
| ch4-afd4.2-4.3-v2-atomic.yaml | ✅ Complete V2 | Ch4 ↔ Ch5 parallel, hub-and-spoke 4.3, voorbescherming |
| ch16-afd16.5-v2-atomic.yaml | ✅ Complete V2 | procedure duality, loket, lex silencio, termijn_structure |
| ch16-afd16.7-atomic.yaml | ✅ Complete | inwerkingtreding spectrum |

### Afdeling 16.1 - Elektronisch verkeer en gegevens (2026-01-29)

**Key discovery: Houdbaarheidsregel (Art. 16.5)**

| Lid | Rule | Exception |
|-----|------|-----------|
| 1 | Onderzoeksgegevens ≤2 jaar oud bruikbaar | "in ieder geval" = niet limiterend |
| 2 | Ouder dan 2 jaar toegestaan | MITS actualiteit onderbouwd |
| 3 | Lid 1 NIET van toepassing op | Natura 2000 / flora-fauna |

**Praktijkbelang**: Voorkomt vertragende heronderzoeken, behalve voor natuur (EU-vereisten).

**Digitalisering (Art. 16.1)**:
- Landelijke voorziening (DSO) via art. 20.21
- Latere inwerkingtreding (2026-01-01)
- Afwijking Awb 2:7/2:8 mogelijk → volledig digitale verplichting

### Afdeling 16.3 - Totstandkomingsprocedures (2026-01-29)

**Key discovery: UOV als standaard voor alle Omgevingswet-instrumenten**

| Instrument | Artikel | Procedure |
|------------|---------|-----------|
| Omgevingsvisie | 16.26 | UOV |
| Programma's | 16.27 | UOV (6 maanden zienswijzen voor waterbeheerplannen) |
| Omgevingsplan | 16.30 | UOV + extra Awb-bepalingen (3:43-3:45) |
| Waterschapsverordening | 16.32 | UOV |
| Omgevingsverordening | 16.32 | UOV |
| Gedoogplichtbeschikking | 16.33 | UOV (spoeduitzonderingen mogelijk) |
| Onteigeningsbeschikking | 16.33b | UOV + rechtbankbekrachtiging |

**Actio popularis (Art. 16.23)**:
```
Hoofdregel: iedereen mag zienswijze indienen
    ↓
TENZIJ gedoogplichtbeschikking → belanghebbenden + bestuursorganen
TENZIJ onteigeningsbeschikking → alleen belanghebbenden
```

**Onteigeningsprocedure bijzonderheid**:
- Vereist rechtbankbekrachtiging (16.33d, 16.33e)
- Inwerkingtreding pas na rechterlijke uitspraak
- Meest ingrijpende eigendomsbesluit → meeste waarborgen

### Afdeling 16.4 - Milieueffectrapportage (2026-01-29)

**Key discovery: Dual-track structuur (SMB vs MER)**

| Track | Paragraaf | Scope | EU-richtlijn |
|-------|-----------|-------|--------------|
| **Plan-MER** | 16.4.1 | Omgevingsvisie, programma, omgevingsplan | SMB (2001/42/EG) |
| **Project-MER** | 16.4.2 | Aangewezen projecten (Omgevingsbesluit Bijlage V) | MER (2011/92/EU) |

**Getrapte plicht ontdekt (Art. 16.36, 16.43)**:

```
PLAN-MER:
├── AUTOMATISCH als kader voor project-mer (16.36.1)
├── AUTOMATISCH als passende beoordeling vereist (16.36.2)
└── CONDITIONEEL bij kleine gebieden met aanzienlijke effecten (16.36.3-4)

PROJECT-MER:
├── AUTOMATISCH boven drempel (16.43.1a) = mer-plicht
└── BEOORDELING onder drempel (16.43.1b) = mer-beoordelingsplicht
```

**Tiering principle (Art. 16.37, 16.52.3)**:
- Plan-MER detailniveau afgestemd op planfase
- Als locatie in plan-MER is bepaald → geen locatie-alternatieven meer in project-MER

**Commissie m.e.r. asymmetrie**:

| Track | Commissie-advies | Artikel |
|-------|-----------------|---------|
| Plan-MER | **VERPLICHT** | 16.39 |
| Project-MER | **FACULTATIEF** | 16.47 |

**MER als ontvankelijkheidsvereiste (Art. 16.49)**:
- Geen MER bij aanvraag → buiten behandeling
- MER voldoet niet → afwijzing (na herstelmogelijkheid)

**Grensoverschrijdend (Espoo-verdrag)**:
- Art. 16.42b (plan-MER) en 16.53b (project-MER)
- Bilaterale consultatie: NL als veroorzaker EN als ontvanger

### Afdeling 16.2 - Coördinatie (eerder geëxtraheerd)

**Key patterns (aanvulling)**:

| Concept | Functie | Artikelen |
|---------|---------|-----------|
| **Advies** | Niet-bindend | 16.15 |
| **Instemming** | Bindend veto | 16.16 |
| **Geen fictieve instemming** | Geen automatische consent bij termijnoverschrijding | 16.18 |
| **Reactieve interventie** | Provinciaal veto op omgevingsplan | 16.21 |

**Hiërarchie advies → instemming (16.15-16.16)**:
```
AMvB wijst aan:
    ├── Adviseur (16.15) → niet-bindend advies
    └── Instemmer (16.16) → bindende goedkeuring
        ↓
Gronden voor instemming:
    a. bijzondere deskundigheid
    b. zwaarwegende belangen (fysieke leefomgeving)
    c. provinciale belangen
```

---

## Cross-Chapter Pattern Confirmation (Extended)

### Pattern 5: UOV ALS PROCEDURELE NORM

| Afdeling | Instrumenten | Uitzondering |
|----------|--------------|--------------|
| 16.3 | Alle strategische instrumenten | Kennelijke verschrijving (16.24.2) |
| 16.4 | MER-plichtige besluiten | - |
| 16.5 | Uitgebreide vergunningprocedure | - |

**Awb 3.4 als backbone**: 192 Awb-verwijzingen in Omgevingswet

### Pattern 6: GEEN FICTIEVE BESCHIKKINGEN

| Besluittype | Geen fictie | Artikel |
|-------------|-------------|---------|
| Omgevingsvergunning | Geen lex silencio | 16.64.4 |
| Instemming | Geen fictieve instemming | 16.18.2 |

**Ontwerpkeuze**: Omgevingswet sluit automatische vergunning/consent expliciet uit

### Pattern 7: RECHTERLIJKE CONTROLE SPECTRUM

| Ingrijpendheid | Controle | Voorbeelden |
|----------------|----------|-------------|
| Laag | Bestuursrechter achteraf | Omgevingsvergunning |
| Midden | Rechtbank vooraf (bekrachtiging) | Onteigeningsbeschikking |
| Hoog | Civiele rechter | Ruilbesluit |

---

## Module Status Summary (Updated)

| Module | Status | Key Patterns Discovered |
|--------|--------|------------------------|
| ch5-par5.1.1-atomic.yaml | ✅ Complete | verbod + tenzij/voor zover |
| ch5-par5.1.2-atomic.yaml | ✅ Complete | default + tenzij decision tree |
| ch5-par5.1.3-atomic.yaml | ✅ Complete | hub-and-spoke (5.18 → 5.20-5.29a) |
| ch5-par5.1.4-5.1.5-v2-atomic.yaml | ✅ Complete V2 | imperatief vs facultatief, lifecycle pattern |
| ch5-afd5.2-v2-atomic.yaml | ✅ Complete V2 | projectbesluit = integraal, hiërarchie, doorbreking |
| ch4-afd4.1-atomic.yaml | ✅ Complete | 4.3 hub, 4.9 default+tenzij |
| ch4-afd4.2-4.3-v2-atomic.yaml | ✅ Complete V2 | Ch4 ↔ Ch5 parallel, hub-and-spoke 4.3, voorbescherming |
| ch16-afd16.1-atomic.yaml | ✅ Complete | houdbaarheid data, DSO |
| ch16-afd16.2-atomic.yaml | ✅ Complete | advies vs instemming, reactieve interventie |
| ch16-afd16.3-atomic.yaml | ✅ Complete | UOV-standaard, actio popularis |
| ch16-afd16.4-atomic.yaml | ✅ Complete | dual-track MER, tiering, Commissie asymmetrie |
| ch16-afd16.5-v2-atomic.yaml | ✅ Complete V2 | procedure duality, loket, lex silencio, termijn_structure |
| ch16-afd16.7-atomic.yaml | ✅ Complete | inwerkingtreding spectrum |
| ch16-afd16.4a-atomic.yaml | ✅ Complete | passende beoordeling, Habitatrichtlijn |
| ch16-afd16.6-16.6a-atomic.yaml | ✅ Complete | projectprocedure, kostenverhaal |
| ch16-afd16.8-16.14-atomic.yaml | ✅ Complete | domain-specific (voorkeursrecht, onteigening, etc.) |

### CHAPTER 16 COMPLETE

All 14 afdelingen of Chapter 16 (Procedures) have been extracted:

| Afdeling | Articles | Module | Key Patterns |
|----------|----------|--------|--------------|
| 16.1 | 16.1-16.6 | ch16-afd16.1 | houdbaarheid data, DSO |
| 16.2 | 16.7-16.21 | ch16-afd16.2 | advies vs instemming |
| 16.3 | 16.22-16.33l | ch16-afd16.3 | UOV voor alle instrumenten |
| 16.4 | 16.34-16.53b | ch16-afd16.4 | MER dual-track |
| 16.4a | 16.53c | ch16-afd16.4a | passende beoordeling |
| 16.5 | 16.54-16.68 | ch16-afd16.5 | vergunningprocedure |
| 16.6 | 16.70-16.74 | ch16-afd16.6-16.6a | projectprocedure |
| 16.6a | 16.75-16.76 | ch16-afd16.6-16.6a | kostenverhaal |
| 16.7 | 16.77-16.90 | ch16-afd16.7 | beslistermijn, beroep |
| 16.8-16.14 | 16.91-16.140 | ch16-afd16.8-16.14 | domain-specific |

---

## CHAPTER 2 - BEVOEGDHEDEN (Extraction 2026-01-29)

### Structure Overview

| Afdeling | Articles | Function | Key Pattern |
|----------|----------|----------|-------------|
| **2.1** | 2.1-2.3 | Algemene bepalingen | Subsidiariteitsbeginsel |
| **2.2** | 2.4-2.8 | Omgevingsplan etc. | One-plan-principle |
| **2.3** | 2.9-2.15a | Omgevingswaarden | Resultaat vs inspanning |
| **2.4** | 2.16-2.21a | Taaktoedeling | Per-level task assignment |
| **2.5** | 2.22-2.37 | Instructieregels en instructies | Governance mechanisms |
| **2.6** | 2.38-2.46 | Bijzondere taken | Stikstof, natuur, water |

### Afdeling 2.1 - Algemene bepalingen (Constitutional Core)

**Key discovery: Art. 2.3 subsidiariteitsbeginsel**

```
Subsidiariteitsladder:
├── Art. 2.3 lid 1: Gemeente = DEFAULT
├── Art. 2.3 lid 2: Provincie TENZIJ bovengemeentelijk belang
└── Art. 2.3 lid 3: Rijk TENZIJ provinciegrensoverschrijdend/nationaal belang
```

**Art. 2.1 - Doelgebondenheid**:
- Lid 1: Taken/bevoegdheden ALLEEN voor doelen Ow
- Lid 2: Integratiebeginsel (samenhang 19 belangen)
- Lid 3: 19-belangen catalogus:
  - a. veiligheid (7 items)
  - b. gezondheid (4 items)
  - c. milieu (6 items)
  - d. duurzame ontwikkeling (2 items)

**Art. 2.2 - Bestuursorgaancatalogus**:
- Lid 2a: B&W
- Lid 2b: GS
- Lid 2c: Dagelijks bestuur waterschap
- Lid 2d-g: Ministers + Dienst Hydrografie

### Afdeling 2.2 - Instrumentgrondslag

**One-plan-principle confirmed (Art. 2.4-2.6)**:

| Niveau | Instrument | Bevoegd gezag | Artikel |
|--------|------------|---------------|---------|
| Gemeente | Omgevingsplan | Gemeenteraad | 2.4 |
| Waterschap | Waterschapsverordening | Algemeen bestuur | 2.5 |
| Provincie | Omgevingsverordening | Provinciale staten | 2.6 |

**Exclusiviteit (Art. 2.7)**:
- Lid 1: AMvB kan verplichten opname in Ow-instrument
- Lid 2: AMvB kan uitsluiten uit Ow-instrument
- Doel: Voorkom samenloop met APV etc.

**Delegatie (Art. 2.8)**: Van vertegenwoordigend → dagelijks bestuur (delen)

### Afdeling 2.3 - Omgevingswaarden

**Key discovery: Resultaatverplichting vs inspanningsverplichting (Art. 2.10)**

| Type | Signaal | Juridische gevolgen |
|------|---------|---------------------|
| **Resultaat** | "worden bereikt", "is verplicht" | Harde deadline, rechtsgevolgen bij overschrijding |
| **Inspanning** | "worden nagestreefd" | Best-effort, geen automatische sanctie |

**Critical: Stikstofomgevingswaarden (Art. 2.15a)**

| Deadline | Target | Type |
|----------|--------|------|
| 1 jan 2025 | 40% areaal < KDW | Inspanning |
| 1 jan 2030 | 50% areaal < KDW | Inspanning |
| 1 jan 2035 | **74% areaal < KDW** | **Resultaat** |

**KDW** = Kritische Depositiewaarde (stikstofdepositie waaronder natuur niet verslechtert)

**Omgevingswaarde-hiërarchie**:

| Niveau | Bevoegdheid | Domeinen |
|--------|-------------|----------|
| Gemeente | Facultatief | Lokale kwaliteit |
| Provincie | Verplicht | Geluid industrieterrein |
| Rijk | Verplicht | Luchtkwaliteit, waterkwaliteit, natuur, stikstof |

### Afdeling 2.4 - Taaktoedeling

**Key discovery: Hub-and-spoke per niveau**

```
Art. 2.16 (gemeente)     Art. 2.18 (provincie)     Art. 2.19 (Rijk)
├── bodem                ├── grondwater            ├── rijkswateren
├── geluid               ├── regionale wateren     ├── primaire keringen
├── lokale wegen         ├── provinciale wegen     ├── rijkswegen
├── bouwen               ├── stiltegebieden        ├── defensie
└── ... (21 items)       └── ... (18 items)        └── ... (12 items)
```

**Waterschap (Art. 2.17)**: Functioneel beperkt tot watersysteem + waterkeringen

**Beperkingengebieden (Art. 2.20-2.21a)**:
- Wegen, spoorwegen, luchthavens, waterstaatswerken
- Beperkingengebiedactiviteit = vergunningplichtig (→ Ch5)

### Afdeling 2.5 - Instructieregels en instructies

**Key discovery: Instructieregel vs instructie**

| Type | Karakter | Artikel | Voorbeeld |
|------|----------|---------|-----------|
| **Instructieregel** | Algemeen/permanent | 2.22-2.32 | Bkl instructieregels voor omgevingsplan |
| **Instructie** | Concreet/eenmalig | 2.33-2.34 | GS geeft instructie aan gemeente |

**Instructieregels cascade**:

```
Rijk (AMvB/ministeriële regeling):
├── Art. 2.24: Instructieregels voor omgevingsplan
├── Art. 2.25: Instructieregels voor omgevingsverordening
├── Art. 2.26: Instructieregels voor programma's
│   └── 11 EU-richtlijnen expliciet (KRW, ROR, NEC, etc.)
└── Art. 2.27-2.29: Instructieregels per domein (water, luchtvaart)

Provincie (omgevingsverordening):
├── Art. 2.22: Instructieregels voor omgevingsplan
├── Art. 2.23: Instructieregels waterschapsverordening
└── Art. 2.30: Instructieregels voor programma's
```

**Indeplaatstreding (Art. 2.36-2.37)**:
- GS/Minister kunnen besluit nemen als bestuursorgaan faalt
- Ernstige ultimum remedium - pas na waarschuwing

**Vernietiging waterschap (Art. 2.35)**:
- GS kunnen waterschapsbesluit vernietigen
- Bijzondere relatie provincie-waterschap

### Afdeling 2.6 - Bijzondere taken en bevoegdheden

**Key discovery: Stikstof-complex**

```
Art. 2.15a (omgevingswaarde) ←→ Art. 2.46 (depositieruimte)
        │                              │
        │                              └── Register + toedeling
        └── 40%/50%/74% targets
                    │
                    └──→ Art. 16.53c (passende beoordeling)
```

**Water-cluster (Art. 2.38-2.43)**:

| Artikel | Instrument | Bevoegd gezag |
|---------|------------|---------------|
| 2.39 | Legger (waterstaatswerken) | Waterschap |
| 2.40 | Calamiteitenplan | Waterschap |
| 2.41 | Peilbesluit | Waterschap |
| 2.42 | Verdringingsreeks | Minister |

**Gelaagde gebiedsaanwijzing natuur (Art. 2.44)**:

| Niveau | Gebiedstype | Bevoegd gezag |
|--------|-------------|---------------|
| EU | Natura 2000-gebieden | Minister |
| Nationaal | NNN (Bijzondere nationale natuurgebieden) | Minister |
| Provinciaal | Overige natuurgebieden | GS |

**Stikstofdepositieruimte (Art. 2.46)**:
- Lid 1: Minister registreert ruimte
- Lid 2: GS kunnen toedelen
- Lid 3: AMvB regelt procedure
- Critical voor vergunningverlening

---

## Cross-Chapter Pattern Confirmation (Extended with Ch2)

### Pattern 8: SUBSIDIARITEIT ALS STRUCTUURBEGINSEL

| Artikel | Toepassing | Default |
|---------|------------|---------|
| 2.3 | Taaktoedeling algemeen | Gemeente |
| 5.8 | Bevoegd gezag vergunning | Gemeente (B&W) |
| 4.9 | Bevoegd gezag regels | Gemeente (B&W) |

**Consistently**: Gemeente = DEFAULT, hoger niveau = TENZIJ + onderbouwing

### Pattern 9: DOELGEBONDENHEID

| Artikel | Werking |
|---------|---------|
| 2.1 lid 1 | Alle taken/bevoegdheden gebonden aan Ow-doelen |
| 2.1 lid 2 | Integratiebeginsel (samenhang belangen) |
| 2.1 lid 3 | 19-belangen catalogus als toetsingskader |

**Implication**: Navigator kan checken of besluit past bij doelstelling

### Pattern 10: ONE-PLAN-PRINCIPLE

| Niveau | Voormalige fragmentatie | Nu |
|--------|------------------------|-----|
| Gemeente | Bestemmingsplan, APV, bouwverordening, etc. | 1 omgevingsplan |
| Waterschap | Keur, diverse verordeningen | 1 waterschapsverordening |
| Provincie | Diverse verordeningen | 1 omgevingsverordening |

### Pattern 11: GOVERNANCE HIËRARCHIE

```
Instructieregel (algemeen, preventief)
    │
    └──→ Instructie (concreet, curatief)
              │
              └──→ Indeplaatstreding (ultimum remedium)
                        │
                        └──→ Vernietiging (only waterschap)
```

---

## Module Status Summary (Updated with Ch2)

| Module | Status | Key Patterns Discovered |
|--------|--------|------------------------|
| ch5-par5.1.1-atomic.yaml | ✅ Complete | verbod + tenzij/voor zover |
| ch5-par5.1.2-atomic.yaml | ✅ Complete | default + tenzij decision tree |
| ch5-par5.1.3-atomic.yaml | ✅ Complete | hub-and-spoke (5.18 → 5.20-5.29a) |
| ch5-par5.1.4-5.1.5-v2-atomic.yaml | ✅ Complete V2 | imperatief vs facultatief, lifecycle pattern |
| ch5-afd5.2-v2-atomic.yaml | ✅ Complete V2 | projectbesluit = integraal, hiërarchie, doorbreking |
| ch4-afd4.1-atomic.yaml | ✅ Complete | 4.3 hub, 4.9 default+tenzij |
| ch4-afd4.2-4.3-v2-atomic.yaml | ✅ Complete V2 | Ch4 ↔ Ch5 parallel, hub-and-spoke 4.3, voorbescherming |
| ch16-afd16.1-v2-atomic.yaml | ✅ Complete V2 | houdbaarheid data, DSO |
| ch16-afd16.2-v2-atomic.yaml | ✅ Complete V2 | advies vs instemming, reactieve interventie, Awb 3.5 coördinatie |
| ch16-afd16.3-v2-atomic.yaml | ✅ Complete V2 | UOV-standaard, actio popularis, rechterlijke bekrachtiging |
| ch16-afd16.4-v2-atomic.yaml | ✅ Complete V2 | dual-track MER, tiering, Commissie asymmetrie |
| ch16-afd16.4a-v2-atomic.yaml | ✅ Complete V2 | passende beoordeling, Habitatrichtlijn art. 6 lid 3 |
| ch16-afd16.5-v2-atomic.yaml | ✅ Complete V2 | procedure duality, loket, lex silencio, termijn_structure |
| ch16-afd16.6-16.6a-v2-atomic.yaml | ✅ Complete V2 | projectprocedure UOV, waterschap GS-goedkeuring, kostenverhaal aanhouding |
| ch16-afd16.7-v2-atomic.yaml | ✅ Complete V2 | inwerkingtreding spectrum, uitgestelde inwerkingtreding, beroepsbundeling |
| ch16-afd16.8-16.14-v2-atomic.yaml | ✅ Complete V2 | rechterlijke bekrachtiging onteigening, landinrichting, delegatiegrondslag |
| **ch2-afd2.1-atomic.yaml** | ✅ Complete | subsidiariteit, doelgebondenheid, 19 belangen |
| **ch2-afd2.2-atomic.yaml** | ✅ Complete | one-plan-principle, exclusiviteit |
| **ch2-afd2.3-atomic.yaml** | ✅ Complete | omgevingswaarden, resultaat vs inspanning, stikstof |
| **ch2-afd2.4-atomic.yaml** | ✅ Complete | taaktoedeling per niveau, beperkingengebieden |
| **ch2-afd2.5-atomic.yaml** | ✅ Complete | instructieregels vs instructies, indeplaatstreding |
| **ch2-afd2.6-atomic.yaml** | ✅ Complete | water, natuur, stikstofdepositieruimte |

### CHAPTER 2 COMPLETE

All 6 afdelingen of Chapter 2 (Bevoegdheden) have been extracted:

| Afdeling | Articles | Module | Key Patterns |
|----------|----------|--------|--------------|
| 2.1 | 2.1-2.3 | ch2-afd2.1 | subsidiariteit, doelgebondenheid |
| 2.2 | 2.4-2.8 | ch2-afd2.2 | one-plan-principle |
| 2.3 | 2.9-2.15a | ch2-afd2.3 | omgevingswaarden, stikstof |
| 2.4 | 2.16-2.21a | ch2-afd2.4 | taaktoedeling |
| 2.5 | 2.22-2.37 | ch2-afd2.5 | instructieregels |
| 2.6 | 2.38-2.46 | ch2-afd2.6 | bijzondere taken |

### Cross-Chapter Connections Confirmed

```
Ch2 ←→ Ch4: 2.3 subsidiariteit → 4.9 default gemeente
Ch2 ←→ Ch5: 2.3 subsidiariteit → 5.8 default gemeente
Ch2 ←→ Ch5: 2.20-2.21a beperkingengebied → 5.1 vergunningplicht
Ch2 ←→ Ch16: 2.15a omgevingswaarde → 16.53c passende beoordeling
Ch2 ←→ Ch16: 2.46 stikstofdepositieruimte → 16.53c toedeling
```

---

## CHAPTER 18 - HANDHAVING EN UITVOERING (Extraction 2026-01-29)

### Structure Overview

| Afdeling | Articles | Function | Key Pattern |
|----------|----------|----------|-------------|
| **18.1** | 18.1-18.16b | Bestuursrechtelijke handhaving | Wie verleent = wie handhaaft |
| **18.2** | 18.17 | Strafrechtelijke handhaving | EEZ-rechtsmacht |
| **18.3** | 18.18-18.27 | Kwaliteitsbevordering | Omgevingsdiensten |

### Afdeling 18.1 - Bestuursrechtelijke handhaving

**Key discovery: Art. 18.2 - Wie verleent, handhaaft**

```
Handhavingstaak volgt BG-toedeling:
├── Lid 1: activiteit met regels (§4.1.1) → BG van §4.1.3
├── Lid 2: vergunningplichtig → BG van §5.1.2
├── Lid 3: projectbesluit → vaststeller projectbesluit
├── Lid 4: gedoogplicht → alleen als AMvB toewijst
├── Lid 5: overige → B&W (DEFAULT)
└── Lid 6: AMvB kan afwijken (binnen art. 2.3)
```

**Critical pattern confirmed**: Same default + tenzij structure as Ch4/Ch5

**Handhavingsinstrumenten hiërarchie**:

| Instrument | Artikel | Karakter |
|------------|---------|----------|
| Toezicht | 18.1a | Preventief |
| Last onder bestuursdwang | 18.4 | Reparatoir |
| Last onder dwangsom | 18.4a | Reparatoir |
| Intrekking vergunning | 18.10 | Reparatoir |
| Bestuurlijke boete | 18.11-18.15a | Punitief |
| Voorleggen aan OM | 18.16 | Escalatie |

**Boetecategorieën (Sr art. 23)**:

| Categorie | Domein | Artikel |
|-----------|--------|---------|
| 6 | Seveso (+ 10% omzet) | 18.11 |
| 5 | Erfgoed, luchthaven | 18.13, 18.14 |
| 4 | Bouw bij bedreiging | 18.12 lid 3 |
| 2 | Bouw standaard | 18.12 lid 2 |

**Art. 18.10 lid 3 - Herstelmogelijkheid eerst**:
- VOORWAARDE voor intrekking: eerst kans tot herstel bieden
- Uitzondering: valse gegevens of verkeerde persoon

### Afdeling 18.3 - Omgevingsdiensten

**Verplichte regionale samenwerking (Art. 18.21)**:

| Aspect | Regel |
|--------|-------|
| Instelling | GS + B&W gezamenlijk |
| Rechtsvorm | Openbaar lichaam (Wgr) |
| Werkgebied | Veiligheidsregio |
| Specialisatie | RIE-cat.4, Seveso |

**Kwaliteitsborging (Art. 18.24)**:
- Tweejaarlijks doeltreffendheidsonderzoek
- Bij falen: Rijk kan AMvB-regels stellen

### Cross-Chapter Connections (Ch18)

```
Ch18 ←→ Ch4: 18.2 lid 1 → 4.1.3 (BG regels)
Ch18 ←→ Ch5: 18.2 lid 2 → 5.1.2 (BG vergunning)
Ch18 ←→ Ch5: 18.10 → 5.40 (intrekking)
Ch18 ←→ Ch16: 18.3 → 16.16 (instemmer = mede-handhaver)
Ch18 ←→ Ch2: 18.2 lid 6 → 2.3 (subsidiariteitsgrens)
```

---

## Module Status Summary (Updated with Ch18)

| Module | Status | Key Patterns Discovered |
|--------|--------|------------------------|
| ch5-par5.1.1-atomic.yaml | ✅ Complete | verbod + tenzij/voor zover |
| ch5-par5.1.2-atomic.yaml | ✅ Complete | default + tenzij decision tree |
| ch5-par5.1.3-atomic.yaml | ✅ Complete | hub-and-spoke (5.18 → 5.20-5.29a) |
| ch5-par5.1.4-5.1.5-v2-atomic.yaml | ✅ Complete V2 | imperatief vs facultatief, lifecycle pattern |
| ch5-afd5.2-v2-atomic.yaml | ✅ Complete V2 | projectbesluit = integraal, hiërarchie, doorbreking |
| ch4-afd4.1-atomic.yaml | ✅ Complete | 4.3 hub, 4.9 default+tenzij |
| ch4-afd4.2-4.3-v2-atomic.yaml | ✅ Complete V2 | Ch4 ↔ Ch5 parallel, hub-and-spoke 4.3, voorbescherming |
| ch16-afd16.1-v2-atomic.yaml | ✅ Complete V2 | houdbaarheid data, DSO |
| ch16-afd16.2-v2-atomic.yaml | ✅ Complete V2 | advies vs instemming, reactieve interventie, Awb 3.5 coördinatie |
| ch16-afd16.3-v2-atomic.yaml | ✅ Complete V2 | UOV-standaard, actio popularis, rechterlijke bekrachtiging |
| ch16-afd16.4-v2-atomic.yaml | ✅ Complete V2 | dual-track MER, tiering, Commissie asymmetrie |
| ch16-afd16.4a-v2-atomic.yaml | ✅ Complete V2 | passende beoordeling, Habitatrichtlijn art. 6 lid 3 |
| ch16-afd16.5-v2-atomic.yaml | ✅ Complete V2 | procedure duality, loket, lex silencio, termijn_structure |
| ch16-afd16.6-16.6a-v2-atomic.yaml | ✅ Complete V2 | projectprocedure UOV, waterschap GS-goedkeuring, kostenverhaal aanhouding |
| ch16-afd16.7-v2-atomic.yaml | ✅ Complete V2 | inwerkingtreding spectrum, uitgestelde inwerkingtreding, beroepsbundeling |
| ch16-afd16.8-16.14-v2-atomic.yaml | ✅ Complete V2 | rechterlijke bekrachtiging onteigening, landinrichting, delegatiegrondslag |
| ch2-afd2.1-atomic.yaml | ✅ Complete | subsidiariteit, doelgebondenheid, 19 belangen |
| ch2-afd2.2-atomic.yaml | ✅ Complete | one-plan-principle, exclusiviteit |
| ch2-afd2.3-atomic.yaml | ✅ Complete | omgevingswaarden, resultaat vs inspanning, stikstof |
| ch2-afd2.4-atomic.yaml | ✅ Complete | taaktoedeling per niveau, beperkingengebieden |
| ch2-afd2.5-atomic.yaml | ✅ Complete | instructieregels vs instructies, indeplaatstreding |
| ch2-afd2.6-atomic.yaml | ✅ Complete | water, natuur, stikstofdepositieruimte |
| **ch18-atomic.yaml** | ✅ Complete | wie verleent=handhaaft, omgevingsdiensten, boetecategorieën |
| **ch3-v2-atomic.yaml** | ✅ Complete V2 | visie vs programma, programmatische aanpak, EU-doorwerking |

### CHAPTER 18 COMPLETE

All 3 afdelingen of Chapter 18 (Handhaving) have been extracted:

| Afdeling | Articles | Module | Key Patterns |
|----------|----------|--------|--------------|
| 18.1 | 18.1-18.16b | ch18-atomic | wie verleent = wie handhaaft |
| 18.2 | 18.17 | ch18-atomic | EEZ-rechtsmacht |
| 18.3 | 18.18-18.27 | ch18-atomic | omgevingsdiensten |

### System Pattern Confirmed: DEFAULT + TENZIJ Cascade

The extraction of Ch2, Ch4, Ch5, Ch16, and Ch18 confirms a **STRUCTURAL PATTERN** across the entire Omgevingswet:

| Chapter | Article | Default | Exceptions |
|---------|---------|---------|------------|
| Ch2 | 2.3 | Gemeente | Provincie/Rijk "tenzij" |
| Ch4 | 4.9 | Gemeente (B&W) | 4.10, 4.11, 4.12, 4.13 |
| Ch5 | 5.8 | Gemeente (B&W) | 5.9, 5.10, 5.11, 5.13 |
| Ch16 | 16.62 | Reguliere procedure | 16.5.3 (uitgebreid) |
| Ch18 | 18.2 | B&W | AMvB kan afwijken (lid 6) |

**Navigation implication**: Always start at default, check for explicit exceptions.

---

## AFDELING 5.2 V2 - PROJECTPROCEDURE (Extraction 2026-01-29)

### Structure Overview

| Paragraaf | Articles | Function | Key Pattern |
|-----------|----------|----------|-------------|
| **5.2.1** | 5.44-5.46 | Algemene bepalingen | Bevoegdheid hiërarchie, verplichte projecten |
| **5.2.2** | 5.47-5.50 | Voornemen, verkenning, voorkeursbeslissing | Procedurefasen |
| **5.2.3** | 5.51-5.54 | Projectbesluit | Integraal besluit, doorbreking |
| **5.2.4** | 5.55 | Gemeentelijke projecten | Via omgevingsplan route |

### Key Discovery: Bevoegdheid Hiërarchie (Art. 5.44-5.44b)

```
Projectbesluit bevoegdheid:
├── Waterschap: ALLEEN watertaken (art. 2.17)
├── GS: provinciaal belang (subsidiariteitstoets art. 2.3)
└── Minister: nationaal belang (+ BZK overeenstemming)
    │
    └── BZK overeenstemming NIET vereist voor:
        ├── Uitwerking (art. 5.54)
        ├── Wijziging
        └── Aangewezen categorieën (ministeriële regeling)

VOORRANGSREGELS (art. 5.44a):
├── Bij conflict: "hoofdlocatie" bepaalt
├── GS + waterschap → GS wint
└── Rijk + GS/waterschap → Rijk wint
```

**CRITICAL**: Gemeente kan GEEN projectbesluit nemen - alleen omgevingsplanroute (art. 5.55)

### Verplichte Projectbesluiten (Art. 5.46)

| Categorie | Bevoegd gezag | Voorbeelden |
|-----------|---------------|-------------|
| Hoofdinfrastructuur | Minister I&W | Autowegen, spoorwegen, vaarwegen |
| Primaire waterkeringen (Rijk) | Minister I&W | Rijkswaterkeringen |
| Primaire waterkeringen (overig) | Waterschap | Waterschapskeringen |

### Procedurele Fasen (§ 5.2.2)

```
Art. 5.47 VOORNEMEN
    │   └── Participatie: iedereen mag oplossingen voordragen
    ▼
Art. 5.48 VERKENNING
    │   └── Second opinion recht via onafhankelijke deskundige
    ▼
Art. 5.49 VOORKEURSBESLISSING (optioneel)
    │   └── Uitkomsten: project / geen project / combinatie / niets
    ▼
Art. 5.51-5.54 PROJECTBESLUIT
        └── Integraal besluit

SNELROUTE (art. 5.50):
├── Uitwerking projectbesluit → skip fasen 1-3
└── Wijziging projectbesluit → skip fasen 1-3
```

### INTEGRAAL BESLUIT Pattern (Art. 5.52)

**Het projectbesluit combineert meerdere functies in één besluit:**

| Lid | Functie | Karakter |
|-----|---------|----------|
| 1 | Wijzigt omgevingsplan | ALTIJD |
| 2a | Geldt als omgevingsvergunning | INDIEN BEPAALD |
| 2b | Geldt als ander aangewezen besluit | VIA AMvB |

**Implicatie**: één besluit, één procedure, één rechtsbescherming

### DOORBREKING Mechanismen (Art. 5.53, 5.53a)

```
DOORBREKING LAGER NIVEAU (art. 5.53 lid 3-4):
├── GS kan opzij zetten:
│   ├── Gemeente regels (behalve omgevingsplan)
│   └── Waterschap regels
└── Minister kan opzij zetten:
    ├── Gemeente regels
    ├── Provincie regels
    └── Waterschap regels

VOORWAARDE: "onevenredige belemmering" + "dringende redenen"

BESCHERMING HOGER NIVEAU (art. 5.53a):
├── Waterschap mag Rijksprojectbesluit niet belemmeren
└── GS mag Rijksprojectbesluit niet belemmeren
    │
    UITZONDERING: als instructieregel/instructie het vergt
```

### INDEPLAATSTREDING (Art. 5.45a)

**Sterkste coördinatie-instrument:**

| Coördinator | Kan vervangen | Triggers |
|-------------|---------------|----------|
| GS | Alle behalve Rijk | Niet-tijdig / belemmerend besluit |
| Minister | ALLE organen | Niet-tijdig / belemmerend besluit |

**Sterker dan instructie (art. 2.34)**: directe vervanging, geen opdracht

### Gemeentelijke Route (Art. 5.55)

```
Gemeente kan GEEN projectbesluit, MAAR:
    │
    └── Omgevingsplanwijziging met:
        ├── Overeenkomstige toepassing art. 5.45, 5.47-5.49, 5.51
        └── Art. 16.87 (beroep in één instantie) wordt van toepassing

VOORDEEL: versnelde rechtsbescherming bij grote gemeentelijke projecten
```

### Cross-Chapter Connections (Afd 5.2)

```
Afd 5.2 ←→ Ch2: 5.44 lid 3 → 2.3 (subsidiariteitstoets)
Afd 5.2 ←→ Ch4: 5.53 lid 1 → 4.1, 4.2, §4.1.2, §4.3.1 (beoordelingsregels plan)
Afd 5.2 ←→ Afd 5.1: 5.53 lid 2 → §5.1.3-5.1.5 (beoordelingsregels vergunning)
Afd 5.2 ←→ Ch16: 5.45 → 16.7 (coördinatieregeling)
Afd 5.2 ←→ Ch16: 5.55 → 16.87 (beroep in één instantie)
Afd 5.2 ←→ Afd 2.5: 5.53a → 2.24, 2.34 (instructies kunnen doorwerken)
```

---

## CHAPTER 3 - OMGEVINGSVISIES EN PROGRAMMA'S (Extraction 2026-01-29)

### Structure Overview

| Afdeling | Articles | Function | Key Pattern |
|----------|----------|----------|-------------|
| **3.1** | 3.1-3.3 | Omgevingsvisies | Verplicht strategisch instrument |
| **3.2** | 3.4-3.19 | Programma's | Uitvoeringsgerichte maatregelen |

### Afdeling 3.1 - Omgevingsvisies

**Verplicht op elk niveau (Art. 3.1)**:

| Niveau | Bevoegd gezag | Type |
|--------|---------------|------|
| Gemeente | Gemeenteraad | Verplicht |
| Provincie | Provinciale staten | Verplicht |
| Rijk | Minister BZK | Verplicht |

**Inhoud (Art. 3.2)**: Hoofdlijnen kwaliteit + ontwikkelingsrichting + integraal beleid

**EU-beginselen (Art. 3.3)**: Voorzorg, preventief, bron, vervuiler betaalt

### Afdeling 3.2 - Programma's

**Verplichte programma's matrix**:

| Niveau | Instrument | Artikel | EU-grondslag |
|--------|------------|---------|--------------|
| Gemeente | Actieplan geluid (agglomeratie) | 3.6 | Richtlijn omgevingslawaai |
| Waterschap | Waterbeheerprogramma | 3.7 | - |
| Provincie | Actieplan geluid (buiten agglo) | 3.8.1 | Richtlijn omgevingslawaai |
| Provincie | Regionaal waterprogramma | 3.8.2 | KRW, ROR, zwemwater |
| Provincie | Beheerplan N2000 | 3.8.3 | Habitatrichtlijn |
| Rijk | NEC-programma | 3.9.1a | NEC-richtlijn |
| Rijk | Actieplan geluid (rijksinfra) | 3.9.1b | Richtlijn omgevingslawaai |
| Rijk | Stroomgebiedsbeheerplannen | 3.9.2a | KRW |
| Rijk | Overstromingsrisicobeheerplannen | 3.9.2b | ROR |
| Rijk | Maatregelprogramma mariene strategie | 3.9.2c | KRMS |
| Rijk | Maritiem ruimtelijk plan | 3.9.2d | KMRP |
| Rijk | Nationaal waterprogramma | 3.9.2e | - |
| **Rijk** | **Stikstofprogramma** | **3.9.4** | **Habitatrichtlijn** |

**Critical: Art. 3.9 lid 4 = stikstofprogramma**
- Verminderen depositie op N2000-habitats
- Voldoen aan art. 2.15a omgevingswaarden (40%/50%/74%)
- Bereiken instandhoudingsdoelstellingen

**Art. 3.10 - Reactief programma**:
- Bij (dreigende) overschrijding omgevingswaarde → B&W stelt programma vast
- DEFAULT gemeente, TENZIJ water (waterschap/Rijk)

### §3.2.4 - Programmatische aanpak

**Kernprincipe: saldering via programma (Art. 3.16)**:

```
Omgevingswaarde stelt limiet
        ↓
Programma definieert beschikbare ruimte
        ↓
Maatregelen compenseren effecten activiteiten
        ↓
Beoordelingsregels (5.18 etc.) wijken voor programma
```

**Uitvoeringsplicht (Art. 3.18)**: Alleen met instemming of via instructieregel

**Wijziging (Art. 3.19)**: Toegestaan mits saldo-neutraal

### Cross-Chapter Connections (Ch3)

```
Ch3 ←→ Ch2: 3.2 → 2.1 (doelgebondenheid)
Ch3 ←→ Ch2: 3.9.4 → 2.15a (stikstofomgevingswaarden)
Ch3 ←→ Ch5: 3.16 → 5.18 (beoordelingsregels wijken)
Ch3 ←→ Ch16: 3.* → 16.26-16.27 (procedure)
Ch3 ←→ Ch20: 3.11 → 20.1 (monitoring → wijziging)
```

---

## Module Status Summary (Updated with Ch3)

| Module | Status | Key Patterns Discovered |
|--------|--------|------------------------|
| ch5-par5.1.1-atomic.yaml | ✅ Complete | verbod + tenzij/voor zover |
| ch5-par5.1.2-atomic.yaml | ✅ Complete | default + tenzij decision tree |
| ch5-par5.1.3-atomic.yaml | ✅ Complete | hub-and-spoke (5.18 → 5.20-5.29a) |
| ch5-par5.1.4-5.1.5-v2-atomic.yaml | ✅ Complete V2 | imperatief vs facultatief, lifecycle pattern |
| ch5-afd5.2-v2-atomic.yaml | ✅ Complete V2 | projectbesluit = integraal, hiërarchie, doorbreking |
| ch4-afd4.1-atomic.yaml | ✅ Complete | 4.3 hub, 4.9 default+tenzij |
| ch4-afd4.2-4.3-v2-atomic.yaml | ✅ Complete V2 | Ch4 ↔ Ch5 parallel, hub-and-spoke 4.3, voorbescherming |
| ch16-afd16.1-atomic.yaml | ✅ Complete | houdbaarheid data, DSO |
| ch16-afd16.2-atomic.yaml | ✅ Complete | advies vs instemming, reactieve interventie |
| ch16-afd16.3-atomic.yaml | ✅ Complete | UOV-standaard, actio popularis |
| ch16-afd16.4-atomic.yaml | ✅ Complete | dual-track MER, tiering, Commissie asymmetrie |
| ch16-afd16.4a-atomic.yaml | ✅ Complete | passende beoordeling, Habitatrichtlijn |
| ch16-afd16.5-v2-atomic.yaml | ✅ Complete V2 | procedure duality, loket, lex silencio, termijn_structure |
| ch16-afd16.6-16.6a-atomic.yaml | ✅ Complete | projectprocedure, kostenverhaal |
| ch16-afd16.7-atomic.yaml | ✅ Complete | inwerkingtreding spectrum |
| ch16-afd16.8-16.14-atomic.yaml | ✅ Complete | domain-specific |
| ch2-afd2.1-atomic.yaml | ✅ Complete | subsidiariteit, doelgebondenheid |
| ch2-afd2.2-atomic.yaml | ✅ Complete | one-plan-principle |
| ch2-afd2.3-atomic.yaml | ✅ Complete | omgevingswaarden, stikstof |
| ch2-afd2.4-atomic.yaml | ✅ Complete | taaktoedeling |
| ch2-afd2.5-atomic.yaml | ✅ Complete | instructieregels |
| ch2-afd2.6-atomic.yaml | ✅ Complete | water, natuur, stikstofdepositieruimte |
| ch18-atomic.yaml | ✅ Complete | wie verleent=handhaaft, omgevingsdiensten |
| **ch3-v2-atomic.yaml** | ✅ Complete V2 | omgevingsvisie, programma's, programmatische aanpak, EU-doorwerking |
| **ch5-par5.1.1-v2-atomic.yaml** | ✅ V2 | TENZIJ vs VOOR ZOVER, lid-level logica, handhavingshiërarchie |
| **ch5-par5.1.2-v2-atomic.yaml** | ✅ V2 | subsidiariteitstrap, noodbevoegdheid, beslisboom |
| **ch5-par5.1.3-v2-atomic.yaml** | ✅ V2 | hub-spoke beoordelingsregels, beschermde_belangen |
| **ch4-afd4.1-v2-atomic.yaml** | ✅ V2 | 4.3 hub, 4.9 default+tenzij, Ch4↔Ch5 parallel, maatwerk-hiërarchie |
| **ch16-par16.5-v2-atomic.yaml** | ✅ V2 | loketfunctie, default+tenzij procedure, lex silencio exclusie, termijnen |

### CHAPTER 3 COMPLETE

All 2 afdelingen of Chapter 3 (Strategische instrumenten) have been extracted:

| Afdeling | Articles | Module | Key Patterns |
|----------|----------|--------|--------------|
| 3.1 | 3.1-3.3 | ch3-v2-atomic | omgevingsvisie verplicht op elk niveau |
| 3.2 | 3.4-3.19 | ch3-v2-atomic | verplichte/onverplichte programma's, programmatische aanpak |

### Stikstof-Complex Complete

With Ch2 and Ch3 extracted, the stikstof-complex is now fully mapped:

```
Art. 2.15a (omgevingswaarden: 40%/50%/74%)
        ↓
Art. 3.9 lid 4 (stikstofprogramma)
        ↓
Art. 2.46 (stikstofdepositieruimte register)
        ↓
Art. 16.53c (passende beoordeling)
```

---

## CHAPTER 1 - ALGEMENE BEPALINGEN V2 (Extraction 2026-01-29)

### Structure Overview

| Afdeling | Articles | Function | Key Pattern |
|----------|----------|----------|-------------|
| **1.1** | 1.1 | Begripsbepalingen | Bijlage-systematiek, AMvB-doorwerking |
| **1.2** | 1.2-1.5 | Toepassingsgebied en doelen | 10 componenten, duale doelstelling, EEZ-scope |
| **1.3** | 1.6-1.8 | Zorg fysieke leefomgeving | Zorgplicht-hiërarchie met 3 niveaus |

### Art. 1.2 - Fysieke leefomgeving (10 componenten - NIET LIMITATIEF)

```
"in ieder geval" = open lijst - rechter kan uitbreiden

bouwwerken | infrastructuur | watersystemen | water | bodem
lucht | landschappen | natuur | cultureel erfgoed | werelderfgoed
```

**Lid 3 - Gevolgen** (ook NIET limitatief):
- Wijzigen onderdelen/gebruik
- Gebruik natuurlijke hulpbronnen
- Emissies, hinder, risico's
- **Nalaten** (ook inactiviteit is "activiteit"!)

**Lid 4 - Menselijke gevolgen**:
- Alleen INDIRECT via fysieke leefomgeving
- Geen directe gezondheidsregulering

### Art. 1.3 - Duale doelstelling (GELIJKWAARDIG)

| Pool | Elementen | Karakter |
|------|-----------|----------|
| **a. BESCHERMEN** | veilig, gezond, omgevingskwaliteit, intrinsieke waarde natuur | Ecocentrisch |
| **b. BENUTTEN** | doelmatig beheren/gebruiken/ontwikkelen, maatschappelijke behoeften | Antropocentrisch |

**"In onderlinge samenhang"** = beide doelen moeten worden afgewogen, geen wettelijke hiërarchie

Kaderdoelen (GW art. 21): duurzame ontwikkeling, bewoonbaarheid, leefmilieu

### Art. 1.4 - Lex Specialis

```
Omgevingswet NIET van toepassing als:
├── Ander wet regelt uitputtend
└── TENZIJ Omgevingswet expliciet anders bepaalt

Voorbeelden andere wetten: Mijnbouwwet, Kernenergiewet
```

### Art. 1.5 - Geografische Scope

| Gebied | Toepassing | Uitzonderingen |
|--------|------------|----------------|
| Nederland | Volledig | - |
| EEZ | Ja | Art. 5.1 lid 1a/b, lid 2a (bouw/omgevingsplan) |
| Buiten EEZ | Extraterritoriaal | Alleen stortingsactiviteiten + walvisregels |

### Zorgplicht-hiërarchie (Afd 1.3) - V2 DIEPTE

| Niveau | Artikel | Norm | Proportionaliteit | Handhaving |
|--------|---------|------|-------------------|------------|
| **ABSTRACT** | 1.6 | "voldoende zorg" | - | Niet direct |
| **CONCREET** | 1.7 | voorkomen → beperken → stoppen | "redelijkerwijs" | Bestuursrecht |
| **ABSOLUUT** | 1.7a | verbod aanzienlijke gevolgen | Geen | **Strafrecht** |

**Art. 1.7 - Drietraps-cascade**:
```
TRAP 1 (a): VOORKOMEN
    ↓ (kan niet)
TRAP 2 (b): BEPERKEN of ongedaan maken
    ↓ (onvoldoende)
TRAP 3 (c): STOPPEN (activiteit achterwege laten)

Trigger: "weet of redelijkerwijs kan vermoeden"
         → objectieve kenbaarheidsnorm
```

**Art. 1.7a - EU Richtlijn Milieustrafrecht**:
- NIEUW per 2024
- Absoluut verbod - geen proportionaliteitstoets
- AMvB definieert "aanzienlijk" + "gevallen"

**Art. 1.8 - Safe Harbour Mechanisme**:

| Lid | Situatie | Vereiste | Effect |
|-----|----------|----------|--------|
| 1 | Art. 1.6/1.7 | Specifieke regels + NALEVING | Voldaan aan zorgplicht |
| 2 | Art. 1.7a | Specifieke regels (geen naleving nodig) | Art. 1.7a niet van toepassing |

**KRITISCH verschil**: Lid 1 = compliance defence, Lid 2 = regulatory defence

### Cross-Chapter Connections (Ch1)

```
Ch1 ←→ Bijlage: 1.1 → begripsbepalingen
Ch1 ←→ Ch5: 1.5 → 5.1 (EEZ-uitzonderingen)
Ch1 ←→ Ch2: 1.3 → 2.1 (doelgebondenheid bestuursorganen)
Ch1 ←→ Ch18: 1.7a → 18.* (strafrechtelijke handhaving)
```

---

## Module Status (Updated with Ch1 V2)

| Module | Status |
|--------|--------|
| **ch1-v2-atomic.yaml** | ✅ Complete V2 |
| ch2-afd2.1-2.6-atomic.yaml (6 files) | ✅ Complete |
| ch3-atomic.yaml | ✅ Complete |
| ch4-afd4.1-4.3-atomic.yaml (2 files) | ✅ Complete |
| ch5-*.yaml (5 files) | ✅ Complete |
| ch16-*.yaml (8 files) | ✅ Complete |
| ch18-atomic.yaml | ✅ Complete |

### Core System Architecture Complete

```
Ch1 (Foundations) → Ch2 (Governance) → Ch3 (Strategic)
                         ↓
              Ch4 (Rules) ↔ Ch5 (Permits)
                         ↓
                   Ch16 (Procedures)
                         ↓
                   Ch18 (Enforcement)
```

---

## CHAPTER 19 - BIJZONDERE OMSTANDIGHEDEN (Extraction 2026-01-29)

### Structure Overview

| Afdeling | Articles | Function | Key Pattern |
|----------|----------|----------|-------------|
| **19.0** | 19.0 | Toepassingsbereik | definities voor heel hoofdstuk |
| **19.1** | 19.1-19.7 | Ongewoon voorval | meldplicht → maatregelen → kostenverhaal |
| **19.2** | 19.8-19.9 | Archeologische toevalsvondst | meldplicht RCE, beperkte opgravingsbevoegdheid |
| **19.2a** | 19.9a-19.9d | Toevalsvondst bodemverontreiniging | vergelijkbaar met ongewoon voorval |
| **19.3** | 19.10-19.12 | Alarmeringswaarden | parallel aan omgevingswaarden, gedragsvoorschriften |
| **19.4** | 19.13-19.16 | Gevaar waterstaatswerken | **vergaande noodbevoegdheid** |
| **19.5** | 19.17-19.19 | Buitengewone omstandigheden | staatsnoodrecht |

### Emergency Powers Hierarchy

| Situatie | Trigger | Bevoegdheid | Grenzen |
|----------|---------|-------------|---------|
| Ongewoon voorval | milieu-incident | herstelmaatregelen + kosten | normale wetgeving |
| Alarmeringswaarden | drempeloverschrijding | gedragsvoorschriften | programma-verplichting |
| Waterstaatsgevaar | dijkdoorbraak dreigt | **afwijken van alle wettelijke voorschriften** | Grondwet + internationaal |
| Buitengewone omstandigheden | staatsnood | coördinatiewet actief | KB-activering |

### Art. 19.15 - Vergaande noodbevoegdheid

**Critical discovery**: De beheerder mag bij dijkgevaar afwijken van ALLE wettelijke voorschriften in dit hoofdstuk én de Waterwet, uitgezonderd:
- Grondwet
- Internationaal recht

Dit is de meest vergaande bevoegdheid in de hele Omgevingswet.

### Cross-Chapter Links

| Link | Richting | Purpose |
|------|----------|---------|
| 19.1 → 18.1 | forward | kostenverhaal via handhavingsladder |
| 19.3 ↔ 2.15 | bidirectional | alarmeringswaarden parallel aan omgevingswaarden |
| 19.4 → Waterwet | external | noodbevoegdheden voor waterstaatswerken |
| 19.5 → Coördinatiewet | external | staatsnoodrecht-activering |

---

---

## CHAPTER 20 - MONITORING EN INFORMATIE (Extraction 2026-01-29)

### Structure Overview

| Afdeling | Articles | Function | Key Pattern |
|----------|----------|----------|-------------|
| **20.1** | 20.1-20.7a | Monitoring en verzameling | monitoringsplicht gekoppeld aan waarden |
| **20.2** | 20.8-20.13 | Gegevensbeheer | registers, publieksinformatie |
| **20.3** | 20.14-20.17 | Verslagen en kaarten | rapportage-verplichtingen |
| **20.4** | 20.18-20.19 | Evaluatie | PBL 4-jaarlijks, waterkeringen 12-jaarlijks |
| **20.5** | 20.20-20.30 | DSO | digitaal stelsel met 6 paragrafen |

### Art. 20.20 - DSO Drievoudig Doel

| Doel | Omschrijving |
|------|-------------|
| **a. Informatie** | beschikbaar stellen over fysieke leefomgeving |
| **b. Loketfunctie** | faciliteren elektronisch verkeer (Art. 16.1) |
| **c. Doelmatigheid** | bevorderen doeltreffende taakuitoefening |

### Art. 20.4 - EU-Implementatie (12 richtlijnen)

drinkwater | grondwater | habitat | kaderrichtlijn water | NEC | gevaarlijke stoffen lucht | luchtkwaliteit | prioritaire stoffen | stedelijk afvalwater | energie-unie | vogel | zwemwater

### Verplichte Registers (Art. 20.11)

| Register | Inhoud |
|----------|--------|
| **PRTR** | uitstoot en overbrenging verontreinigende stoffen |
| **Externe veiligheid** | installaties, transportroutes, buisleidingen |
| **Beschermde gebieden** | Art. 6 kaderrichtlijn water |

### Feedback Loop Pattern

```
Ch2/Ch3 (doelen stellen)
        ↓
    Ch20 (meten)
        ↓
    ┌───┴───┐
    ↓       ↓
Ch3 (bijsturen)  Ch19 (noodmaatregelen)
```

---

## Module Status (Updated with Ch20)

| Module | Status |
|--------|--------|
| **ch1-v2-atomic.yaml** | ✅ Complete V2 |
| ch2-afd2.1-2.6-atomic.yaml (6 files) | ✅ Complete |
| ch3-v2-atomic.yaml | ✅ Complete V2 |
| ch4-afd4.1-4.3-atomic.yaml (2 files) | ✅ Complete |
| ch5-*.yaml (5 files) | ✅ Complete |
| ch16-*.yaml (8 files) | ✅ Complete |
| ch18-atomic.yaml | ✅ Complete |
| ch19-atomic.yaml | ✅ Complete |
| ch20-atomic.yaml | ✅ Complete |
| **ch22-ch23-atomic.yaml** | ✅ Complete |
| **ch9-v2-atomic.yaml** | ✅ Complete V2 |
| **ch10-v2-atomic.yaml** | ✅ Complete V2 |

---

## CHAPTER 10 - GEDOOGPLICHTEN V2 (Extraction 2026-01-29)

### Structure Overview

| Afdeling | Articles | Function | Key Pattern |
|----------|----------|----------|-------------|
| **10.1** | 10.1-10.1a | Algemene bepalingen | Begrippen, toegangsrecht |
| **10.2** | 10.2-10.10j | Van rechtswege | Automatisch - geen beschikking |
| **10.3** | 10.11-10.28 | Bij beschikking | Vier cumulatieve criteria |
| **10.4** | 10.29 | Overig | Populatiebeheer |

### Tweesporig Systeem

```
GEDOOGPLICHTEN:
├── VAN RECHTSWEGE (Afd 10.2)
│   └── Automatisch - geen besluit nodig
│       ├── wegen/waterstaatswerken (10.2)
│       ├── waterbeheer (10.3)
│       ├── mijnbouw > 100m (10.9)
│       ├── landinrichting (10.10c-10.10g)
│       └── waterstoftransport (10.10i)
│
└── BIJ BESCHIKKING (Afd 10.3)
    └── Besluit vereist - art. 10.11 criteria
        ├── infrastructuur/water (10.13)
        ├── energie/mijnbouw (10.14)
        ├── waterstaatswerken (10.17)
        └── vangnet (10.21)
```

### Art. 10.11 - Vier Cumulatieve Criteria

| Criterium | Inhoud |
|-----------|--------|
| **a. Noodzaak** | Gebruik onroerende zaak vereist |
| **b. Onderhandeling** | Redelijke poging gefaald |
| **c. Proportionaliteit** | Minimale belemmering |
| **d. Subsidiariteit** | Onteigening niet gerechtvaardigd |

**KRITISCH**: Alle vier cumulatief vereist. Als belangen onteigening vorderen → Ch11, niet Ch10.

### Bevoegdheidsverdeling

| Bevoegd gezag | Werken |
|---------------|--------|
| **Minister I&W** | Spoor, drinkwater, energie, mijnbouw, vangnet |
| **Minister OCW** | Archeologie |
| **Minister Defensie** | Defensiewerken |
| **Waterschap** | Waterstaatswerken |
| **B&W** | Bodem, stortplaatsen |
| **GS** | Ontgrondingen provinciaal |

### Informatieplicht Termijnen

| Termijn | Situatie |
|---------|----------|
| **48 uur** | Wegen/water (10.4), populatiebeheer (10.29) |
| **4 weken** | N2000 maatregelen (10.10b) |
| **4 dagen** | Ontwerpvoorbereiding (10.10j) |
| **Geen** | Spoedeisend |

### Key Discovery: Lichter dan Onteigening

```
Belangen rechthebbende:
├── Vorderen NIET onteigening → GEDOOGPLICHT (Ch10)
│   └── Dulden gebruik, eigendom blijft
│
└── Vorderen WEL onteigening → ONTEIGENING (Ch11)
    └── Eigendomsovergang
```

### Cross-Chapter Connections

```
Ch10 ←→ Ch5: 10.13 → 5.46 (projectbesluit als grondslag)
Ch10 ←→ Ch11: 10.11d → onteigening als zwaardere optie
Ch10 ←→ Ch15: gedoogplicht → schadevergoeding
Ch10 ←→ Ch16: procedure gedoogplichtbeschikking
```

---

## CHAPTER 9 - VOORKEURSRECHT V2 (Extraction 2026-01-29)

### Structure Overview

| Afdeling | Articles | Function | Key Pattern |
|----------|----------|----------|-------------|
| **9.1** | 9.1-9.5 | Vestiging en gelding | Drie-niveau hiërarchie, grondslag-afhankelijke duur |
| **9.2** | 9.6-9.22 | Vervreemding na vestiging | Aanbiedingsplicht, uitzonderingen, procedure |

### Bevoegdheid Hiërarchie

```
VESTIGING:                    UITVOERING:
├── Gemeente: gemeenteraad    ├── Gemeente: B&W
├── Provincie: PS             ├── Provincie: GS
└── Rijk: Minister BZK        └── Rijk: Minister BZK

EXCLUSIVITEIT (art. 9.2):
Rijk > Provincie > Gemeente
- Hoger niveau blokkeert lager
- Hoger niveau doet lager vervallen
```

### Grondslag-Geldingsduur Matrix

| Grondslag | Basis | Maximum | Upgrade |
|-----------|-------|---------|---------|
| **c. Beschikking** | 3 jaar | 3 jaar | → b of a |
| **b. Visie/programma** | 3 jaar | 3 jaar | → a |
| **a. Omgevingsplan** | 5 jaar | 10 jaar | +5 verlenging |
| **Voorlopig (lid 2)** | 3 maanden | 3 maanden | → definitief |

### Procedure bij Vervreemding

```
Art. 9.7: AANBIEDINGSPLICHT (hoofdregel)
        ↓
Art. 9.12: Uitnodiging tot onderhandeling
        ↓
Art. 9.13: BG beslist binnen 6 weken
        ↓
    ┌───┴───┐
    ↓       ↓
BEREID   NIET BEREID / TERMIJN
    ↓           ↓
Onderhandeling  Vrije vervreemding 3 jaar
    ↓           (of verval bij 5+ jaar plan)
Art. 9.16: Prijsprocedure rechtbank
```

### Uitzonderingen op Aanbiedingsplicht (art. 9.8)

| Type | Situatie |
|------|----------|
| Familie | Echtgenoot, partner, bloed-/aanverwanten tot 2e graad, pleegkind |
| Erfrecht | Boedelverdeling, testament |
| Overheid | Verkoop aan gemeente/provincie/Staat/aangewezen rechtspersoon |
| Gedwongen | Executie, rechterlijk bevel |
| Pachter | Bestaand voorkeursrecht pachter |
| Contract | Ingeschreven overeenkomst van voor beschikking |
| Hardheid | Gewichtige redenen (art. 9.10) |

### Eigenaarsbescherming

| Recht | Artikel | Situatie |
|-------|---------|----------|
| **Prijsvaststelling** | 9.16 | Impasse in onderhandeling → rechtbank |
| **Gedwongen koop** | 9.18 | Persoonlijke omstandigheden → overheid moet kopen |
| **Vrije vervreemding** | 9.14, 9.17 | Na weigering/termijnoverschrijding → 3 jaar vrij |

### Anti-Ontwijking

| Mechanisme | Artikel | Werking |
|------------|---------|---------|
| **Nietigheid** | 9.22 | Frauduleuze transacties kunnen nietig worden verklaard |
| **Notaris poortwachter** | 9.21 | Verklaring vereist voor inschrijving kadaster |
| **Cooldown** | 9.3 | 2 jaar wachttijd na verval voor hervestiging |

### Cross-Chapter Connections

```
Ch9 ←→ Ch16: 9.3 → 16.82a (inschrijvingstermijn)
Ch9 ←→ Ch16: 9.20 → 16.123 (prijsvaststelling)
Ch9 ←→ Ch2: 9.1 → omgevingsplan/visie (grondslag)
Ch9 ←→ Ch3: 9.1 → programma (grondslag)
```

---

## CHAPTERS 22-23 - OVERGANGSRECHT EN SLOTBEPALINGEN (Extraction 2026-01-29)

### Chapter 22 - Overgangsrecht

| Afdeling | Articles | Function | Key Pattern |
|----------|----------|----------|-------------|
| **22.1** | 22.1-22.17 | Overgangsfase | tijdelijk deel omgevingsplan |
| **22.2** | 22.18-22.19 | Sanering geluid | deadline 18 juli 2039 |
| **22.4** | 22.21-22.22 | Legalisering natuur | PAS-projecten |

### Chapter 23 - Overige en slotbepalingen

| Afdeling | Articles | Function | Key Pattern |
|----------|----------|----------|-------------|
| **23.1** | 23.1-23.2 | Implementatie internationaal | vangnet + automatische doorwerking |
| **23.2** | 23.3 | Experimenteerbepaling | afwijken van de wet zelf |
| **23.3** | 23.4-23.8 | Participatie en totstandkoming | voorhang, beginselen |
| **23.4** | 23.9-23.11 | Evaluatie en slot | 5-jaarlijkse evaluatie |

### Key Discoveries

**Art. 22.21 - PAS Legalisatie**: Wettelijke basis voor legalisatie van projecten die onder PAS legaal waren maar na 29 mei 2019 illegaal werden. Programma met maatregelen binnen 3 jaar.

**Art. 23.3 - Experimenteerbepaling**: Bij AMvB kan worden afgeweken van de Omgevingswet ZELF, maar alleen voor Art. 1.3a doelen (bescherming en benutten fysieke leefomgeving).

**Art. 23.5 - Voorhangprocedure**: 4 weken aan Staten-Generaal. Bijzonder: als AMvB omgevingswaarden bevat kan Kamer eisen dat deze bij wet worden vastgesteld.

**Art. 23.6 - Milieubeginselen**: Verplichte motivering van voorzorg, preventie, bronbeginsel, vervuiler betaalt.

---

## OMGEVINGSWET EXTRACTION COMPLETE

### Final Module Status

| Module | Status |
|--------|--------|
| ch1-atomic.yaml | ✅ Complete |
| ch2-afd2.1-2.6-atomic.yaml (6 files) | ✅ Complete |
| ch3-atomic.yaml | ✅ Complete |
| ch4-afd4.1-4.3-atomic.yaml (2 files) | ✅ Complete |
| ch5-*.yaml (5 files) | ✅ Complete |
| ch16-*.yaml (8 files) | ✅ Complete |
| ch18-atomic.yaml | ✅ Complete |
| ch19-atomic.yaml | ✅ Complete |
| ch20-atomic.yaml | ✅ Complete |
| ch22-ch23-atomic.yaml | ✅ Complete |

### Complete System Architecture

```
                    ┌─────────────────────────────────────┐
                    │  Ch1 FOUNDATIONS (Art. 1.3 doelen)  │
                    └─────────────────────────────────────┘
                                      │
           ┌──────────────────────────┼──────────────────────────┐
           ▼                          ▼                          ▼
    ┌─────────────┐           ┌─────────────┐           ┌─────────────┐
    │ Ch2 GOVERN  │◄─────────►│ Ch3 STRAT   │           │ Ch4 RULES   │
    │ bevoegdheden│           │ visie/progr │           │ algemene    │
    └─────────────┘           └─────────────┘           └─────────────┘
           │                          │                          │
           └──────────────────────────┼──────────────────────────┘
                                      ▼
                           ┌─────────────────┐
                           │  Ch5 PERMITS    │
                           │  vergunning +   │
                           │  projectbesluit │
                           └─────────────────┘
                                      │
                                      ▼
                           ┌─────────────────┐
                           │ Ch16 PROCEDURES │
                           │ aanvraag → loket│
                           │ → besluit → MER │
                           └─────────────────┘
                                      │
                    ┌─────────────────┼─────────────────┐
                    ▼                 ▼                 ▼
            ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
            │ Ch18 ENFORCE│   │ Ch19 EMERG  │   │ Ch20 DATA   │
            │ handhaving  │   │ bijzondere  │◄──│ monitoring  │
            │ omgevingsd. │   │ omstandigh. │   │ DSO         │
            └─────────────┘   └─────────────┘   └─────────────┘
                                      ▲                 │
                                      │                 │
                                      └─────────────────┘
                                        feedback loop

                           ┌─────────────────┐
                           │ Ch22 TRANSITION │
                           │ tijdelijk deel  │
                           │ PAS-legalisatie │
                           └─────────────────┘

                           ┌─────────────────┐
                           │ Ch23 META-RULES │
                           │ experimenten    │
                           │ voorhang        │
                           │ evaluatie       │
                           └─────────────────┘
```

---

## CHAPTERS 8-12 - PROPERTY AND LAND RIGHTS DOMAIN (Extraction 2026-01-29)

### Chapter Overview

| Chapter | Title | Articles | Function |
|---------|-------|----------|----------|
| **Ch8** | Populatiebeheer, schadebestrijding en jacht | 8.1-8.5 | Fauna management |
| **Ch9** | Voorkeursrecht | 9.1-9.22 | Preferential purchase rights |
| **Ch10** | Gedoogplichten | 10.1-10.29 | Toleration obligations |
| **Ch11** | Onteigening | 11.1-11.21 | Expropriation |
| **Ch12** | Landinrichting | 12.1-12.82 | Land consolidation |

### Instrument Hierarchy (licht → zwaar)

| # | Instrument | Effect | Eigendom |
|---|------------|--------|----------|
| 1 | **Voorkeursrecht** (Ch9) | Overheid krijgt eerste koopoptie | blijft bij eigenaar |
| 2 | **Gedoogplicht** (Ch10) | Eigenaar moet activiteit toestaan | blijft bij eigenaar |
| 3 | **Onteigening** (Ch11) | Gedwongen eigendomsovergang | gaat naar overheid |
| 4 | **Landinrichting** (Ch12) | Kavelruil ter verbetering inrichting | ruil tussen eigenaren |

### Key Patterns

**Art. 9.1 - Voorkeursrecht vestiging**: Drie grondslagen (omgevingsplan > visie/programma > beschikking)

**Art. 10.2 - Gedoogplichten van rechtswege**: Automatische gedoogplicht voor wegen, waterstaatswerken, nutsleidingen

**Art. 11.6 - Onteigening grondslag**: Planologische titel vereist (omgevingsplan/vergunning/projectbesluit)

**Art. 11.5 - Drie criteria**: Onteigeningsbelang + noodzaak + urgentie (cumulatief)

---

### Module Status (Final)

| Module | Status |
|--------|--------|
| ch1-atomic.yaml | ✅ Complete |
| ch2-afd2.1-2.6-atomic.yaml (6 files) | ✅ Complete |
| ch3-atomic.yaml | ✅ Complete |
| ch4-afd4.1-4.3-atomic.yaml (2 files) | ✅ Complete |
| ch5-*.yaml (5 files) | ✅ Complete |
| **ch8-12-property-domain-atomic.yaml** | ✅ Complete |
| ch16-*.yaml (8 files) | ✅ Complete |
| ch18-atomic.yaml | ✅ Complete |
| ch19-atomic.yaml | ✅ Complete |
| ch20-atomic.yaml | ✅ Complete |
| ch22-ch23-atomic.yaml | ✅ Complete |

### Chapters Not Extracted (Reserved/Empty/Support)

| Chapter | Status | Reason |
|---------|--------|--------|
| Ch6, Ch7, Ch14, Ch21 | Reserved | Empty in source |

---

## CHAPTERS 13, 15, 17 - FINANCIAL & ADVISORY SUPPORT (Extraction 2026-01-29)

### Chapter Overview

| Chapter | Title | Articles | Key Pattern |
|---------|-------|----------|-------------|
| **Ch13** | Financiële bepalingen | 13.1-13.25 | Leges + kostenverhaal |
| **Ch15** | Schade | 15.1-15.53 | Nadeelcompensatie |
| **Ch17** | Adviesorganen | 17.1-17.11 | Commissie m.e.r. + StAB |

### Key Discoveries

**Art. 13.22 - Anterieure overeenkomst**: Privaatrechtelijk kostenverhaal heeft voorkeur boven publiekrechtelijk.

**Art. 15.5 - Actieve risicoaanvaarding**: Woningkopers na planwijziging hebben GEEN risicoaanvaarding.

**Art. 15.7 - Normaal maatschappelijk risico**: 4% drempel voor waardevermindering onroerende zaak.

**Art. 17.9 - Gemeentelijke adviescommissie**: Verplichte commissie voor rijksmonumenten (vervangt welstands- en monumentencommissie).

---

## V2 ATOMIC EXTRACTION SCHEMA (2026-01-29)

### Schema Enhancement Rationale

The v1 atomic extraction captured artikel structure but missed critical **legal logic** that determines how norms apply. V2 schema adds:

| Enhancement | Purpose | Critical For |
|-------------|---------|--------------|
| `bron_path` | XML traceability | Source verification |
| `lid-level logica` | Capture logic per lid | Complex articles like 5.1, 5.5 |
| `conditie.type` | Distinguish TENZIJ vs VOOR ZOVER | Burden of proof determination |
| `afsluiting` capture | Don't truncate closing text | Where conditions often appear |
| `sub_onderdelen` | Nested lists | Preserve hierarchy |
| `handhaving_categorie` | ZWAAR/MIDDEL/LICHT | Enforcement priority |

### Critical Discovery: TENZIJ vs VOOR ZOVER

**Discovered during Art. 5.1 v2 extraction** - This distinction is FUNDAMENTAL to understanding Dutch administrative law:

| Keyword | Dutch | Default State | Legal Effect | Example |
|---------|-------|---------------|--------------|---------|
| **TENZIJ** | unless | Norm APPLIES | Exception REMOVES norm | Art. 5.1 lid 1: forbidden UNLESS AMvB exempts |
| **VOOR ZOVER** | insofar as | Norm DOESN'T apply | Scope ACTIVATES norm | Art. 5.1 lid 2: forbidden FOR CASES WHERE AMvB designates |

**Practical implications**:

```
TENZIJ (Art. 5.1 lid 1):
├── DEFAULT: Activity is forbidden (vergunningplichtig)
├── Burden: Initiator must prove exemption applies
└── AMvB: Lists EXEMPTIONS (vrijstellingen)

VOOR ZOVER (Art. 5.1 lid 2):
├── DEFAULT: Activity is NOT forbidden (vergunningvrij)
├── Burden: Government must designate specific cases
└── AMvB: Lists DESIGNATED CASES (aanwijzingen)
```

**Schema capture**:
```yaml
conditie:
  type: tenzij  # or voor_zover
  effect: "AMvB kan gevallen VRIJSTELLEN"  # or AANWIJZEN
  delegatie_richting: "wet → AMvB vrijstelling"
default: "vergunningplichtig"
uitzondering: "vrijgesteld indien AMvB aanwijst"
```

### Subsidiariteitstrap Pattern (from § 5.1.2)

The v2 extraction revealed the exact **subsidiariteitstrap** (decentralization ladder):

```
┌─────────────────────────────────────────────────────────────────┐
│                    SUBSIDIARITEITSTRAP                          │
│                                                                 │
│   Art. 5.8 (DEFAULT)                                            │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │  B&W (gemeente) beslist op aanvraag                     │   │
│   └─────────────────────────────────────────────────────────┘   │
│              │                                                  │
│              │ TENZIJ                                           │
│              ▼                                                  │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │  Art. 5.9: wateractiviteit                              │   │
│   │  → dagelijks bestuur waterschap / GS / Minister         │   │
│   └─────────────────────────────────────────────────────────┘   │
│              │ TENZIJ                                           │
│              ▼                                                  │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │  Art. 5.10: provinciaal belang (AMvB aanwijst)          │   │
│   │  → GS (grenzen art. 2.3 lid 2)                          │   │
│   └─────────────────────────────────────────────────────────┘   │
│              │ TENZIJ                                           │
│              ▼                                                  │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │  Art. 5.11: nationaal belang (AMvB aanwijst)            │   │
│   │  → Minister (grenzen art. 2.3 lid 3)                    │   │
│   └─────────────────────────────────────────────────────────┘   │
│              │                                                  │
│              │ + Art. 5.12: Meervoudige aanvraag               │
│              │   → Hoogste niveau in aanvraag beslist          │
│              │                                                  │
│              │ + Art. 5.13: Continuïteitsprincipe              │
│              │   → "Eens bevoegd, altijd bevoegd"              │
│              │                                                  │
│              │ + Art. 5.14: Grensoverschrijdend                │
│              │   → Zwaartepunt bepaalt BG                      │
│              │                                                  │
│              │ + Art. 5.16: Noodbevoegdheid                    │
│              │   → Minister I&W kan overnemen (nationale       │
│              │     veiligheid, rampen, calamiteiten)           │
│              │                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Key article**: Art. 2.3 (subsidiariteitsbeginsel) is referenced as boundary condition for exceptions.

### Hub-Spoke Pattern: Beoordelingsregels (from § 5.1.3)

Art. 5.18 functions as **central hub** with activity-specific **spokes**:

```
                         ┌─── 5.20 bouwactiviteit
                         │    └─ veiligheid, gezondheid, duurzaamheid
                         │
                         ├─── 5.21 omgevingsplanactiviteit
                         │    └─ toetsing aan omgevingsplan
                         │
                         ├─── 5.22 rijksmonumentenactiviteit
                         │    └─ cultureel erfgoed belangen
                         │
          ┌──────────────┼─── 5.23 ontgrondingsactiviteit
          │              │
          │              ├─── 5.24 wateractiviteit
    5.18 ─┤              │    └─ waterbeheer, ecologie
   (HUB)  │              │
          │              ├─── 5.26 milieubelastende activiteit
          │              │    └─ BBT, effectbeoordeling
          │              │
          │              ├─── 5.27 mijnbouwlocatieactiviteit
          │              │
          │              ├─── 5.28 beperkingengebiedactiviteit
          │              │
          └──────────────┼─── 5.29 Natura 2000 / flora-fauna
                         │    └─ passende beoordeling (ADC)
                         │
                         └─── 5.29a jachtgerelateerd
```

**Each spoke specifies**:
- `beschermde_belangen`: What interests are protected
- `bron_beoordelingsregels`: Where to find detailed rules (typically Bkl)
- Link back to 5.18 as grondslag

### Handhavingshiërarchie (from Art. 5.5)

Art. 5.5 creates a three-tier enforcement system captured with `handhaving_categorie`:

| Categorie | Lid | Protected Interests | Examples |
|-----------|-----|---------------------|----------|
| **ZWAAR** | 1 | veiligheid, gezondheid, milieu, waterkwaliteit, monumenten | Seveso, IPPC |
| **MIDDEL** | 2 | overige activiteiten | Bouw, ontgronding, Natura 2000 |
| **LICHT** | 3 | jacht | Jachtgeweer, valkeniers |

**Practical use**: Determines enforcement priority and sanction severity under Ch18.

### V2 Extraction Files Created

| File | Paragraaf | Key V2 Enhancements |
|------|-----------|---------------------|
| `ch5-par5.1.1-v2-atomic.yaml` | § 5.1.1 | TENZIJ vs VOOR ZOVER at lid-level, handhavingshiërarchie |
| `ch5-par5.1.2-v2-atomic.yaml` | § 5.1.2 | Subsidiariteitstrap with exact decision tree |
| `ch5-par5.1.3-v2-atomic.yaml` | § 5.1.3 | Hub-spoke pattern, beschermde_belangen per activity |

### Ch4 ↔ Ch5 Structural Parallel (from Afd 4.1 v2)

The v2 extraction of Afdeling 4.1 confirms a **structural parallel** with Afdeling 5.1:

| Chapter 4 (Regels) | Chapter 5 (Vergunning) | Function |
|--------------------|------------------------|----------|
| Art. 4.3 | Art. 5.1 | Activity list (HUB) |
| Art. 4.9 | Art. 5.8 | Default: gemeente (TENZIJ) |
| Art. 4.10 | Art. 5.9 | Water exception |
| Art. 4.11 | Art. 5.10 | Province exception |
| Art. 4.12 | Art. 5.11 | National exception |
| Art. 4.13 | Art. 5.13 | Combination/continuity |
| Art. 4.13a | Art. 5.16 | Flexibility (transfer) |

**Activity list alignment**:
```
Art. 4.3 lid 1           Art. 5.1
─────────────────        ─────────
a. bouwactiviteit    →   lid 2a
b. milieubelastend   →   lid 2b
c. lozing            →   lid 2c
d. wateronttrekking  →   lid 2d
e. mijnbouw          →   lid 2e
f. beperkingsgebied  →   lid 2f
j. Natura 2000       →   lid 1e
k. jacht/faunabeheer →   lid 1f-g
```

**Navigation implication**: For any activity, check BOTH:
- Art. 4.3 → which rules apply (via Bal/Bkl/Bbl)
- Art. 5.1 → is permit required

Often the SAME bevoegd gezag handles both.

### Navigation Implications from V2

1. **Route by condition type**:
   - TENZIJ → Check for exemptions in AMvB
   - VOOR ZOVER → Check if case is designated in AMvB

2. **Follow subsidiariteitstrap**:
   - Always start at gemeente (5.8)
   - Check explicit exceptions (5.9, 5.10, 5.11, 5.13)
   - For multiple activities, apply 5.12 (highest level wins)

3. **Use hub-spoke for assessment**:
   - Identify activity type from 5.1
   - Route to specific spoke article (5.20-5.29a)
   - Apply beschermde_belangen from that spoke

4. **Enforcement prioritization**:
   - Map violation to handhaving_categorie
   - ZWAAR → immediate action (Ch18)
   - LICHT → proportional response

---

## OMGEVINGSWET EXTRACTION 100% COMPLETE

### Final Module Status

| Module | Chapters | Status |
|--------|----------|--------|
| ch1-atomic.yaml | Ch1 | ✅ |
| ch2-afd2.1-2.6-atomic.yaml | Ch2 (6 files) | ✅ |
| ch3-atomic.yaml | Ch3 | ✅ |
| ch4-afd4.1-4.3-atomic.yaml | Ch4 (2 files) | ✅ |
| ch5-*.yaml | Ch5 (5 files) | ✅ |
| ch8-12-property-domain-atomic.yaml | Ch8-12 | ✅ |
| **ch13-15-17-support-atomic.yaml** | Ch13, Ch15, Ch17 | ✅ |
| ch16-*.yaml | Ch16 (8 files) | ✅ |
| ch18-atomic.yaml | Ch18 | ✅ |
| ch19-atomic.yaml | Ch19 | ✅ |
| ch20-atomic.yaml | Ch20 | ✅ |
| ch22-ch23-atomic.yaml | Ch22-23 | ✅ |

### Complete Omgevingswet Architecture

```
╔══════════════════════════════════════════════════════════════════╗
║                    OMGEVINGSWET NAVIGATOR                        ║
║                    Complete Legal Logic Map                      ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  CORE OPERATIONAL FLOW                                           ║
║  ┌────────────────────────────────────────────────────────────┐  ║
║  │ Ch1 → Ch2 → Ch3 → Ch4 ↔ Ch5 → Ch16 → Ch18 → Ch19 → Ch20   │  ║
║  │ doelen governance strategie regels vergunning procedures   │  ║
║  │                                   handhaving nood monitor  │  ║
║  └────────────────────────────────────────────────────────────┘  ║
║                                                                  ║
║  PROPERTY DOMAIN (Ch8-12)                                        ║
║  ┌────────────────────────────────────────────────────────────┐  ║
║  │ Ch8 fauna → Ch9 voorkeursrecht → Ch10 gedoogplicht         │  ║
║  │           → Ch11 landinrichting → Ch12 onteigening         │  ║
║  └────────────────────────────────────────────────────────────┘  ║
║                                                                  ║
║  SUPPORT SYSTEMS                                                 ║
║  ┌────────────────────────────────────────────────────────────┐  ║
║  │ Ch13 financiën (leges, kostenverhaal)                      │  ║
║  │ Ch15 schade (nadeelcompensatie, 4% drempel)                │  ║
║  │ Ch17 advies (Commissie m.e.r., StAB, gem. commissie)       │  ║
║  └────────────────────────────────────────────────────────────┘  ║
║                                                                  ║
║  CLOSING                                                         ║
║  ┌────────────────────────────────────────────────────────────┐  ║
║  │ Ch22 overgangsrecht (tijdelijk deel, PAS-legalisatie)      │  ║
║  │ Ch23 slotbepalingen (experimenten, voorhang, evaluatie)    │  ║
║  └────────────────────────────────────────────────────────────┘  ║
║                                                                  ║
║  RESERVED (Empty): Ch6, Ch7, Ch14, Ch21                          ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

### All 23 Chapters Mapped

| # | Chapter | Function | Extracted |
|---|---------|----------|-----------|
| 1 | Algemene bepalingen | Doelen, scope, zorgplicht | ✅ |
| 2 | Bevoegdheidstoedeling | Wie doet wat | ✅ |
| 3 | Omgevingsvisies en programma's | Strategie | ✅ |
| 4 | Algemene regels | Activiteitenregels | ✅ |
| 5 | Omgevingsvergunning/projectbesluit | Toestemming | ✅ |
| 6 | [Gereserveerd] | - | N/A |
| 7 | [Gereserveerd] | - | N/A |
| 8 | Populatiebeheer en jacht | Fauna | ✅ |
| 9 | Voorkeursrecht | Grondpolitiek | ✅ |
| 10 | Gedoogplichten | Toleratieplicht | ✅ |
| 11 | Landinrichting | Herverkaveling | ✅ |
| 12 | Onteigening | Ultimum remedium | ✅ |
| 13 | Financiële bepalingen | Leges, kostenverhaal | ✅ |
| 14 | [Gereserveerd] | - | N/A |
| 15 | Schade | Nadeelcompensatie | ✅ |
| 16 | Procedures | Aanvraag → besluit | ✅ |
| 17 | Adviesorganen | Commissie m.e.r., StAB | ✅ |
| 18 | Handhaving | Enforcement | ✅ |
| 19 | Bijzondere omstandigheden | Noodrecht | ✅ |
| 20 | Monitoring en informatie | DSO | ✅ |
| 21 | [Gereserveerd] | - | N/A |
| 22 | Overgangsrecht | Transitie | ✅ |
| 23 | Slotbepalingen | Meta-regels | ✅ |

**Extraction complete: 19 of 23 chapters (4 reserved/empty)**

---

## AFDELING 2.5 V2 EXTRACTION (2026-01-29)

### Doorwerking van beleid - Policy Implementation Mechanisms

Afdeling 2.5 implements the **intergovernmental hierarchy** (subsidiariteitstrap) through two distinct mechanisms:

| § | Mechanism | Instrument | Character | Articles |
|---|-----------|------------|-----------|----------|
| **2.5.1** | Instructieregels | in verordening/AMvB | ALGEMEEN, vooraf | 2.22-2.32 |
| **2.5.2** | Instructies | concreet besluit | INDIVIDUEEL, achteraf | 2.33-2.35 |
| **2.5.3** | Sancties | indeplaatstreding/vernietiging | ULTIMUM REMEDIUM | 2.36-2.37 |

### Critical Pattern: Instructieregels vs Instructies

**§ 2.5.1 INSTRUCTIEREGELS** (algemene normstelling):
```
┌─────────────────────────────────────────────────────────────────┐
│  Art. 2.22/2.24: GRONDSLAG                                      │
│  ├─ Provincie (2.22) → gemeente/waterschap                      │
│  └─ Rijk (2.24) → provincie/gemeente/waterschap                 │
│                                                                 │
│  Art. 2.23/2.25: INHOUD                                         │
│  ├─ Verplichte onderwerpen (13 categorieën bij Rijk)            │
│  ├─ Provinciaal/nationaal belang (begrenzing)                   │
│  └─ Art. 2.23 lid 4: GEEN individuele opdrachten                │
│                                                                 │
│  Art. 2.26-2.31a: SECTORSPECIFIEK                               │
│  ├─ Erfgoed, veiligheid, werelderfgoed                          │
│  ├─ Luchthavens, geluid, zwemwater                              │
│  └─ Stedelijk afvalwater, natuur (incl. stikstof!)              │
│                                                                 │
│  Art. 2.32: ONTHEFFING                                          │
│  └─ Evenredigheidstoets: "onevenredig belemmerd"                │
└─────────────────────────────────────────────────────────────────┘
```

**§ 2.5.2 INSTRUCTIES** (individuele sturing):
```
┌─────────────────────────────────────────────────────────────────┐
│  Art. 2.33/2.34: GRONDSLAG                                      │
│  ├─ GS → gemeenteraad/waterschapsbestuur (2.33)                 │
│  └─ Minister → provincie/gemeente/waterschap (2.34)             │
│                                                                 │
│  Art. 2.35: TOEPASSING                                          │
│  ├─ Lid 1: NIET voor herhaalde toepassing (→ instructieregels)  │
│  └─ Lid 2: Belang moet openbaar zijn gemaakt                    │
│                                                                 │
│  SUBSIDIARITEIT: Art. 2.33 lid 4 / Art. 2.34 lid 6              │
│  └─ Instructie NIET als Gemeentewet/Provinciewet/Waterschapswet │
│     regulier toezicht mogelijk maakt                            │
└─────────────────────────────────────────────────────────────────┘
```

### Escalatieladder Interbestuurlijk Toezicht

```
Level 1: INSTRUCTIE (zacht)
   ↓ geen gevolg binnen termijn
Level 2: INDEPLAATSTREDING (art. 2.36)
   ├─ GS treedt in de plaats van waterschap (lid 1)
   └─ Minister treedt in de plaats van waterschap (lid 2)
   ↓ achteraf onrechtmatig bevonden
Level 3: VERNIETIGING (art. 2.37)
   └─ Koninklijk besluit vernietigt waterschapsbesluit
```

**Let op**: Art. 2.36-2.37 gaan ALLEEN over waterschappen. Voor gemeente/provincie: Gemeentewet/Provinciewet.

### Sectorale Verplichte Instructieregels (Art. 2.26-2.31a)

| Artikel | Sector | Doel | EU-richtlijn |
|---------|--------|------|--------------|
| 2.26 | Cultureel erfgoed | rijksmonumenten, stads-/dorpsgezichten | - |
| 2.27 | Externe veiligheid | aandachtsgebieden (Bkl 5.12-5.16) | Seveso |
| 2.28 | Werelderfgoed | UNESCO-bescherming | - |
| 2.29 | Luchthavens | Schiphol, regionale, militaire | Chicago |
| 2.29a | Geluid | geluidproductieplafonds | - |
| 2.30 | Zwemlocaties | aanwijzing, badseizoen | Zwemwaterrichtlijn |
| 2.31 | Stedelijk afvalwater | openbare riolen | Richtlijn stedelijk afvalwater |
| 2.31a | Natuur | N2000, soorten, **stikstofdepositie** | Vogel-/Habitatrichtlijn |

**Kritiek**: Art. 2.31a lid 2 (stikstofdepositieruimte) is FACULTATIEF ("kunnen worden gesteld"), niet verplicht!

### Art. 2.32 Ontheffingsmechanisme

```yaml
# Ontheffingspatroon
DEFAULT: instructieregel geldt
TENZIJ: ontheffing verleend

# Wie verleent?
provinciale_instructieregel:
  verlener: gedeputeerde_staten
  aanvrager: gemeente/waterschap

rijks_instructieregel:
  verlener: Minister (of GS bij provinciale locatiebepaling)
  aanvrager: gemeente/waterschap/provincie

# Criterium (art. 2.32 lid 5)
toetsing: evenredigheid
norm: "onevenredig belemmerd in verhouding tot belang"
```

### Navigation Routes (Afd 2.5)

| Vraag | Entry Point | Route |
|-------|-------------|-------|
| "Hoe werkt provinciaal beleid door naar gemeenten?" | Art. 2.22 | → 2.23 (inhoud) → 2.32 (ontheffing) |
| "Hoe werkt rijksbeleid door naar lagere overheden?" | Art. 2.24 | → 2.25 (inhoud) → 2.26-2.31a (specifiek) |
| "Kan de provincie een gemeente een aanwijzing geven?" | Art. 2.33 | → 2.35 (begrenzingen) → evt. 2.36 (indeplaatstreding) |
| "Is er ontheffing mogelijk van instructieregels?" | Art. 2.32 | → specifieke voorwaarden per lid |
| "Wat als waterschap instructie niet opvolgt?" | Art. 2.36 | → indeplaatstreding, evt. → 2.37 vernietiging |

### Cross-Chapter Connections

```
Art. 2.3 (subsidiariteit)
    ↓ grenzen voor
Art. 2.22/2.24 (instructieregels)
    ↓ doorwerking naar
Art. 4.1/4.2 (omgevingsverordening/omgevingsplan)
    ↓ toepassing via
Art. 5.8-5.11 (bevoegd gezag vergunning)
    ↓ handhaving via
Hoofdstuk 18 (handhavingsladder)
```

### V2 Extraction Files Summary

| File | Version | Key Patterns |
|------|---------|--------------|
| `ch5-par5.1.1-v2-atomic.yaml` | V2 | TENZIJ vs VOOR ZOVER, handhavingshiërarchie |
| `ch5-par5.1.2-v2-atomic.yaml` | V2 | Subsidiariteitstrap, beslisboom |
| `ch5-par5.1.3-v2-atomic.yaml` | V2 | Hub-spoke beoordelingsregels |
| `ch4-afd4.1-v2-atomic.yaml` | V2 | 4.3 hub, Ch4↔Ch5 parallel |
| `ch16-par16.5-v2-atomic.yaml` | V2 | Loketfunctie, lex silencio exclusie |
| **`ch2-afd2.5-v2-atomic.yaml`** | V2 | Instructieregels vs instructies, escalatieladder |
| **`ch18-v2-atomic.yaml`** | V2 | WIE VERLEENT=WIE HANDHAAFT, boetecategorieën, omgevingsdiensten |

---

## CHAPTER 18 V2 EXTRACTION (2026-01-29)

### Core Principle: "Wie Verleent = Wie Handhaaft"

Art. 18.2 implements seamless accountability through direct coupling:

```
┌─────────────────────────────────────────────────────────────────┐
│  ACTIVITY WITH GENERAL RULES (§ 4.1.1)?                         │
│  ├─ Art. 18.2 lid 1: BG from § 4.1.3 enforces                   │
│  └─ Links to: Art. 4.9 (gemeente) / 4.10-4.12 (exceptions)      │
│                                                                 │
│  ACTIVITY WITH PERMIT REQUIREMENT (Ch5)?                        │
│  ├─ Art. 18.2 lid 2: BG from § 5.1.2 enforces                   │
│  └─ Links to: Art. 5.8 (gemeente) / 5.9-5.11 (exceptions)       │
│                                                                 │
│  DEFAULT (Art. 18.2 lid 5):                                     │
│  └─ B&W is fallback enforcer                                    │
└─────────────────────────────────────────────────────────────────┘
```

### Enforcement Ladder (licht → zwaar)

| Level | Instrument | Legal Basis | Character |
|-------|------------|-------------|-----------|
| 1 | Warning | informal | preventief |
| 2 | Last onder dwangsom | Awb 5:32 | preventief |
| 3 | Last onder bestuursdwang | Art. 18.4 | feitelijk |
| 4 | Intrekking beschikking | Art. 18.10 | beëindiging |
| 5 | Bestuurlijke boete | Art. 18.11-18.15 | punitief |
| 6 | Strafrechtelijke vervolging | Art. 18.16 → OM | punitief |

### Boete Categories by Sector

| Article | Sector | Maximum | Sr Category |
|---------|--------|---------|-------------|
| 18.11 | Seveso-richtlijn | 6e cat. OR 10% omzet | ZWAAR |
| 18.12 | Bouw/sloop | 2e cat. (→ 4e bij gevaar) | LICHT-MIDDEL |
| 18.13 | Erfgoed | 5e cat. | MIDDEL |
| 18.14 | Luchthaven | 5e cat. | MIDDEL |
| 18.15 | Spoor | via Spoorwegwet | via sectorwet |
| 18.15a | Flora/fauna handel | 1e-2e cat. | LICHT |

### Omgevingsdiensten (Art. 18.21-18.24)

```
┌─────────────────────────────────────────────────────────────────┐
│  VERPLICHTE INSTELLING (Art. 18.21)                             │
│  ├─ GS + B&W MOETEN omgevingsdienst instellen                   │
│  ├─ Territoir: veiligheidsregio of aangewezen kring             │
│  └─ Rechtsvorm: openbaar lichaam via Wgr                        │
│                                                                 │
│  TAKEN (Art. 18.22)                                             │
│  ├─ BASISTAKENPAKKET: alle omgevingsdiensten (bij AMvB)         │
│  └─ BIJZONDERE TAKEN: speciale diensten voor:                   │
│      ├─ IPPC categorie 4 installaties                           │
│      └─ Seveso-inrichtingen                                     │
└─────────────────────────────────────────────────────────────────┘
```

### Three-Pillar Consistency

| Domain | Default Gemeente | Exception Pattern |
|--------|------------------|-------------------|
| Rules (Ch4) | Art. 4.9 B&W | Art. 4.10-4.12 TENZIJ |
| Permits (Ch5) | Art. 5.8 B&W | Art. 5.9-5.11 TENZIJ |
| Enforcement (Ch18) | Art. 18.2 lid 5 B&W | Art. 18.2 lid 1-4 TENZIJ |

---

## V2 SCHEMA UPDATE: DOORWERKING PATTERNS

Based on Afd 2.5 extraction, add to schema:

```yaml
# For doorwerking-related articles
doorwerking:
  type: instructieregel | instructie
  richting: rijk_naar_provincie | rijk_naar_gemeente | rijk_naar_waterschap | provincie_naar_gemeente | provincie_naar_waterschap
  karakter: algemeen | individueel
  instrument_doel: omgevingsverordening | omgevingsplan | waterschapsverordening | projectbesluit

# For sanctie articles
interbestuurlijk_toezicht:
  niveau: instructie | indeplaatstreding | vernietiging
  actor: gedeputeerde_staten | minister | kroon
  target: gemeente | waterschap | provincie

# For sectorale verplichtingen
sectorale_verplichting:
  sector: erfgoed | veiligheid | werelderfgoed | luchthavens | geluid | zwemwater | afvalwater | natuur
  eu_implementatie: boolean
  richtlijn: string  # if applicable
```

---

## CHAPTER 11 V2 EXTRACTION: ONTEIGENING (2026-01-29)

### Grondbeleid Trilogy Complete

Chapter 11 completes the "grondbeleid drieluik" (land policy triptych):

| Instrument | Chapter | Karakter | Eigendom | Ingrijpendheid |
|------------|---------|----------|----------|----------------|
| **Voorkeursrecht** | Ch9 | Vrijwillige verkoop, overheid eerste koper | blijft bij eigenaar | LICHT |
| **Gedoogplicht** | Ch10 | Eigenaar moet activiteit dulden | blijft bij eigenaar | MIDDEL |
| **Onteigening** | Ch11 | Gedwongen eigendomsovergang | gaat naar overheid | ZWAAR |

### Core Structure: 5 Afdelingen

```
┌─────────────────────────────────────────────────────────────────┐
│  AFDELING 11.1: ALGEMENE BEPALINGEN                             │
│  ├─ Art. 11.1: Grondwettelijke basis (art. 14 Gw)               │
│  └─ Art. 11.2: Wie kan onteigenaar zijn (5 categorieën)         │
│                                                                 │
│  AFDELING 11.2: ONTEIGENINGSBESCHIKKING                         │
│  ├─ Art. 11.3: Aanwijzing te onteigenen zaken                   │
│  ├─ Art. 11.4: Bevoegd gezag (gemeenteraad/waterschap/PS/Min)   │
│  ├─ Art. 11.5: DRIE CUMULATIEVE CRITERIA ← kerntoets            │
│  │   ├─ (a) onteigeningsbelang → Art. 11.6 (planologische titel)│
│  │   ├─ (b) noodzaak → Art. 11.7-11.10 (minnelijk/zelfrealisatie)│
│  │   └─ (c) urgentie → Art. 11.11 (3-jaar-termijn)              │
│  └─ Art. 11.12-11.13: Verval en procedurele uitsluiting         │
│                                                                 │
│  AFDELING 11.3: SCHADELOOSSTELLING                              │
│  └─ Art. 11.14: Route naar afd. 15.3 (civiele rechter)          │
│                                                                 │
│  AFDELING 11.4: ONTEIGENINGSAKTE                                │
│  ├─ Art. 11.15-11.17: Verlijden en ondertekening                │
│  ├─ Art. 11.18: ZUIVERENDE WERKING (vrij van alle lasten)       │
│  └─ Art. 11.19-11.20: Lasten en inbezitstelling                 │
│                                                                 │
│  AFDELING 11.5: NIET VERWEZENLIJKEN                             │
│  └─ Art. 11.21: TERUGLEVERING bij niet-verwezenlijking          │
└─────────────────────────────────────────────────────────────────┘
```

### Critical Pattern: Criteria Triade (Art. 11.5)

Art. 11.5 is the **central gatekeeper** for all expropriation:

```
┌─────────────────────────────────────────────────────────────────┐
│              DRIE CUMULATIEVE CRITERIA (Art. 11.5)              │
│                                                                 │
│  1. ONTEIGENINGSBELANG (Art. 11.6)                              │
│     ├─ Omgevingsplan (onder uitsluiting bestaand gebruik)       │
│     ├─ Buitenplanse omgevingsvergunning, OF                     │
│     └─ Projectbesluit                                           │
│     → PLANOLOGISCHE TITEL VEREIST                               │
│                                                                 │
│  2. NOODZAAK (Art. 11.7-11.10)                                  │
│     ├─ Minnelijke verwerving geprobeerd? (lid 1)                │
│     ├─ Zelfrealisatie door eigenaar? (lid 2)                    │
│     │   └─ Anti-misbruik: vervalt na 3 jaar non-realisatie      │
│     ├─ Openbare orde: eerst Woningwet-bevoegdheden (11.8)       │
│     ├─ Opiumwet: eerst Woningwet-bevoegdheden (11.9)            │
│     └─ Leefbaarheid: eerst Woningwet-bevoegdheden (11.10)       │
│     → ULTIMUM REMEDIUM VERPLICHT                                │
│                                                                 │
│  3. URGENTIE (Art. 11.11)                                       │
│     └─ Binnen 3 jaar na inschrijving akte: begin verwezenlijking│
│     → GEEN VOORRAAD-ONTEIGENING                                 │
│                                                                 │
│  ALLE DRIE moeten voldaan zijn!                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Eigenaarsbescherming Mechanismen

| Mechanisme | Artikel | Werking |
|------------|---------|---------|
| **Zelfrealisatierecht** | 11.7 lid 2 | Eigenaar kan zelf bestemming verwezenlijken |
| **Volledige gebouw/erf** | 11.3 lid 2 | Bij gedeeltelijke onteigening: uitbreiding op verzoek |
| **Betaling vooraf** | 11.16 lid 1c | Geen overdracht zonder schadeloosstelling |
| **Teruglevering** | 11.21 | Bij niet-verwezenlijking: terugkoop of extra schadevergoeding |

### Termijnensysteem (3-jaar patroon)

```
VOORAF (besluitvorming):
├─ Art. 11.7 lid 3: Zelfrealisatierecht vervalt na 3 jaar non-realisatie
├─ Art. 11.11: Urgentie ontbreekt als niet binnen 3 jaar begonnen
└─ Art. 11.12: Beschikking vervalt na 12 maanden zonder verzoek rechtbank

ACHTERAF (uitvoering):
├─ Art. 11.15: Verzoek verlijden binnen 2 maanden na voldoen voorwaarden
├─ Art. 11.21 lid 1: Aanbod teruglevering als niet binnen 3 jaar begonnen
└─ Art. 11.21 lid 4: Keuzerecht onteigende als geen aanbod binnen 3 maanden
```

### Zuiverende Werking (Art. 11.18)

```
INSCHRIJVING ONTEIGENINGSAKTE
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│  EIGENDOM VRIJ VAN ALLE LASTEN EN RECHTEN                       │
│  ├─ Hypotheken: vervallen (ambtshalve doorroyement)             │
│  ├─ Beslagen: vervallen (ambtshalve doorroyement)               │
│  ├─ Beperkte rechten: vervallen                                 │
│  │                                                              │
│  └─ UITZONDERING: Erfdienstbaarheden (mits in akte opgenomen)   │
└─────────────────────────────────────────────────────────────────┘
```

### Bevoegdheidsverdeling (Art. 11.4)

| Bevoegd Gezag | Bestuursorgaan | Begrenzing |
|---------------|----------------|------------|
| **Gemeente** | gemeenteraad | geen (default) |
| **Waterschap** | algemeen bestuur | alleen voor waterschapstaken (art. 2.17) |
| **Provincie** | provinciale staten | provinciaal belang OF doelmatigheid |
| **Rijk** | Minister die het aangaat | nationaal belang OF doelmatigheid |

### Drie Rechtelijke Sporen

```
SPOOR 1: BESTUURSRECHTER (beschikking)
├─ Bekrachtiging onteigeningsbeschikking
└─ Hoger beroep: ABRvS

SPOOR 2: CIVIELE RECHTER (schadeloosstelling)
├─ Verzoek vaststelling schadeloosstelling (art. 11.14)
└─ Procedure: afdeling 15.3

SPOOR 3: VOORZIENINGENRECHTER (executie)
├─ Inbezitstelling na inschrijving akte (art. 11.20)
└─ Geen hogere voorziening!
```

### Navigation Routes

| Vraag | Entry Point | Route |
|-------|-------------|-------|
| "Mag dit onteigend worden?" | Art. 11.5 | → 11.6 (grondslag) → 11.7-11.11 (noodzaak/urgentie) |
| "Wie mag onteigenen?" | Art. 11.4 | → check bestuurslaag en begrenzing |
| "Kan de eigenaar zelf realiseren?" | Art. 11.7 lid 2 | → check criteria → evt. 11.7 lid 3 (anti-misbruik) |
| "Wanneer krijg ik schadeloosstelling?" | Art. 11.14 | → 11.16 (voorwaarden) → afd. 15.3 |
| "Wat als onteigenaar niet verwezenlijkt?" | Art. 11.21 | → teruglevering OF extra schadevergoeding |

### Cross-Chapter Connections

```
Ch9 (Voorkeursrecht) ──────────────┐
                                   │
Ch10 (Gedoogplicht) ───────────────┼──► Ch11 (Onteigening)
                                   │         │
Grondwet art. 14 ──────────────────┘         │
                                             ▼
                                       Ch15 afd. 15.3
                                    (Schadeloosstelling)
```

### Module Status Update

| Module | Status |
|--------|--------|
| ch1-v2-atomic.yaml | ✅ Complete |
| ch9-v2-atomic.yaml | ✅ Complete |
| ch10-v2-atomic.yaml | ✅ Complete |
| ch11-v2-atomic.yaml | ✅ Complete |
| ch12-v2-atomic.yaml | ✅ Complete |
| ch8-v2-atomic.yaml | ✅ Complete |
| ch13-v2-atomic.yaml | ✅ Complete |
| ch15-v2-atomic.yaml | ✅ Complete |
| ch17-v2-atomic.yaml | ✅ Complete |
| ch19-v2-atomic.yaml | ✅ Complete |
| **ch20-v2-atomic.yaml** | ✅ Complete |
| **ch22-v2-atomic.yaml** | ✅ Complete |
| **ch23-v2-atomic.yaml** | ✅ Complete |

---

## CHAPTER 12 V2 EXTRACTION: LANDINRICHTING (2026-01-29)

### Instrument Positioning in Grondbeleid

| # | Instrument | Chapter | Karakter | Effect |
|---|------------|---------|----------|--------|
| 1 | Voorkeursrecht | Ch9 | Aankoopprioriteit | Eigendom blijft |
| 2 | Gedoogplicht | Ch10 | Toleratieplicht | Eigendom blijft |
| 3 | **Landinrichting** | **Ch12** | **Collectieve herordening** | **Ruil, geen afname** |
| 4 | Onteigening | Ch11 | Eigendomsontneming | Eigendom gaat over |

### Core Structure: 6 Afdelingen

```
┌─────────────────────────────────────────────────────────────────┐
│  AFDELING 12.1: ALGEMENE BEPALINGEN                             │
│  ├─ § 12.1.1: Begripsbepalingen (rechthebbende, zakelijk ger.)  │
│  └─ § 12.1.2: Algemene bepalingen landinrichting                │
│                                                                 │
│  AFDELING 12.2: INRICHTINGSBESLUIT                              │
│  ├─ § 12.2.1: Vaststelling en inhoud                            │
│  └─ § 12.2.2: Toedeling eigendom/beheer/onderhoud               │
│                                                                 │
│  AFDELING 12.3: UITVOERING VAN LANDINRICHTING                   │
│  ├─ § 12.3.1: Algemene bepalingen                               │
│  └─ § 12.3.2: Verrichten werkzaamheden                          │
│                                                                 │
│  AFDELING 12.4: HERVERKAVELING ← KERN                           │
│  ├─ § 12.4.1: Algemene bepalingen                               │
│  ├─ § 12.4.2: Het ruilbesluit (12.22-12.35)                     │
│  └─ § 12.4.3: Besluit geldelijke regelingen (12.36-12.41)       │
│                                                                 │
│  AFDELING 12.5: OVERIGE BEPALINGEN                              │
│                                                                 │
│  AFDELING 12.6: KAVELRUIL ← VRIJWILLIG ALTERNATIEF              │
│  └─ Art. 12.44-12.47: Kavelruilovereenkomst                     │
└─────────────────────────────────────────────────────────────────┘
```

### Critical Pattern: 5%-Korting (Art. 12.29)

```
┌─────────────────────────────────────────────────────────────────┐
│  KORTING: COLLECTIEVE EIGENDOMSBIJDRAGE (Art. 12.29)            │
│                                                                 │
│  TOTALE OPPERVLAKTE HERVERKAVELINGSBLOK                         │
│           │                                                     │
│           ▼                                                     │
│  MAX 5% VERMINDERD VOOR:                                        │
│  ├─ (a) Openbare wegen en waterstaatswerken                     │
│  ├─ (b) Samenhangende voorzieningen                             │
│  ├─ (c) Natuur/landschap/erfgoed                                │
│  └─ (d) Andere voorzieningen van openbaar nut                   │
│           │                                                     │
│           ▼                                                     │
│  PROPORTIONELE VERDELING (Art. 12.30)                           │
│  └─ Elke eigenaar levert evenredig percentage in                │
│                                                                 │
│  VOORDEEL T.O.V. ONTEIGENING:                                   │
│  ├─ Geen volledige schadeloosstelling per perceel               │
│  ├─ Collectieve lastenverdeling                                 │
│  └─ Sneller en goedkoper                                        │
└─────────────────────────────────────────────────────────────────┘
```

### Eigenaarsbescherming Triade (Art. 12.26, 12.30)

| Bescherming | Artikel | Inhoud |
|-------------|---------|--------|
| **Aard behoud** | 12.26 lid 1 | Recht van dezelfde aard als inbreng |
| **Hoedanigheid behoud** | 12.26 lid 2 | Gelijke hoedanigheid, gelijkwaardige gebruiksmogelijkheden |
| **Oppervlakte behoud** | 12.30 | Gelijke oppervlakte minus proportionele korting |

**Maximum inlevering**: Max 5% kleiner dan inbreng (art. 12.30 lid 3)

### Vrijwillig vs Van Bovenaf

| Instrument | Basis | Initiatief | Karakter |
|------------|-------|------------|----------|
| **Herverkaveling** | Afd. 12.4 | GS (van bovenaf) | Publiekrechtelijk |
| **Kavelruil** | Afd. 12.6 | Eigenaren (vrijwillig) | Privaatrechtelijk |

**Kavelruil vereisten** (art. 12.44):
- Drie of meer eigenaren
- Notariële akte
- Inschrijving openbare registers
- Medeondertekening hypotheekhouders/beslagleggers

### Absolute Uitzonderingen

| Object | Artikel | Effect |
|--------|---------|--------|
| **Begraafplaatsen** | 12.10 lid 1 | Geen wijziging rechten/gebruikstoestand |
| **Militaire locaties** | 12.5 | Toestemming Minister Defensie vereist |
| **Gebouwen** | 12.10 lid 2 | Toestemming eigenaar vereist |

### Navigation Routes

| Vraag | Entry Point | Route |
|-------|-------------|-------|
| "Wat is landinrichting?" | Art. 12.3 | → 12.4 (bevoegdheid) → 12.7 (inrichtingsbesluit) |
| "Hoeveel mag ik kwijtraken?" | Art. 12.29 | → 12.30 (max 5% totaal) |
| "Kan ik vrijwillig ruilen?" | Art. 12.44 | → 12.47 (landelijk gebied) |
| "Wie is bevoegd?" | Art. 12.4/12.20 | → GS is bevoegd gezag |

### Cross-Chapter Connections

```
Ch10 (Gedoogplichten) ──────► Art. 10.10c-10.10g
                              (gedoogplichten landinrichting)
                                      │
                                      ▼
                              Ch12 (Landinrichting)
                                      │
                                      ├──► Ch13 (Financiën)
                                      │    (kostenverdeling)
                                      │
                                      └──► Ch16 (Procedures)
                                           (§ 16.12.2 landinrichting)
```

---

## CHAPTER 8 V2 EXTRACTION: POPULATIEBEHEER, SCHADEBESTRIJDING EN JACHT (2026-01-29)

### Instrument Positioning in Domain-Specific Chapters

| Chapter | Domain | Karakter | Bevoegd Gezag |
|---------|--------|----------|---------------|
| **Ch 8** | Fauna management | Provincie-centraal | GS/PS |
| Ch 9 | Voorkeursrecht | Aankoopprioriteit | Gemeente |
| Ch 10 | Gedoogplichten | Toleratieplicht | Diverse |
| Ch 11 | Onteigening | Eigendomsontneming | Diverse |
| Ch 12 | Landinrichting | Collectieve herordening | GS |

### Core Structure: 5 Artikelen (Compact Chapter)

```
┌─────────────────────────────────────────────────────────────────┐
│  Art. 8.1: FAUNABEHEEREENHEDEN EN FAUNABEHEERPLANNEN            │
│  ├─ Lid 1: Provinciale Staten stellen bij omgevingsverordening: │
│  │   ├─ (a) grens van faunabeheereenheden                       │
│  │   ├─ (b) vereisten aan samenstelling faunabeheereenheid      │
│  │   └─ (c) vereisten aan inhoud faunabeheerplan                │
│  ├─ Lid 2: Faunabeheereenheid stelt vast: faunabeheerplan       │
│  │         TENZIJ omgevingsverordening dit aan PS opdraagt      │
│  └─ Lid 3: Inwerkingtreding: na goedkeuring door GS             │
│                                                                 │
│  Art. 8.2: WILDBEHEEREENHEDEN (AANSLUITPLICHT)                  │
│  ├─ Lid 1: PS stellen grens van wildbeheereenheden vast         │
│  ├─ Lid 2: Jachthouder is VERPLICHT AANGESLOTEN bij wildbeheer  │
│  │         → Conditie: voor gronden binnen grenzen              │
│  └─ Lid 3: Wildbeheereenheden geven UITVOERING aan              │
│            faunabeheerplan                                      │
│                                                                 │
│  Art. 8.3: DE JACHT ← LIMITATIEVE OPSOMMINGEN                   │
│  ├─ Lid 1: JACHTHOUDER = wie gerechtigd is tot jagen, is één:   │
│  │   ├─ (a) EIGENAAR: wie gebruik van jachtrecht niet verloren  │
│  │   ├─ (b) GERECHTIGDE: via zakelijk gebruiksrecht             │
│  │   ├─ (c) PACHTER: bij gemengde/verpachte landbouwbedrijven   │
│  │   └─ (d) HUURDER: van jachtrecht door eigenaar               │
│  ├─ Lid 2: BEPERKINGEN op jachtrecht:                           │
│  │   ├─ (a) Terreinen ≤ 40 hectare: 1 jachthouder max           │
│  │   └─ (b) Grotere terreinen: bij AMvB                         │
│  ├─ Lid 3: JACHTWILD (limitatief):                              │
│  │   haas, fazant, wilde eend, houtduif, konijn                 │
│  └─ Lid 4: Regeling jachtseizoen bij AMvB                       │
│                                                                 │
│  Art. 8.4: AANSPRAKELIJKHEIDSVERZEKERING JACHTGEWEREN           │
│  ├─ Lid 1: VERZEKERINGSPLICHT voor jachtgeweerhouder            │
│  │         → EUR 1.000.000 per gebeurtenis                      │
│  ├─ Lid 2: Polis bij door AFM toegelaten verzekeraar            │
│  └─ Lid 3: DIRECT ACTION: benadeelde kan rechtstreeks van       │
│            verzekeraar vorderen                                 │
│                                                                 │
│  Art. 8.5: AFPALINGSRECHT EENDENKOOIEN                          │
│  └─ Historisch recht: afpaling op 1130 meter                    │
└─────────────────────────────────────────────────────────────────┘
```

### Critical Pattern: Provincie-Centrale Organisatie

```
┌─────────────────────────────────────────────────────────────────┐
│              PROVINCIALE REGIE (Art. 8.1-8.2)                   │
│                                                                 │
│  PROVINCIALE STATEN                                             │
│  ├─ Stelt grenzen vast van:                                     │
│  │   ├─ Faunabeheereenheden (art. 8.1 lid 1a)                   │
│  │   └─ Wildbeheereenheden (art. 8.2 lid 1)                     │
│  ├─ Bepaalt vereisten aan:                                      │
│  │   ├─ Samenstelling faunabeheereenheid (art. 8.1 lid 1b)      │
│  │   └─ Inhoud faunabeheerplan (art. 8.1 lid 1c)                │
│  └─ Kan zelf faunabeheerplan vaststellen (art. 8.1 lid 2 TENZIJ)│
│                                                                 │
│  GEDEPUTEERDE STATEN                                            │
│  └─ Keurt faunabeheerplan goed (art. 8.1 lid 3)                 │
│                                                                 │
│  FAUNABEHEEREENHEID                                             │
│  └─ Stelt faunabeheerplan vast (art. 8.1 lid 2 default)         │
│                                                                 │
│  WILDBEHEEREENHEID                                              │
│  └─ Voert faunabeheerplan uit (art. 8.2 lid 3)                  │
└─────────────────────────────────────────────────────────────────┘
```

### Limitatieve Opsommingen (Rechtszekerheid)

| Subject | Artikel | Lijst |
|---------|---------|-------|
| **Jachtgerechtigden** | 8.3 lid 1 | Eigenaar, zakelijk gerechtigde, pachter, huurder |
| **Jachtwild** | 8.3 lid 3 | Haas, fazant, wilde eend, houtduif, konijn |
| **Beperkingen** | 8.3 lid 2 | ≤40 ha: 1 jachthouder; >40 ha: bij AMvB |

**Juridische betekenis**: Gesloten lijsten - wat niet genoemd is, valt erbuiten.

### Verzekeringsplicht met Direct Action (Art. 8.4)

```
┌─────────────────────────────────────────────────────────────────┐
│  AANSPRAKELIJKHEIDSVERZEKERING (Art. 8.4)                       │
│                                                                 │
│  VERPLICHTING (lid 1):                                          │
│  ├─ Wie: Jachtgeweerhouder                                      │
│  ├─ Waarvoor: Schade aan personen en zaken                      │
│  └─ Minimum: EUR 1.000.000 per gebeurtenis                      │
│                                                                 │
│  VERZEKERAAR (lid 2):                                           │
│  └─ Door AFM toegelaten tot uitoefening bedrijf                 │
│                                                                 │
│  DIRECT ACTION (lid 3):                                         │
│  ├─ Benadeelde kan RECHTSTREEKS vorderen van verzekeraar        │
│  ├─ Geen omweg via jachtgeweerhouder nodig                      │
│  └─ Gelijk aan WAM-systematiek in verkeersrecht                 │
│                                                                 │
│  PROCESSUELE POSITIE:                                           │
│  └─ Benadeelde → rechtstreeks → verzekeraar                     │
└─────────────────────────────────────────────────────────────────┘
```

### Historisch Recht: Afpalingsrecht (Art. 8.5)

```
┌─────────────────────────────────────────────────────────────────┐
│  EENDENKOOIEN - AFPALINGSRECHT                                  │
│                                                                 │
│  GERECHTIGDE: Rechthebbende op eendenkooi                       │
│                                                                 │
│  RECHT: Afpaling (verbod jachtbedrijf rond kooi)                │
│  AFSTAND: 1130 meter                                            │
│                                                                 │
│  HISTORISCHE OORSPRONG:                                         │
│  ├─ Middeleeuwse kooiers                                        │
│  └─ Bescherming tegen verstoring door nabije jacht              │
│                                                                 │
│  PRAKTISCHE WERKING:                                            │
│  └─ Binnen 1130m van kooi mag geen jacht worden uitgeoefend     │
└─────────────────────────────────────────────────────────────────┘
```

### Navigation Routes

| Vraag | Entry Point | Route |
|-------|-------------|-------|
| "Wie mag jagen?" | Art. 8.3 lid 1 | → check categorie (a)-(d) |
| "Op welke dieren mag gejaagd?" | Art. 8.3 lid 3 | → limitatieve lijst |
| "Moet ik me aansluiten?" | Art. 8.2 lid 2 | → ja, als jachthouder binnen grenzen |
| "Wie stelt faunabeheerplan vast?" | Art. 8.1 lid 2-3 | → faunabeheereenheid, tenzij PS; goedkeuring GS |
| "Is jachtgeweer verzekerd?" | Art. 8.4 | → verplicht EUR 1M, direct action mogelijk |

### Cross-Chapter Connections

```
Ch 5 (Vergunningen) ──────► Art. 5.1 lid 2
                            (jacht activiteiten)
                                   │
                                   ▼
                           Ch 8 (Jacht)
                                   │
                                   ├──► Bal (specifieke regels)
                                   │
                                   └──► Omgevingsverordening
                                        (faunabeheereenheden)
```

### Schema Update: New Patterns from Ch8

```yaml
# For limitatieve opsommingen
limitatieve_lijst:
  type: jachtgerechtigden | jachtwild | andere
  opsomming: [list of items]
  juridisch_effect: gesloten_systeem

# For verzekeringsverplichting
verzekering:
  plicht: boolean
  minimum: EUR amount
  direct_action: boolean
  toezichthouder: AFM | DNB | other

# For historische rechten
historisch_recht:
  type: afpalingsrecht | andere
  gerechtigde: who
  object: what
  afstand_of_maat: specific measurement
```

---

## CHAPTER 2 V2 EXTRACTION: TAKEN EN BEVOEGDHEDEN (2026-01-29)

### Complete V2 Upgrade for Chapter 2

All 6 afdelingen now have V2 atomic extractions with full schema compliance:

| Afdeling | Articles | V2 File | Key Patterns |
|----------|----------|---------|--------------|
| **2.1** | 2.1-2.3 | ch2-afd2.1-v2-atomic.yaml | Subsidiariteitsbeginsel, doelgebondenheid |
| **2.2** | 2.4-2.8 | ch2-afd2.2-v2-atomic.yaml | One-plan-principle, exclusiviteit |
| **2.3** | 2.9-2.15a | ch2-afd2.3-v2-atomic.yaml | Omgevingswaarden, stikstof (resultaatsverplichting) |
| **2.4** | 2.16-2.21a | ch2-afd2.4-v2-atomic.yaml | Taaktoedeling per bestuurslaag |
| **2.5** | 2.22-2.37 | ch2-afd2.5-v2-atomic.yaml | Instructieregels vs instructies |
| **2.6** | 2.38-2.46 | ch2-afd2.6-v2-atomic.yaml | Bijzondere taken (water, geluid, natuur) |

### NEW PATTERN: Subsidiariteitsladder (Art. 2.3)

```
┌─────────────────────────────────────────────────────────────────┐
│  SUBSIDIARITEITSBEGINSEL (Art. 2.3)                             │
│                                                                 │
│  DEFAULT: Gemeente                                              │
│     │                                                           │
│     ├─ "tenzij daarover andere regels zijn gesteld"             │
│     │                                                           │
│     ▼                                                           │
│  PROVINCIE (lid 2) - alleen als nodig voor:                     │
│     ├─ (a) provinciaal belang EN gemeente kan niet behartigen   │
│     └─ (b) doelmatige uitoefening OF internationale verplichting│
│     │                                                           │
│     ▼                                                           │
│  RIJK (lid 3) - alleen als nodig voor:                          │
│     ├─ (a) nationaal belang EN prov/gem kan niet behartigen     │
│     └─ (b) doelmatige uitoefening OF internationale verplichting│
│     │                                                           │
│     ▼                                                           │
│  RIJK (lid 4) - altijd voor niet-ingedeeld gebied (zee, EEZ)    │
└─────────────────────────────────────────────────────────────────┘
```

### NEW PATTERN: Omgevingswaarden Hierarchie (Afd 2.3)

```
┌─────────────────────────────────────────────────────────────────┐
│  OMGEVINGSWAARDEN HIËRARCHIE                                    │
│                                                                 │
│  NIVEAU 1: WET (art. 2.15a)                                     │
│  └─ Stikstof: 40% (2025) → 50% (2030) → 74% (2035)              │
│     ├─ RESULTAATSVERPLICHTING (lid 2)                           │
│     └─ Enige wettelijk verankerde omgevingswaarde               │
│                                                                 │
│  NIVEAU 2: RIJK - AMvB (art. 2.14-2.15)                         │
│  └─ Verplicht: luchtkwaliteit, waterkwaliteit, zwemwater,       │
│     waterveiligheid (primaire waterkeringen), geluid rijksinfra │
│     ├─ EU-grondslag voor veel waarden                           │
│     └─ Waterveiligheid: ≤1:100.000 sterftekans in 2050          │
│                                                                 │
│  NIVEAU 3: PROVINCIE - Omgevingsverordening (art. 2.12-2.13a)   │
│  └─ Verplicht: regionale waterkeringen, geluidproductieplafonds │
│     provinciale wegen/spoorwegen                                │
│     └─ Mits binnen grenzen art. 2.3 lid 2 (subsidiariteit)      │
│                                                                 │
│  NIVEAU 4: GEMEENTE - Omgevingsplan (art. 2.11-2.11a)           │
│  └─ Verplicht: geluidproductieplafonds industrieterreinen       │
│     └─ Geen aanvulling/afwijking van hogere niveaus             │
│        TENZIJ hoger niveau dit expliciet toestaat               │
└─────────────────────────────────────────────────────────────────┘
```

### NEW PATTERN: Taaktoedeling Water (Cross-Afdeling)

```
┌─────────────────────────────────────────────────────────────────┐
│  WATERTAKEN VERDELING (Art. 2.16-2.19, 2.38-2.42)               │
│                                                                 │
│  GEMEENTE (art. 2.16):                                          │
│  ├─ Hemelwater (inzameling)                                     │
│  ├─ Grondwater (maatregelen openbaar gebied)                    │
│  └─ Riolering (inzameling & transport)                          │
│                                                                 │
│  WATERSCHAP (art. 2.17):                                        │
│  ├─ Beheer watersystemen (regionale wateren)                    │
│  └─ Zuivering stedelijk afvalwater                              │
│      └─ Kan bij gezamenlijk besluit naar gemeente (lid 3)       │
│                                                                 │
│  PROVINCIE (art. 2.18):                                         │
│  ├─ Coördinatie gemeente/waterschap                             │
│  ├─ Toezicht waterschapsbeheer (excl. primaire keringen)        │
│  ├─ Zwemwaterbeheer                                             │
│  └─ Toedeling regionale wateren aan waterschappen               │
│                                                                 │
│  RIJK (art. 2.19):                                              │
│  ├─ Rijkswateren (beheer)                                       │
│  ├─ Kustlijnbeheer                                              │
│  ├─ Toezicht primaire waterkeringen                             │
│  └─ Technische leidraden primaire waterkeringen                 │
│                                                                 │
│  BIJZONDERE INSTRUMENTEN (art. 2.39-2.42):                      │
│  ├─ Legger (technisch beheerregister)                           │
│  ├─ Peilbesluit (waterstanden/bandbreedten)                     │
│  └─ Verdringingsreeks (rangorde bij waterschaarste)             │
└─────────────────────────────────────────────────────────────────┘
```

### NEW PATTERN: Stikstof Mechanisme (Art. 2.15a + 2.46)

```
┌─────────────────────────────────────────────────────────────────┐
│  STIKSTOFMECHANISME (Art. 2.15a + 2.46)                         │
│                                                                 │
│  OMGEVINGSWAARDEN (art. 2.15a):                                 │
│  ├─ 2025: 40% areaal onder KDW                                  │
│  ├─ 2030: 50% areaal onder KDW                                  │
│  ├─ 2035: 74% areaal onder KDW                                  │
│  └─ Type: RESULTAATSVERPLICHTING (moet gehaald worden)          │
│                                                                 │
│  STIKSTOFDEPOSITIERUIMTE (art. 2.46):                           │
│  ├─ Registratie door Minister (of aangewezen bestuursorgaan)    │
│  ├─ Voorwaarde: AANVULLENDE maatregelen (additionaliteit)       │
│  ├─ Toedeling bij vergunningverlening Natura 2000-activiteit    │
│  └─ Ruimte ≥ toename depositie (strikte toets)                  │
│                                                                 │
│  KOPPELING MET HOOFDSTUK 5:                                     │
│  └─ Natura 2000-activiteit = vergunningplichtig (art. 5.1)      │
│      └─ Stikstofdepositie = toetsingscriterium                  │
└─────────────────────────────────────────────────────────────────┘
```

### Cross-Chapter Connections Discovered

```
┌─────────────────────────────────────────────────────────────────┐
│  CHAPTER 2 HUB-FUNCTIE                                          │
│                                                                 │
│  Art. 2.3 (subsidiariteit) ◄──────────────────────────────────► │
│  ├─ Art. 2.22 (instructieregels provincie) - "met inachtneming" │
│  ├─ Art. 2.24 (instructieregels Rijk) - "met inachtneming"      │
│  ├─ Art. 2.12 (omgevingswaarden prov) - "met inachtneming"      │
│  └─ Art. 2.14 (omgevingswaarden Rijk) - "met inachtneming"      │
│                                                                 │
│  Art. 2.15a (stikstof) ◄──────────────────────────────────────► │
│  ├─ Art. 2.46 (stikstofdepositieruimte)                         │
│  ├─ Art. 3.9 (programma stikstof)                               │
│  └─ Art. 5.1 (Natura 2000-vergunning)                           │
│                                                                 │
│  Art. 2.44 (natuurgebieden) ◄─────────────────────────────────► │
│  ├─ Art. 5.1 (Natura 2000-activiteit vergunning)                │
│  ├─ Art. 2.18 (provinciale natuurtaak)                          │
│  └─ Art. 2.19 (rijksnatuurtaak)                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Module Status Update (2026-01-29)

| Module | Status | Schema |
|--------|--------|--------|
| ch2-afd2.1-v2-atomic.yaml | ✅ Complete | V2 |
| ch2-afd2.2-v2-atomic.yaml | ✅ Complete | V2 |
| ch2-afd2.3-v2-atomic.yaml | ✅ Complete | V2 |
| ch2-afd2.4-v2-atomic.yaml | ✅ Complete | V2 |
| ch2-afd2.5-v2-atomic.yaml | ✅ Complete | V2 |
| ch2-afd2.6-v2-atomic.yaml | ✅ Complete | V2 |

**Chapter 2 Coverage**: 37 articles (2.1-2.46, excluding 2.22-2.37 which was already V2)

---

## CHAPTER 16 V2 UPGRADE (2026-01-29)

### Progress Summary

Chapter 16 (Procedures) contains 14 afdelingen with 174 articles total. V2 upgrade in progress.

### Key Patterns Discovered

#### 1. Coördinatie Mechanisme (Art. 16.7-16.8)

```
┌─────────────────────────────────────────────────────────────────┐
│              AWB AFD 3.5 COÖRDINATIE                            │
├─────────────────────────────────────────────────────────────────┤
│  Verplichte coördinatie (art. 16.7):                            │
│  ├─ Water + andere activiteiten (gelijktijdig ingediend)        │
│  ├─ Milieu + water (verplicht gelijktijdig ex art. 5.7 lid 4)   │
│  └─ Projectbesluit uitvoeringsbesluiten                         │
│                                                                 │
│  Facultatieve koepelcoördinatie (art. 16.8):                    │
│  └─ Kan worden uitgebreid naar plan + programma + vergunning    │
└─────────────────────────────────────────────────────────────────┘
```

#### 2. Advies vs Instemming Hiërarchie (Art. 16.15-16.18)

| Instrument | Bindendheid | Gevolg ontbreken | Voorbeeld |
|------------|-------------|------------------|-----------|
| **Advies** | Lichter | Besluit kan toch genomen worden | Art. 16.15 |
| **Instemming** | Zwaarder | Besluit kan NIET zonder | Art. 16.16 |

**Kritiek: GEEN fictieve instemming** (art. 16.18 lid 2) - bij niet tijdig beslissen wordt instemming NIET geacht verleend.

#### 3. Reactieve Aanwijzing (Art. 16.21)

```
Gemeente stelt omgevingsplan vast
           ↓
  GS heeft zienswijze ingediend
           ↓
 Zienswijze niet/niet volledig overgenomen
           ↓
     GS kan onderdeel UITSLUITEN
           ↓
┌─────────────────────────────────────────┐
│ DUBBELE VOORWAARDE:                     │
│ 1. Nodig voor evenwichtige toedeling    │
│ 2. Strijd met provinciaal belang        │
│    (aangegeven in openbaar document)    │
└─────────────────────────────────────────┘
           ↓
  Ultimum remedium: motiveren waarom
  andere bevoegdheden niet volstaan
```

#### 4. Plan-MER vs Project-MER Onderscheid (Art. 16.34-16.53b)

| Aspect | Plan-MER (§ 16.4.1) | Project-MER (§ 16.4.2) |
|--------|---------------------|------------------------|
| **Wie maakt** | Bevoegd gezag | Initiatiefnemer |
| **Commissie m.e.r.** | Verplicht advies | Facultatief |
| **Trigger** | Kader voor projecten | Concrete activiteit |
| **Alternatieven** | Strategische keuzes | Projectalternatieven |

#### 5. Passende Beoordeling (Art. 16.53c)

```
Plan/project met mogelijk significante effecten op Natura 2000
                        ↓
            Passende beoordeling VERPLICHT
                        ↓
         Koppeling met art. 16.36 lid 2:
         Als passende beoordeling → plan-MER ook verplicht
```

### Module Status (Chapter 16 V2)

| Module | Status | Articles | Key Content |
|--------|--------|----------|-------------|
| ch16-afd16.1-v2-atomic.yaml | ✅ Complete | 16.1-16.6 | Elektronisch verkeer, DSO, houdbaarheid gegevens |
| ch16-afd16.2-v2-atomic.yaml | ✅ Complete | 16.7-16.21 | Coördinatie, advies/instemming, reactieve aanwijzing |
| ch16-afd16.3-v2-atomic.yaml | ✅ Complete | 16.22-16.33l | Totstandkomingsprocedures, Awb 3.4 |
| ch16-afd16.4-v2-atomic.yaml | ✅ Complete | 16.34-16.53b | Milieueffectrapportage (plan-MER + project-MER) |
| ch16-afd16.4a-v2-atomic.yaml | ✅ Complete | 16.53c | Passende beoordeling Natura 2000 |
| ch16-afd16.5-v2-atomic.yaml | ✅ Complete | 16.54-16.68 | Omgevingsvergunning procedure, loket, lex silencio |
| ch16-afd16.6-16.6a-v2-atomic.yaml | ✅ Complete | 16.70-16.76 | Projectprocedure, kostenverhaalsbeschikking |
| ch16-afd16.7-v2-atomic.yaml | ✅ Complete | 16.77-16.90 | Beslistermijn, inwerkingtreding, beroep |
| ch16-afd16.8-16.14-v2-atomic.yaml | ✅ Complete | 16.91-16.140 | Domain-specific (onteigening, landinrichting) |

**Articles completed V2**: 174 (of 174 total) - CHAPTER 16 COMPLETE

---

## NEW PATTERNS FROM V2 EXTRACTIONS (2026-01-29)

### Pattern 12: VOORBESCHERMING HIËRARCHIE (from Afd 4.2)

Art. 4.15-4.19b implements **voorbereidingsbescherming** - protective measures before formal planning is complete:

```
┌─────────────────────────────────────────────────────────────────┐
│              VOORBESCHERMING HIËRARCHIE                         │
│                                                                 │
│  ART. 4.16: PROVINCIE OVER GEMEENTE                             │
│  ├─ PS kan: activiteiten verbieden of voorwaarden stellen       │
│  ├─ Scope: "ter bescherming van provinciale belangen"           │
│  └─ Effect: Omgevingsplan wijziging AUTOMATISCH bij             │
│             vaststelling omgevingsverordening                   │
│                                                                 │
│  ART. 4.17: RIJK OVER ALLEN                                     │
│  ├─ Minister kan: activiteiten verbieden of voorwaarden stellen │
│  ├─ Scope: "ter bescherming van nationale belangen"             │
│  └─ Effect: Omgevingsplan/verordening wijziging AUTOMATISCH     │
│                                                                 │
│  ART. 4.18-4.19: PROCEDUREEL                                    │
│  ├─ 4.18: Bekendmaking door kennisgeving                        │
│  └─ 4.19: Verval na 2 jaar (verlenging 2 jaar mogelijk)         │
│                                                                 │
│  HIËRARCHIE: Rijk > Provincie > Gemeente                        │
│  Hogere overheid kan lagere instrumenten DOORBREKEN             │
└─────────────────────────────────────────────────────────────────┘
```

### Pattern 13: ZAAKSGEBONDENHEID (from § 5.1.4)

Art. 5.37 establishes **zaaksgebondenheid** - the permit follows the activity, not the person:

```
┌─────────────────────────────────────────────────────────────────┐
│              ZAAKSGEBONDENHEID (Art. 5.37)                       │
│                                                                 │
│  NORMADRESSAAT (lid 1):                                         │
│  └─ "degene die de activiteit verricht"                         │
│      NOT: de aanvrager of vergunninghouder                      │
│                                                                 │
│  PRAKTISCH EFFECT:                                              │
│  ├─ Overdracht eigendom → vergunning gaat mee                   │
│  ├─ Geen aparte overdrachtsvergunning nodig                     │
│  └─ Nieuwe eigenaar = nieuwe normadressaat                      │
│                                                                 │
│  UITZONDERING (Art. 5.37a):                                     │
│  └─ Bij meervoudige activiteiten kan BG verantwoordelijkheden   │
│     verdelen tussen meerdere partijen                           │
│                                                                 │
│  VERGELIJK: Zaaksgebondenheid vs persoonsgebondenheid           │
│  ├─ Zaaksgebonden: omgevingsvergunning (Ow)                     │
│  └─ Persoonsgebonden: rijbewijs, paspoort (andere wetten)       │
└─────────────────────────────────────────────────────────────────┘
```

### Pattern 14: LIFECYCLE PATTERN (from § 5.1.5)

Art. 5.38-5.43 defines the **complete lifecycle** of an omgevingsvergunning:

```
┌─────────────────────────────────────────────────────────────────┐
│              VERGUNNING LIFECYCLE                                │
│                                                                 │
│  1. ACTUALISERING (Art. 5.38)                                   │
│     └─ Periodieke review van voorschriften                      │
│        └─ Trigger: tijdsverloop, nieuwe inzichten               │
│                                                                 │
│  2. WIJZIGING (Art. 5.39-5.40)                                  │
│     ├─ Art. 5.39: IMPERATIEF (MOET wijzigen/intrekken)          │
│     │   ├─ Strijdigheid met wettelijk voorschrift               │
│     │   ├─ Niet naleven voorschriften                           │
│     │   └─ BBT/BKE geëvolueerd                                  │
│     └─ Art. 5.40: FACULTATIEF (KAN wijzigen/intrekken)          │
│         ├─ Op verzoek vergunninghouder                          │
│         ├─ Nieuwe inzichten                                     │
│         └─ 3 jaar niet-gebruik                                  │
│                                                                 │
│  3. INTREKKING (Art. 5.39-5.40)                                 │
│     └─ Volgt zelfde imperatief/facultatief onderscheid          │
│                                                                 │
│  4. REVISIEVERGUNNING (Art. 5.43)                               │
│     └─ Consolidatie: vervangt meerdere vergunningen             │
│        door één coherente vergunning                            │
└─────────────────────────────────────────────────────────────────┘
```

**Key distinction discovered**:

| Type | Artikel | Signaalwoord | Betekenis |
|------|---------|--------------|-----------|
| **Imperatief** | 5.39 | "wijzigt", "trekt in" | MOET handelen |
| **Facultatief** | 5.40 | "kan wijzigen", "kan intrekken" | MAG handelen |

### Pattern 15: HUB-AND-SPOKE 4.3 met 27 Internationale Verplichtingen (from Afd 4.3)

Art. 4.3 functions as **central activity hub** with Art. 4.20-4.36 as **activity-specific spokes**:

```
┌─────────────────────────────────────────────────────────────────┐
│              HUB-AND-SPOKE PATTERN (Ch4)                         │
│                                                                 │
│                         ART. 4.3 (HUB)                          │
│                    17 activiteitcategorieën                     │
│                              │                                  │
│      ┌───────────┬───────────┼───────────┬───────────┐         │
│      │           │           │           │           │         │
│      ▼           ▼           ▼           ▼           ▼         │
│   4.20-4.21   4.22-4.25   4.26-4.27   4.28-4.31   4.32-4.36   │
│   Int'l       Bouw        Water       Milieu      Natuur      │
│   27 verpl.   activiteit  activiteit  belastend   bescherming │
│                                                                 │
│  ART. 4.20: INTERNATIONALE VERPLICHTINGEN (27 stuks!)          │
│  ├─ EU Richtlijnen: 23 stuks                                   │
│  │   ├─ Seveso III (2012/18/EU)                                │
│  │   ├─ IPPC/IED (2010/75/EU)                                  │
│  │   ├─ Kaderrichtlijn Water (2000/60/EG)                      │
│  │   ├─ Habitatrichtlijn (92/43/EEG)                           │
│  │   └─ ... en 19 andere                                       │
│  └─ Internationale Verdragen: 4 stuks                          │
│      ├─ OSPAR                                                   │
│      ├─ London Protocol                                         │
│      ├─ MARPOL                                                  │
│      └─ BWM-verdrag                                             │
│                                                                 │
│  SPOKE ARTIKELEN:                                               │
│  ├─ 4.21: bouwwerken (veiligheid, gezondheid, duurzaamheid)    │
│  ├─ 4.22: infrastructurele werken                              │
│  ├─ 4.23: installaties (IED-scope)                             │
│  ├─ 4.24: milieubelastende activiteiten                        │
│  ├─ 4.26-4.27: wateractiviteiten                               │
│  ├─ 4.28-4.31: beperkingengebiedactiviteiten                   │
│  └─ 4.32-4.36: Natura 2000, flora/fauna                        │
└─────────────────────────────────────────────────────────────────┘
```

### Pattern 16: LOKETFUNCTIE EN TERMIJNSTART (from Afd 16.5)

Art. 16.54-16.56 establishes the **loket** (service desk) principle:

```
┌─────────────────────────────────────────────────────────────────┐
│              LOKETFUNCTIE (Art. 16.54)                           │
│                                                                 │
│  INDIENINGSPUNT (wie ontvangt aanvraag):                        │
│  ├─ Gemeente: altijd toegestaan                                 │
│  ├─ Waterschap: bij wateractiviteiten                           │
│  └─ OOK ALS zij niet bevoegd gezag zijn!                        │
│                                                                 │
│  KRITISCH: LOKETDATUM = TERMIJNSTART                            │
│  ├─ Art. 16.54 lid 1: "Loket zendt door naar BG"               │
│  └─ Termijn begint bij ontvangst LOKET, niet BG!               │
│                                                                 │
│  PRAKTISCH EFFECT:                                              │
│  ┌────────────────────────────────────────────────────┐         │
│  │  Aanvrager → Gemeente → (doorsturen) → Provincie   │         │
│  │              ↑                                      │         │
│  │              DAG 0 (termijn start)                 │         │
│  └────────────────────────────────────────────────────┘         │
│                                                                 │
│  DOORZENDPLICHT:                                                │
│  └─ Loket MOET onverwijld doorsturen naar bevoegd gezag         │
└─────────────────────────────────────────────────────────────────┘
```

### Pattern 17: PROCEDURE DUALITEIT (from § 16.5.2-16.5.3)

Art. 16.62-16.65 establishes **two tracks** for permit procedures:

```
┌─────────────────────────────────────────────────────────────────┐
│              PROCEDURE DUALITEIT                                 │
│                                                                 │
│  ART. 16.62: DEFAULT + TENZIJ                                   │
│  ├─ DEFAULT: Reguliere procedure (§ 16.5.2)                     │
│  │   ├─ Termijn: 8 weken (+ 6 weken verlenging)                 │
│  │   ├─ Met instemming: 12 weken (+ 6 weken)                    │
│  │   └─ Geen zienswijzeprocedure                                │
│  │                                                              │
│  └─ TENZIJ: Uitgebreide procedure (§ 16.5.3)                    │
│      ├─ Awb afdeling 3.4 van toepassing                         │
│      ├─ Wel zienswijzeprocedure                                 │
│      ├─ 6 maanden + 6 weken verlenging                          │
│      └─ Bij AMvB aangewezen gevallen                            │
│                                                                 │
│  KRITIEK: LEX SILENCIO EXCLUSIE (Art. 16.64 lid 4)              │
│  ├─ Awb § 4.1.3.3 NIET van toepassing                           │
│  ├─ Geen vergunning van rechtswege bij termijnoverschrijding    │
│  └─ Bewuste ontwerpkeuze Omgevingswet                           │
│                                                                 │
│  RATIO:                                                          │
│  ├─ Milieu/natuur te belangrijk voor automatische verlening     │
│  └─ Initiatiefnemer kan dwangsom vorderen bij overschrijding    │
└─────────────────────────────────────────────────────────────────┘
```

### Pattern 18: BBT-KOPPELING (from § 5.1.4-5.1.5)

Art. 5.38-5.39 links permits to **Best Beschikbare Technieken** (BBT):

```
┌─────────────────────────────────────────────────────────────────┐
│              BBT-KOPPELING                                       │
│                                                                 │
│  ACTUALISATIEPLICHT (Art. 5.38):                                │
│  └─ Voorschriften moeten actueel blijven t.a.v. BBT             │
│                                                                 │
│  WIJZIGINGSPLICHT (Art. 5.39 lid 2):                            │
│  ├─ (a) Strijdigheid met wettelijk voorschrift                  │
│  ├─ (b) BBT/BKE is geëvolueerd                                  │
│  └─ (c) Nieuwe wetenschappelijke inzichten                      │
│                                                                 │
│  DOORWERKING:                                                    │
│  ├─ EU publiceert BREF-documenten                               │
│  ├─ BREF → BBT-conclusies                                       │
│  ├─ BBT-conclusies → wijziging Bal                              │
│  └─ Bal wijziging → vergunningvoorschriften moeten volgen       │
│                                                                 │
│  TERMIJN: 4 jaar na publicatie BBT-conclusies                   │
│  └─ Vergunning moet zijn aangepast                              │
└─────────────────────────────────────────────────────────────────┘
```

---

## MODULE STATUS V2 (Final Update 2026-01-29)

### Chapter 4 V2 Complete

| Module | Status | Key Patterns |
|--------|--------|--------------|
| ch4-afd4.1-v2-atomic.yaml | ✅ Complete | 4.3 hub, 4.9 default+tenzij, Ch4↔Ch5 parallel |
| ch4-afd4.2-4.3-v2-atomic.yaml | ✅ Complete | Voorbescherming hiërarchie, hub-and-spoke 4.3, 27 int'l verplichtingen |

### Chapter 5 V2 Complete

| Module | Status | Key Patterns |
|--------|--------|--------------|
| ch5-par5.1.1-v2-atomic.yaml | ✅ Complete | TENZIJ vs VOOR ZOVER, handhavingshiërarchie |
| ch5-par5.1.2-v2-atomic.yaml | ✅ Complete | Subsidiariteitstrap, beslisboom |
| ch5-par5.1.3-v2-atomic.yaml | ✅ Complete | Hub-spoke beoordelingsregels |
| ch5-par5.1.4-5.1.5-v2-atomic.yaml | ✅ Complete | Zaaksgebondenheid, lifecycle pattern, imperatief vs facultatief, BBT-koppeling |
| ch5-afd5.2-v2-atomic.yaml | ✅ Complete | Projectbesluit integraal, doorbreking, hiërarchie |

### Chapter 16 V2 Complete

| Module | Status | Key Patterns |
|--------|--------|--------------|
| ch16-afd16.1-v2-atomic.yaml | ✅ Complete | DSO, houdbaarheid gegevens |
| ch16-afd16.2-v2-atomic.yaml | ✅ Complete | Advies vs instemming, reactieve aanwijzing |
| ch16-afd16.3-v2-atomic.yaml | ✅ Complete | UOV-standaard, actio popularis |
| ch16-afd16.4-v2-atomic.yaml | ✅ Complete | Plan-MER vs project-MER |
| ch16-afd16.4a-v2-atomic.yaml | ✅ Complete | Passende beoordeling |
| ch16-afd16.5-v2-atomic.yaml | ✅ Complete | Loketfunctie, procedure dualiteit, lex silencio exclusie |
| ch16-afd16.6-16.6a-v2-atomic.yaml | ✅ Complete | Projectprocedure UOV, kostenverhaal aanhouding |
| ch16-afd16.7-v2-atomic.yaml | ✅ Complete | Inwerkingtreding spectrum, beroepsbundeling |
| ch16-afd16.8-16.14-v2-atomic.yaml | ✅ Complete | Domain-specific (onteigening, landinrichting) |

---
