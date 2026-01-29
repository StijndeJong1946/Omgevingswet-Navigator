# Atomic Legal Logic Extraction Schema v2

## Principle

> Extract what the law SAYS, not what we INTERPRET.

Each artikel is captured at atomic level with full structural fidelity. The mapping guide is updated based on patterns that EMERGE from extraction, not imposed beforehand.

---

## Schema Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-01-28 | Initial schema |
| v2 | 2026-01-29 | Added: bron_path traceability, lid-level logica, conditie typing (tenzij/voor_zover distinction), afsluiting capture, sub_onderdelen nesting, handhaving_categorie |

---

## Atomic Unit: Artikel (v2)

```yaml
artikel_X.Y:
  # === IDENTIFICATION ===
  nummer: "X.Y"
  titel: "(exact title from source)"
  bron_path: "/HoofdstukX/AfdelingX.Y/ParagraafX.Y.Z/ArtikelX.Y"  # NEW: XML path
  inwerking: "YYYY-MM-DD"

  # === STRUCTURE (as written) ===
  leden:
    1:  # Changed: use nummer as key, not array
      bron_path: "/path/to/Lid1"  # NEW: traceability
      structuur:
        aanhef: "opening text before list"  # NEW
        onderdelen:
          a:
            tekst: "text"
            bron_path: "/path/to/Onderdeela"
            sub_onderdelen:  # NEW: nested lists
              1:
                tekst: "nested text"
                bron_path: "/path/to/Onderdeel1"
              2:
                tekst: "nested text"
        afsluiting: "closing text after list"  # NEW: captures TENZIJ/VOOR ZOVER

        # For simple leden without lists:
        volledige_tekst: "full text if no list structure"

      # === LID-LEVEL LOGIC (NEW) ===
      logica:
        type: "verbod" | "verplichting" | "machtiging" | "definitie" | "delegatie"
        norm: "exact legal norm statement"
        conditie:
          type: "tenzij" | "voor_zover" | "wanneer" | "indien" | "mits" | "in_afwijking_van" | "onverminderd" | "in_ieder_geval"
          tekst: "exact conditional phrase"
          effect: "what happens when condition applies"
          delegatie_richting: "who determines specifics"  # NEW
        default: "what applies without condition"  # NEW
        uitzondering: "what applies with condition"  # NEW
        handhaving_categorie: "ZWAAR" | "MIDDEL" | "LICHT"  # NEW: for art. 5.5 type

  # === ARTICLE-LEVEL FUNCTION ===
  functie:
    werkwoord: "verbiedt" | "verplicht" | "machtigt" | "definieert" | "bepaalt" | "delegeert" | "begrenst"
    object: "what is being regulated"
    subject: "who/what is addressed"
    bevoegd_gezag: "gemeente" | "provincie" | "waterschap" | "rijk"  # if applicable

  # === ARTICLE-LEVEL LOGIC SUMMARY (NEW) ===
  logica_samenvatting:
    narrative: |
      Multi-line explanation of how leden work together
      Critical for complex articles like 5.1, 5.5

  # === REFERENCES ===
  interne_refs:
    - naar: "artikel X.A"
      type: "grondslag" | "verwijzing" | "begrenzing" | "impliciet"  # NEW
      context: "exact phrase containing reference"
      bron_path: "/path/to/target"  # NEW

  externe_refs:
    - naar: "BWBR0043298"
      wet: "Bal"
      artikel: "3.1"  # NEW: specific article
      context: "exact phrase"

  # === DELEGATIONS ===
  delegeert:
    - type: "bij AMvB" | "bij ministeriële regeling" | "bij verordening" | "bij omgevingsplan" | "bij programma"
      naar: "identified target"
      voor: "what is delegated"
      actor: "who receives delegation"  # NEW
      mechanisme: "TENZIJ-vrijstelling" | "VOOR ZOVER-aanwijzing"  # NEW: critical distinction

  # === ACTORS (if mentioned) ===
  actoren:
    - actor: "gemeente" | "provincie" | "waterschap" | "rijk" | "minister" | "korpschef"
      rol: "what role in this artikel"
```

---

## Critical Distinction: TENZIJ vs VOOR ZOVER

**Discovered in Art. 5.1 extraction:**

| Keyword | Legal Effect | Default | Example |
|---------|--------------|---------|---------|
| **TENZIJ** | Exception to norm | Norm applies unless... | Art. 5.1 lid 1: forbidden UNLESS AMvB exempts |
| **VOOR ZOVER** | Scope of norm | Norm doesn't apply unless... | Art. 5.1 lid 2: forbidden FOR CASES WHERE AMvB designates |

This determines:
- Where burden of proof lies
- Whether activity is default-permitted or default-forbidden
- Direction of delegation (vrijstelling vs aanwijzing)

**Schema must capture:**
```yaml
conditie:
  type: tenzij  # or voor_zover
  effect: "AMvB kan gevallen VRIJSTELLEN"  # or AANWIJZEN
  delegatie_richting: "wet → AMvB vrijstelling"
default: "vergunningplichtig"
uitzondering: "vrijgesteld indien AMvB aanwijst"
```

---

## Condition Types (Expanded)

| Type | Dutch | Effect | Capture As |
|------|-------|--------|------------|
| tenzij | unless | Exception removes norm | `default` + `uitzondering` |
| voor_zover | insofar as | Scope activates norm | `default` + `uitzondering` |
| wanneer | when | Trigger condition | `conditie.tekst` |
| indien | if | Conditional application | `conditie.tekst` |
| mits | provided that | Requirement for norm | `conditie.tekst` |
| in_afwijking_van | notwithstanding | Override | `conditie.tekst` |
| onverminderd | without prejudice to | Cumulation | `conditie.tekst` |
| in_ieder_geval | in any case | Minimum requirement | `logica.type: verplichting` |

---

## Handhaving Hierarchy (from Art. 5.5)

Art. 5.5 creates a three-tier enforcement system. Capture with:

```yaml
logica:
  handhaving_categorie: ZWAAR | MIDDEL | LICHT
```

| Category | Protected Interests | Articles |
|----------|---------------------|----------|
| ZWAAR | veiligheid, gezondheid, milieu, waterkwaliteit, monumenten | 5.5 lid 1 |
| MIDDEL | overige activiteiten | 5.5 lid 2 |
| LICHT | jacht | 5.5 lid 3 |

---

## Extraction Process (Updated)

### Step 1: Read artikel from source XML
- Extract exact text
- Preserve structure (leden, onderdelen, sub_onderdelen)
- Capture bwb-ng-variabel-deel as bron_path
- Note aanhef and afsluiting separately from list items

### Step 2: Identify legal function per LID
- What verb drives this lid? (verbiedt, verplicht, machtigt, etc.)
- Is there a condition (tenzij, voor zover, etc.)?
- What is the default state?
- What is the exception/scope?

### Step 3: Trace references
- `<intref>` → internal cross-reference with bwb-ng-variabel-deel path
- `<extref>` → external law reference with bwb-id
- Note reference type (grondslag, verwijzing, begrenzing)

### Step 4: Find delegations
- "bij algemene maatregel van bestuur"
- "bij ministeriële regeling"
- "in de omgevingsverordening/waterschapsverordening/omgevingsplan"
- Note delegation mechanism (TENZIJ-vrijstelling vs VOOR ZOVER-aanwijzing)

### Step 5: Extract conditions with full logic
- Capture condition type
- Determine default vs exception
- Note delegatie_richting

### Step 6: Note actors
- Which bestuursorganen are mentioned?
- What role do they play?
- Who is bevoegd gezag?

### Step 7: Write article-level summary
- For complex articles with multiple leden
- Explain how leden interact
- Note critical distinctions

---

## Paragraaf-Level Analysis

After extracting all artikelen in a paragraaf, add:

```yaml
paragraaf_analyse:

  structuur:
    artikelen_count: N
    totaal_leden: N
    totaal_onderdelen: N

  patronen:
    pattern_name:
      beschrijving: "what pattern was observed"
      evidence: ["art X", "art Y"]

  relaties:
    intern:
      - van: "art X"
        naar: "art Y"
        type: "begrenzing" | "uitwerking" | "handhaving"
    extern:
      - naar: "art 2.3"
        context: "why referenced"

  routes:
    entry_points:
      - artikel: "X.Y"
        vraag: "navigation question this answers"
    exit_points:
      - naar: "next paragraaf or external"
        context: "when to route there"

mapping_guide_update:
  nieuwe_inzichten:
    insight_name:
      observatie: "what was discovered"
      implicatie: "what this means for navigation"

  schema_verbeteringen:
    - description of schema improvement
```

---

## Iteration Loop

```
READ paragraaf from source XML
    ↓
FOR EACH artikel in paragraaf:
    EXTRACT with v2 schema
    CAPTURE lid-level logica
    NOTE bron_paths for traceability
    ↓
ANALYZE paragraaf patterns
    ↓
UPDATE mapping guide with discoveries
    ↓
NEXT paragraaf → REPEAT
```

---

## What We DON'T Do

- ❌ Pre-categorize artikelen into "types"
- ❌ Impose navigation patterns before extraction
- ❌ Skip leden/onderdelen (capture full structure)
- ❌ Paraphrase legal text (preserve exact wording)
- ❌ Create "hub" designations before seeing the data
- ❌ Truncate afsluiting text (CRITICAL for tenzij/voor zover)
- ❌ Flatten nested onderdelen (preserve hierarchy)

---

## Extraction Priority

Based on mapping guide analysis and cross-reference density:

| Priority | Paragraaf | Articles | Reason |
|----------|-----------|----------|--------|
| P1 | **§ 5.1.1** | 5.1-5.6 | Core permit logic ✅ DONE v2 |
| P1 | **§ 5.1.2** | 5.7-5.16 | Bevoegd gezag routing ✅ DONE v2 |
| P1 | **§ 5.1.3** | 5.17-5.33a | Beoordelingsregels ✅ DONE v2 |
| P1 | **Afd 4.1** | 4.1-4.13a | General rules framework ✅ DONE v2 |
| P2 | **§ 16.5** | 16.54-16.68 | Procedure vergunning ✅ DONE v2 |
| P0 | **Afd 2.1** | 2.1-2.3 | Subsidiariteit, doelgebondenheid ✅ DONE v2 |
| P0 | **Afd 2.2** | 2.4-2.8 | Decentrale instrumenten (omgevingsplan etc) ✅ DONE v2 |
| P0 | **Afd 2.3** | 2.9-2.15a | Omgevingswaarden (incl. stikstof) ✅ DONE v2 |
| P0 | **Afd 2.4** | 2.16-2.21a | Taaktoedeling per bestuurslaag ✅ DONE v2 |
| P2 | **Afd 2.5** | 2.22-2.37 | Instructieregels & instructies ✅ DONE v2 |
| P1 | **Afd 2.6** | 2.38-2.46 | Bijzondere taken (water, natuur, stikstof) ✅ DONE v2 |
| P2 | **Ch 18** | 18.1-18.27 | Handhaving en uitvoering ✅ DONE v2 |
| P2 | **Afd 5.2** | 5.44-5.55 | Projectprocedure ✅ DONE v2 |
| P2 | **Ch 3** | 3.1-3.19 | Omgevingsvisies en programma's ✅ DONE v2 |
| P0 | **Ch 1** | 1.1-1.8 | Algemene bepalingen (scope, zorgplicht) ✅ DONE v2 |
| P3 | **Ch 9** | 9.1-9.22 | Voorkeursrecht (grondbeleid) ✅ DONE v2 |
| P3 | **Ch 10** | 10.1-10.29 | Gedoogplichten ✅ DONE v2 |
| P3 | **Ch 11** | 11.1-11.21 | Onteigening ✅ DONE v2 |
| P3 | **Ch 12** | 12.1-12.47 | Landinrichting ✅ DONE v2 |
| P3 | **Ch 8** | 8.1-8.5 | Populatiebeheer, schadebestrijding, jacht ✅ DONE v2 |
| P2 | **Ch 13** | 13.1-13.24 | Financiële bepalingen ✅ DONE v2 |
| P2 | **Ch 15** | 15.1-15.53 | Schade (nadeelcompensatie, gedoogplichten, onteigening) ✅ DONE v2 |
| P3 | **Ch 17** | 17.1-17.10 | Adviesorganen en adviseurs ✅ DONE v2 |
| P2 | **Ch 19** | 19.0-19.19 | Bevoegdheden in bijzondere omstandigheden ✅ DONE v2 |
| P2 | **Ch 20** | 20.1-20.30 | Monitoring en informatie ✅ DONE v2 |
| P2 | **Ch 22** | 22.1-22.22 | Overgangsrecht (transitie omgevingsplan, PAS-legalisering) ✅ DONE v2 |
| P3 | **Ch 23** | 23.1-23.11 | Overige en slotbepalingen (experimenten, evaluatie) ✅ DONE v2 |

---

## File Naming Convention

```
ch{X}-par{X.Y.Z}-v{N}-atomic.yaml
```

Example: `ch5-par5.1.1-v2-atomic.yaml`

- `ch{X}` = chapter number
- `par{X.Y.Z}` = paragraaf number (or `afd{X.Y}` for afdeling)
- `v{N}` = schema version used
- `atomic` = extraction type
