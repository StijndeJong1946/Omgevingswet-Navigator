#!/usr/bin/env python3
"""
Omgevingswet XML Metadata Stripper (Option B: Selective Strip)

Removes irrelevant metadata while preserving legally relevant data:
- REMOVES: tracking IDs, publication chains, JCI references
- KEEPS: structure, text, inwerking dates, status, cross-references
"""

from lxml import etree
from pathlib import Path
import re

# Attributes to REMOVE (tracking/administrative)
STRIP_ATTRIBUTES = {
    'stam-id',
    'versie-id',
    'id',
    'label-id',
    'publicatie_bron',
    'publicatie_iwt',
    'ondertekening_bron',
    'bron',
    'effect',
    'dtdversie',
    'soort',
    'verwijzing-id',
}

# Attributes to KEEP (legally relevant)
KEEP_ATTRIBUTES = {
    'inwerking',           # Entry into force date
    'status',              # Legal status (officieel, goed)
    'bwb-ng-variabel-deel', # Navigation path
    'bwb-id',              # Cross-reference identifier
    'label',               # Display label
    'nr',                  # Number
    'level',               # List level
    'type',                # List type
    'start',               # List start
    'nr-sluiting',         # List number closure
    'doc',                 # Reference doc
}

# Elements to REMOVE entirely
STRIP_ELEMENTS = {
    'meta-data',           # All metadata blocks
    'brondata',            # Source/publication data
    'jcis',                # JCI reference containers
    'jci',                 # JCI references
    'bwb-inputbestand',    # Input file reference
    'bwb-wijzigingen',     # Change tracking
    'redactionele-correcties',  # Editorial corrections
}

# Elements that are structural containers (keep but clean)
STRUCTURAL_ELEMENTS = {
    'toestand', 'wetgeving', 'wet-besluit', 'wettekst',
    'hoofdstuk', 'afdeling', 'paragraaf', 'artikel', 'lid',
    'kop', 'label', 'nr', 'titel',
    'al', 'lijst', 'li', 'li.nr',
    'intref', 'extref',
    'intitule', 'citeertitel', 'aanhef', 'considerans',
    'considerans.al', 'afkondiging', 'wij',
    'lidnr', 'bijlage', 'plaatje', 'tussenkop',
    'artikel.toelichting', 'redactie', 'vetgedrukt',
    'nadruk', 'cursief', 'sup', 'sub',
    'specificatielijst', 'specificatie-item',
    'table', 'tgroup', 'thead', 'tbody', 'row', 'entry', 'colspec',
}


def strip_element(element):
    """Remove an element and all its children."""
    parent = element.getparent()
    if parent is not None:
        parent.remove(element)


def clean_attributes(element):
    """Remove unwanted attributes from an element."""
    attrs_to_remove = []
    for attr in element.attrib:
        # Keep if in whitelist
        if attr in KEEP_ATTRIBUTES:
            continue
        # Remove if in blacklist or not recognized
        if attr in STRIP_ATTRIBUTES or attr not in KEEP_ATTRIBUTES:
            attrs_to_remove.append(attr)

    for attr in attrs_to_remove:
        del element.attrib[attr]


def process_element(element):
    """Recursively process element and its children."""
    # Get tag name without namespace
    tag = etree.QName(element.tag).localname if isinstance(element.tag, str) else element.tag

    # Remove unwanted elements
    if tag in STRIP_ELEMENTS:
        strip_element(element)
        return

    # Clean attributes on remaining elements
    clean_attributes(element)

    # Process children (iterate over copy since we may modify)
    for child in list(element):
        process_element(child)


def strip_metadata(input_path: Path, output_path: Path) -> dict:
    """
    Strip metadata from Omgevingswet XML.

    Returns stats dict with counts.
    """
    print(f"Reading: {input_path}")

    # Parse with recovery mode for any malformed content
    parser = etree.XMLParser(remove_blank_text=False, recover=True)
    tree = etree.parse(str(input_path), parser)
    root = tree.getroot()

    # Count elements before
    count_before = len(list(root.iter()))
    size_before = input_path.stat().st_size

    # Process all elements
    process_element(root)

    # Count elements after
    count_after = len(list(root.iter()))

    # Write output
    print(f"Writing: {output_path}")
    tree.write(
        str(output_path),
        encoding='UTF-8',
        xml_declaration=True,
        pretty_print=True
    )

    size_after = output_path.stat().st_size

    return {
        'elements_before': count_before,
        'elements_after': count_after,
        'elements_removed': count_before - count_after,
        'size_before': size_before,
        'size_after': size_after,
        'size_reduction_pct': round((1 - size_after/size_before) * 100, 1)
    }


def extract_structure_summary(input_path: Path) -> dict:
    """Extract high-level structure info from the XML."""
    tree = etree.parse(str(input_path))
    root = tree.getroot()

    # Find all hoofdstukken
    chapters = []
    for hoofdstuk in root.iter('hoofdstuk'):
        kop = hoofdstuk.find('kop')
        if kop is not None:
            nr_el = kop.find('nr')
            titel_el = kop.find('titel')
            nr = nr_el.text if nr_el is not None else '?'
            titel = titel_el.text if titel_el is not None else '?'

            # Count articles in this chapter
            artikel_count = len(list(hoofdstuk.iter('artikel')))
            chapters.append({
                'nr': nr,
                'titel': titel,
                'artikelen': artikel_count
            })

    # Count total articles
    total_articles = len(list(root.iter('artikel')))

    # Check for bijlage
    bijlage = root.find('.//bijlage')
    has_bijlage = bijlage is not None

    return {
        'chapters': chapters,
        'total_articles': total_articles,
        'has_bijlage': has_bijlage
    }


if __name__ == '__main__':
    # Paths
    project_dir = Path(__file__).parent.parent
    input_file = project_dir / 'source' / 'Omgevingswet.xml'
    output_file = project_dir / 'source' / 'Omgevingswet_clean.xml'

    # First, extract structure summary
    print("\n=== STRUCTURE ANALYSIS ===")
    structure = extract_structure_summary(input_file)
    print(f"\nTotal chapters: {len(structure['chapters'])}")
    print(f"Total articles: {structure['total_articles']}")
    print(f"Has bijlage (definitions): {structure['has_bijlage']}")
    print("\nChapters:")
    for ch in structure['chapters']:
        print(f"  {ch['nr']}: {ch['titel']} ({ch['artikelen']} artikelen)")

    # Strip metadata
    print("\n=== STRIPPING METADATA ===")
    stats = strip_metadata(input_file, output_file)

    print("\n=== RESULTS ===")
    print(f"Elements: {stats['elements_before']:,} → {stats['elements_after']:,} ({stats['elements_removed']:,} removed)")
    print(f"File size: {stats['size_before']:,} → {stats['size_after']:,} bytes")
    print(f"Reduction: {stats['size_reduction_pct']}%")
    print(f"\nClean file: {output_file}")
