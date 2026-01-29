# Omgevingswet Navigator - Methodology

## Extraction Principles

1. **Source XML is truth** - Omgevingswet XML from wetten.overheid.nl is canonical
2. **Extract, don't interpret** - Preserve exact legal text and structure
3. **Infrastructure first** - Extract shared data before building modules
4. **Validate continuously** - Check coverage and accuracy at each phase
5. **Document discoveries** - Use ERRATA.md for patterns found during extraction

## Phased Approach

### Phase 0: Discovery (Current)
- [x] Obtain Omgevingswet XML
- [ ] Analyze structure: chapters, afdelingen, articles
- [ ] Identify metadata to strip vs. retain
- [ ] Define module granularity
- [ ] Document structure findings

### Phase 1: Infrastructure Extraction
- [ ] Extract definitions (begrippen) from Bijlage
- [ ] Extract instrument types
- [ ] Extract bevoegdheid rules
- [ ] Map cross-references to AMvBs
- [ ] Create infrastructure YAML files

### Phase 2: Module Design
- [ ] Define module template
- [ ] Build pilot modules
- [ ] Validate and refine

### Phase 3: Full Extraction
- [ ] Extract all modules
- [ ] Build routing registry
- [ ] Create procedure flows

### Phase 4: Integration
- [ ] Connect to BAL Navigator
- [ ] Build cross-reference links
- [ ] Test navigation

## Metadata Handling

### Strip (irrelevant)
- `stam-id`, `versie-id`, `id`, `label-id`
- `<brondata>`, `<publicatie>`, `<dossierref>`
- `<jcis>`, `<jci>` blocks
- `publicatie_*`, `ondertekening_*` attributes

### Retain (legally relevant)
- `inwerking` (entry into force date)
- `status` (legal status)
- `<intref>`, `<extref>` with `bwb-id` (cross-references)
- `bwb-ng-variabel-deel` (navigation paths)
