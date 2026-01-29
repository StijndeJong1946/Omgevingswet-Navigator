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
| ch5-par5.1.4-5.1.5-atomic.yaml | ✅ Complete | imperatief vs facultatief |
| ch5-afd5.2-atomic.yaml | ✅ Complete | projectbesluit = integraal |
| ch4-afd4.1-atomic.yaml | ✅ Complete | 4.3 hub, 4.9 default+tenzij |
| ch4-afd4.2-4.3-atomic.yaml | ✅ Complete | Ch4 ↔ Ch5 parallel |
| ch16-afd16.5-atomic.yaml | ✅ Complete | procedure duality, loket, lex silencio |
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
| ch5-par5.1.4-5.1.5-atomic.yaml | ✅ Complete | imperatief vs facultatief |
| ch5-afd5.2-atomic.yaml | ✅ Complete | projectbesluit = integraal |
| ch4-afd4.1-atomic.yaml | ✅ Complete | 4.3 hub, 4.9 default+tenzij |
| ch4-afd4.2-4.3-atomic.yaml | ✅ Complete | Ch4 ↔ Ch5 parallel |
| ch16-afd16.1-atomic.yaml | ✅ Complete | houdbaarheid data, DSO |
| ch16-afd16.2-atomic.yaml | ✅ Complete | advies vs instemming, reactieve interventie |
| ch16-afd16.3-atomic.yaml | ✅ Complete | UOV-standaard, actio popularis |
| ch16-afd16.4-atomic.yaml | ✅ Complete | dual-track MER, tiering, Commissie asymmetrie |
| ch16-afd16.5-atomic.yaml | ✅ Complete | procedure duality, loket, lex silencio |
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
| ch5-par5.1.4-5.1.5-atomic.yaml | ✅ Complete | imperatief vs facultatief |
| ch5-afd5.2-atomic.yaml | ✅ Complete | projectbesluit = integraal |
| ch4-afd4.1-atomic.yaml | ✅ Complete | 4.3 hub, 4.9 default+tenzij |
| ch4-afd4.2-4.3-atomic.yaml | ✅ Complete | Ch4 ↔ Ch5 parallel |
| ch16-afd16.1-atomic.yaml | ✅ Complete | houdbaarheid data, DSO |
| ch16-afd16.2-atomic.yaml | ✅ Complete | advies vs instemming, reactieve interventie |
| ch16-afd16.3-atomic.yaml | ✅ Complete | UOV-standaard, actio popularis |
| ch16-afd16.4-atomic.yaml | ✅ Complete | dual-track MER, tiering, Commissie asymmetrie |
| ch16-afd16.4a-atomic.yaml | ✅ Complete | passende beoordeling, Habitatrichtlijn |
| ch16-afd16.5-atomic.yaml | ✅ Complete | procedure duality, loket, lex silencio |
| ch16-afd16.6-16.6a-atomic.yaml | ✅ Complete | projectprocedure, kostenverhaal |
| ch16-afd16.7-atomic.yaml | ✅ Complete | inwerkingtreding spectrum |
| ch16-afd16.8-16.14-atomic.yaml | ✅ Complete | domain-specific (voorkeursrecht, onteigening, etc.) |
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
| ch5-par5.1.4-5.1.5-atomic.yaml | ✅ Complete | imperatief vs facultatief |
| ch5-afd5.2-atomic.yaml | ✅ Complete | projectbesluit = integraal |
| ch4-afd4.1-atomic.yaml | ✅ Complete | 4.3 hub, 4.9 default+tenzij |
| ch4-afd4.2-4.3-atomic.yaml | ✅ Complete | Ch4 ↔ Ch5 parallel |
| ch16-afd16.1-atomic.yaml | ✅ Complete | houdbaarheid data, DSO |
| ch16-afd16.2-atomic.yaml | ✅ Complete | advies vs instemming, reactieve interventie |
| ch16-afd16.3-atomic.yaml | ✅ Complete | UOV-standaard, actio popularis |
| ch16-afd16.4-atomic.yaml | ✅ Complete | dual-track MER, tiering, Commissie asymmetrie |
| ch16-afd16.4a-atomic.yaml | ✅ Complete | passende beoordeling, Habitatrichtlijn |
| ch16-afd16.5-atomic.yaml | ✅ Complete | procedure duality, loket, lex silencio |
| ch16-afd16.6-16.6a-atomic.yaml | ✅ Complete | projectprocedure, kostenverhaal |
| ch16-afd16.7-atomic.yaml | ✅ Complete | inwerkingtreding spectrum |
| ch16-afd16.8-16.14-atomic.yaml | ✅ Complete | domain-specific (voorkeursrecht, onteigening, etc.) |
| ch2-afd2.1-atomic.yaml | ✅ Complete | subsidiariteit, doelgebondenheid, 19 belangen |
| ch2-afd2.2-atomic.yaml | ✅ Complete | one-plan-principle, exclusiviteit |
| ch2-afd2.3-atomic.yaml | ✅ Complete | omgevingswaarden, resultaat vs inspanning, stikstof |
| ch2-afd2.4-atomic.yaml | ✅ Complete | taaktoedeling per niveau, beperkingengebieden |
| ch2-afd2.5-atomic.yaml | ✅ Complete | instructieregels vs instructies, indeplaatstreding |
| ch2-afd2.6-atomic.yaml | ✅ Complete | water, natuur, stikstofdepositieruimte |
| **ch18-atomic.yaml** | ✅ Complete | wie verleent=handhaaft, omgevingsdiensten, boetecategorieën |

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
| ch5-par5.1.4-5.1.5-atomic.yaml | ✅ Complete | imperatief vs facultatief |
| ch5-afd5.2-atomic.yaml | ✅ Complete | projectbesluit = integraal |
| ch4-afd4.1-atomic.yaml | ✅ Complete | 4.3 hub, 4.9 default+tenzij |
| ch4-afd4.2-4.3-atomic.yaml | ✅ Complete | Ch4 ↔ Ch5 parallel |
| ch16-afd16.1-atomic.yaml | ✅ Complete | houdbaarheid data, DSO |
| ch16-afd16.2-atomic.yaml | ✅ Complete | advies vs instemming, reactieve interventie |
| ch16-afd16.3-atomic.yaml | ✅ Complete | UOV-standaard, actio popularis |
| ch16-afd16.4-atomic.yaml | ✅ Complete | dual-track MER, tiering, Commissie asymmetrie |
| ch16-afd16.4a-atomic.yaml | ✅ Complete | passende beoordeling, Habitatrichtlijn |
| ch16-afd16.5-atomic.yaml | ✅ Complete | procedure duality, loket, lex silencio |
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
| **ch3-atomic.yaml** | ✅ Complete | omgevingsvisie, programma's, programmatische aanpak, stikstofprogramma |

### CHAPTER 3 COMPLETE

All 2 afdelingen of Chapter 3 (Strategische instrumenten) have been extracted:

| Afdeling | Articles | Module | Key Patterns |
|----------|----------|--------|--------------|
| 3.1 | 3.1-3.3 | ch3-atomic | omgevingsvisie verplicht op elk niveau |
| 3.2 | 3.4-3.19 | ch3-atomic | verplichte/onverplichte programma's, programmatische aanpak |

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

## CHAPTER 1 - ALGEMENE BEPALINGEN (Extraction 2026-01-29)

### Structure Overview

| Afdeling | Articles | Function | Key Pattern |
|----------|----------|----------|-------------|
| **1.1** | 1.1 | Begripsbepalingen | Bijlage-systematiek |
| **1.2** | 1.2-1.5 | Toepassingsgebied en doelen | Dubbele doelstelling |
| **1.3** | 1.6-1.8 | Zorg fysieke leefomgeving | Zorgplicht-hiërarchie |

### Art. 1.2 - Fysieke leefomgeving (10 onderdelen)

bouwwerken | infrastructuur | watersystemen | water | bodem | lucht | landschappen | natuur | cultureel erfgoed | werelderfgoed

### Art. 1.3 - Dubbele doelstelling

| Pool | Elementen |
|------|-----------|
| **a. BESCHERMEN** | veilig, gezond, omgevingskwaliteit, intrinsieke waarde natuur |
| **b. BENUTTEN** | doelmatig beheren/gebruiken/ontwikkelen, maatschappelijke behoeften |

### Zorgplicht-hiërarchie

| Artikel | Type | Handhaafbaar |
|---------|------|--------------|
| 1.6 | Algemene zorgplicht | Indirect |
| 1.7 | Voorkomen → beperken → stoppen | Direct |
| 1.7a | Absoluut verbod (aanzienlijk) | Strafrecht |

---

## Module Status (Updated with Ch1)

| Module | Status |
|--------|--------|
| **ch1-atomic.yaml** | ✅ Complete |
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
| **ch1-atomic.yaml** | ✅ Complete |
| ch2-afd2.1-2.6-atomic.yaml (6 files) | ✅ Complete |
| ch3-atomic.yaml | ✅ Complete |
| ch4-afd4.1-4.3-atomic.yaml (2 files) | ✅ Complete |
| ch5-*.yaml (5 files) | ✅ Complete |
| ch16-*.yaml (8 files) | ✅ Complete |
| ch18-atomic.yaml | ✅ Complete |
| ch19-atomic.yaml | ✅ Complete |
| ch20-atomic.yaml | ✅ Complete |
| **ch22-ch23-atomic.yaml** | ✅ Complete |

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
| **Ch10** | Gedoogplichten | 10.1-10.30 | Toleration obligations |
| **Ch11** | Landinrichting | 11.1-11.97 | Land consolidation |
| **Ch12** | Onteigening | 12.1-12.41 | Expropriation |

### Instrument Hierarchy (licht → zwaar)

| # | Instrument | Effect | Eigendom |
|---|------------|--------|----------|
| 1 | **Voorkeursrecht** (Ch9) | Overheid krijgt eerste koopoptie | blijft bij eigenaar |
| 2 | **Gedoogplicht** (Ch10) | Eigenaar moet activiteit toestaan | blijft bij eigenaar |
| 3 | **Landinrichting** (Ch11) | Kavelruil ter verbetering inrichting | ruil tussen eigenaren |
| 4 | **Onteigening** (Ch12) | Gedwongen eigendomsovergang | gaat naar overheid |

### Key Patterns

**Art. 9.1 - Voorkeursrecht vestiging**: Drie grondslagen (omgevingsplan > visie/programma > beschikking)

**Art. 10.2 - Gedoogplichten van rechtswege**: Automatische gedoogplicht voor wegen, waterstaatswerken, nutsleidingen

**Art. 12.2 - Onteigening grondslag**: Uitvoering omgevingsplan, omgevingsvisie, of projectbesluit

**Art. 12.30 - Volledige schadeloosstelling**: Waarde + waardevermindering overblijvende + bijkomende schade

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
