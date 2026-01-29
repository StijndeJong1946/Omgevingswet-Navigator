# Omgevingswet Module Template

## Structure

```yaml
# Module: [Afdeling X.Y] - [Title]
# Omgevingswet Navigator Module
# Source: Omgevingswet.xml

_metadata:
  module_id: "ow-mod-ch{X}-afd-{X.Y}"
  chapter: X
  chapter_title: "[Chapter title]"
  afdeling: "X.Y"
  afdeling_title: "[Afdeling title]"
  article_range: ["X.Y", "X.Z"]
  article_count: N
  extraction_date: "YYYY-MM-DD"
  source_path: "/HoofdstukX/AfdelingX.Y"

# Article extraction pattern
article_X.Y:
  article: "X.Y"
  title_nl: "(article title)"

  # Full legal text
  text_nl: |
    [Complete article text, preserving structure]

  # For articles with numbered lids
  leden:
    - lid: 1
      text: "[Lid 1 text]"
    - lid: 2
      text: "[Lid 2 text]"

  # Cross-references (optional)
  internal_refs:  # intref to other OW articles
    - ref: "artikel X.Y"
      path: "/HoofdstukX/..."

  external_refs:  # extref to other laws
    - ref: "artikel Z Awb"
      bwb_id: "BWBR0005537"

  # Procedural metadata (where applicable)
  procedure:
    type: "regulier|uitgebreid|coordinated"
    termijn: "X weken"
    bevoegd_gezag: ["gemeente", "provincie", "rijk", "waterschap"]

  # Instrument metadata (where applicable)
  instrument:
    type: "omgevingsvergunning|projectbesluit|..."
    scope: "[what it covers]"
```

## Granularity

- **Primary**: Afdeling level (like BAL)
- **Split if**: >30 articles or distinct sub-topics (use paragraaf)

## Naming Convention

- Module ID: `ow-mod-ch{chapter}-afd-{afdeling}`
- File: `modules/ch{X}-afd{X.Y}/afd-{X.Y}-{slug}.yaml`
- Paragraaf: `modules/ch{X}-afd{X.Y}/par-{X.Y.Z}-{slug}.yaml`

## Key Differences from BAL

| Aspect | BAL | Omgevingswet |
|--------|-----|--------------|
| Content | Technical thresholds | Procedural framework |
| Primary fields | threshold_values, conditions | procedure, termijn, bevoegd_gezag |
| Routing | Activity → threshold → rule | Instrument → procedure → authority |
