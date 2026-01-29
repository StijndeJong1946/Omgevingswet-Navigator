# Omgevingswet Skeleton Mapping Guide

## Purpose

Map the **legal logic structure** of each chapter before full extraction. The skeleton reveals how articles connect, forming decision workflows that can then be deeply extracted.

## Skeleton Schema

```yaml
# ch{X}-skeleton.yaml
_metadata:
  chapter: X
  chapter_title: "[Title]"
  total_articles: N
  afdelingen: M
  clusters_identified: K
  mapping_date: "YYYY-MM-DD"

# Per-article skeleton
skeleton:
  artikel_X.Y:
    title: "(article title)"
    afdeling: "X.Z"

    # ROLE CLASSIFICATION (can have multiple)
    roles:
      - trigger      # Activates legal pathway
      - condition    # Adds if/then logic
      - authority    # Determines who decides
      - procedure    # Defines process steps
      - outcome      # Terminal state/result
      - delegation   # Points to AMvB/external
      - exception    # Breaks normal flow
      - definition   # Clarifies terms

    # WHAT THIS ARTICLE DOES
    determines: "[What decision/rule this article establishes]"

    # GRAPH EDGES
    triggered_by:      # What activates this article
      - source: "artikel X.A" | "external"
        condition: "[When/why]"

    routes_to:         # Where flow goes next
      - target: "artikel X.B"
        condition: "[When this path is taken]"

    exceptions:        # Exception handling
      - exception: "[What exception]"
        defined_in: "artikel X.C" | "AMvB"
        effect: "[What happens]"

    delegates_to:      # External delegations
      - target: "Bal" | "Bkl" | "Bbl" | "Or"
        for: "[What is delegated]"

    # COMPLEXITY INDICATORS
    complexity:
      leden_count: N
      onderdelen_count: N
      has_nested_lists: true|false
      has_exceptions: true|false
      internal_refs_count: N
      external_refs_count: N
      delegation_count: N

    # CLUSTER ASSIGNMENT
    cluster: "cluster-XA"

# Cluster definitions
clusters:
  cluster-XA:
    name: "[Descriptive workflow name]"
    purpose: "[What decision this workflow handles]"
    entry_points: ["X.Y"]      # Where you enter this workflow
    exit_points: ["X.Z"]       # Where workflow terminates/routes out
    articles: ["X.Y", "X.Z", ...]
    complexity: low|medium|high|very_high
```

## Role Classification Reference

| Role | Markers in Text | Example |
|------|-----------------|---------|
| **TRIGGER** | "verboden zonder", "vergunningplichtig", "vereist" | Art. 5.1 |
| **CONDITION** | "indien", "als", "wanneer", "mits", "voor zover" | Art. 5.18 |
| **AUTHORITY** | "bevoegd gezag", "beslist", "verleent", "minister" | Art. 5.9-5.16 |
| **PROCEDURE** | "aanvraag", "termijn", "bekendmaking", "procedure" | Art. 16.x |
| **OUTCOME** | "wordt verleend", "wordt geweigerd", "voorschriften" | Art. 5.34 |
| **DELEGATION** | "bij AMvB", "bij ministeriële regeling", "krachtens" | Art. 5.1 lid 2 |
| **EXCEPTION** | "tenzij", "niet van toepassing", "uitgezonderd" | scattered |
| **DEFINITION** | "wordt verstaan", "begrip", Bijlage reference | Art. 1.1, Bijlage |

## Mapping Process

1. **Read afdeling structure** - Identify paragrafen within afdelingen
2. **Scan each article** - Classify roles, identify key verbs/markers
3. **Map connections** - What triggers this? Where does it route?
4. **Identify clusters** - Group articles into decision workflows
5. **Flag complexity** - Mark articles needing deep extraction attention

## Output Location

```
modules/
├── ch{X}-skeleton.yaml       # Chapter skeleton
└── ch{X}-afd{X.Y}/           # Full modules (after skeleton)
```
