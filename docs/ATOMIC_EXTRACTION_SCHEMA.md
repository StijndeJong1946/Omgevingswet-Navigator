# Atomic Legal Logic Extraction Schema

## Principle

> Extract what the law SAYS, not what we INTERPRET.

Each artikel is captured at atomic level. The mapping guide is updated based on patterns that EMERGE from extraction, not imposed beforehand.

## Atomic Unit: Artikel

```yaml
artikel_X.Y:
  # === IDENTIFICATION ===
  nummer: "X.Y"
  titel: "(exact title from source)"
  afdeling: "X.Z"
  paragraaf: "X.Z.W" # if applicable

  # === STRUCTURE (as written) ===
  leden:
    - lid: 1
      tekst: "exact text"
      onderdelen: # if present
        - a: "text"
        - b: "text"
    - lid: 2
      tekst: "exact text"

  # === LEGAL FUNCTION (what does this artikel DO?) ===
  # Extracted from the text itself, not categorized
  functie:
    werkwoord: "verbiedt" | "verplicht" | "machtigt" | "definieert" | "bepaalt" | "delegeert" | ...
    object: "what is being regulated"
    subject: "who/what is addressed"

  # === REFERENCES (as written in the text) ===
  interne_refs:  # intref elements
    - naar: "artikel X.A"
      context: "exact phrase containing reference"

  externe_refs:  # extref elements
    - naar: "BWBR0043298"  # bwb-id
      wet: "Bal"
      context: "exact phrase"

  # === DELEGATIONS (explicit routing outward) ===
  delegeert:
    - type: "bij AMvB" | "bij ministeriële regeling" | "bij verordening" | "bij omgevingsplan"
      naar: "identified target if clear"
      voor: "what is delegated"
      tekst: "exact delegation phrase"

  # === CONDITIONS (decision logic in the text) ===
  voorwaarden:
    - type: "voor zover" | "indien" | "tenzij" | "mits" | "in afwijking van"
      tekst: "exact conditional phrase"
      effect: "what happens when condition applies"

  # === ACTORS (bestuursorganen mentioned) ===
  actoren:
    - actor: "gemeente" | "provincie" | "waterschap" | "rijk" | "minister"
      rol: "what role in this artikel"
      tekst: "exact mention"
```

## Extraction Process

### Step 1: Read artikel from source XML
Extract exact text, preserve structure (leden, onderdelen).

### Step 2: Identify legal function
What verb drives this artikel? (verbiedt, verplicht, machtigt, etc.)

### Step 3: Trace references
- `<intref>` → internal cross-reference
- `<extref>` → external law reference

### Step 4: Find delegations
Look for: "bij algemene maatregel van bestuur", "bij ministeriële regeling", "krachtens", etc.

### Step 5: Extract conditions
Look for: "voor zover", "indien", "tenzij", "mits", "in afwijking van", "onverminderd"

### Step 6: Note actors
Which bestuursorganen are mentioned and in what role?

## Module Formation (Emergent)

After extracting a set of artikelen:

1. **Group by afdeling** (law's own structure)
2. **Identify clusters** based on:
   - Artikelen that reference each other (intref chains)
   - Artikelen with same legal function
   - Artikelen addressing same subject matter
3. **Define module boundaries** where:
   - Reference chains terminate
   - Subject matter shifts
   - Legal function changes

## Iteration Loop

```
EXTRACT artikel(en) from afdeling
    ↓
CAPTURE atomic logic per schema
    ↓
OBSERVE patterns (refs, delegations, conditions)
    ↓
UPDATE mapping guide if new patterns found
    ↓
DEFINE module boundaries based on observed structure
    ↓
NEXT afdeling → REPEAT
```

## What We DON'T Do

- ❌ Pre-categorize artikelen into "types"
- ❌ Impose navigation patterns before extraction
- ❌ Skip leden/onderdelen (capture full structure)
- ❌ Paraphrase legal text (preserve exact wording)
- ❌ Create "hub" designations before seeing the data

## Starting Point

Based on mapping guide analysis, logical first extractions:

| Afdeling | Articles | Why Start Here |
|----------|----------|----------------|
| **H5 Afd 5.1** | 5.1-5.43 | Core permit logic, most referenced |
| **H4 Afd 4.1** | 4.1-4.14 | General rules framework |
| **H2 Afd 2.4** | 2.33-2.39 | Task allocation (subsidiariteit) |

These contain the legal logic that other chapters reference most.
