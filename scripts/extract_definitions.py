#!/usr/bin/env python3
"""
Extract definitions (begripsbepalingen) from Omgevingswet Bijlage.

Structure:
- Bijlage > Divisie A (Begrippen) contains all definitions
- Each definition is a <li> with <nadruk type="cur">term:</nadruk> followed by definition
- Some definitions have nested sub-definitions
"""

from lxml import etree
from pathlib import Path
import yaml
import re


def clean_text(text):
    """Clean and normalize text content."""
    if not text:
        return ""
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def extract_term_and_definition(li_element):
    """
    Extract term and definition from a list item.
    Returns (term, definition, sub_definitions)
    """
    # Get full text content
    full_text = clean_text(''.join(li_element.itertext()))

    # Find the nadruk element (contains the term)
    nadruk = li_element.find('.//nadruk[@type="cur"]')

    if nadruk is not None:
        term = clean_text(nadruk.text or '')
        # Remove trailing colon from term
        term = term.rstrip(':').strip()

        # Get the definition - everything after the term
        # The definition is the text after nadruk's tail and subsequent elements
        al = li_element.find('.//al')
        if al is not None:
            al_text = clean_text(''.join(al.itertext()))
            # Remove the term from the beginning
            if al_text.startswith(term):
                definition = al_text[len(term):].lstrip(':').strip()
            else:
                definition = al_text
        else:
            definition = full_text
    else:
        # No nadruk - use full text
        term = ""
        definition = full_text

    # Check for nested list (sub-definitions)
    sub_defs = []
    nested_lijst = li_element.find('./lijst')
    if nested_lijst is not None:
        for sub_li in nested_lijst.findall('./li'):
            li_nr = sub_li.find('li.nr')
            sub_al = sub_li.find('al')
            if li_nr is not None and sub_al is not None:
                nr = clean_text(li_nr.text or '')
                sub_text = clean_text(''.join(sub_al.itertext()))
                sub_defs.append({
                    'nr': nr,
                    'text': sub_text
                })

    # If definition is empty but we have sub_defs, construct definition from them
    if not definition and sub_defs:
        definition = '; '.join([f"{sd['nr']} {sd['text']}" for sd in sub_defs])

    return term, definition, sub_defs


def extract_definitions(xml_path: Path) -> list:
    """Extract all definitions from Bijlage."""
    tree = etree.parse(str(xml_path))
    root = tree.getroot()

    definitions = []

    # Find Bijlage > Divisie A (Begrippen)
    bijlage = root.find('.//bijlage')
    if bijlage is None:
        print("ERROR: Bijlage not found")
        return []

    # Find Divisie A
    for divisie in bijlage.findall('.//divisie'):
        kop = divisie.find('kop')
        if kop is not None:
            nr = kop.find('nr')
            if nr is not None and nr.text == 'A':
                # This is Divisie A - Begrippen
                print(f"Found Divisie A: Begrippen")

                # Find the main list
                hoofdlijst = divisie.find('./lijst')
                if hoofdlijst is None:
                    print("ERROR: Main list not found in Divisie A")
                    continue

                # Process each definition
                for li in hoofdlijst.findall('./li'):
                    path = li.get('bwb-ng-variabel-deel', '')
                    term, definition, sub_defs = extract_term_and_definition(li)

                    if term:
                        def_entry = {
                            'term': term,
                            'definition': definition,
                            'path': path
                        }

                        # Create ID from term
                        term_id = re.sub(r'[^a-z0-9]+', '-', term.lower()).strip('-')
                        def_entry['id'] = f'ow-def-{term_id}'

                        if sub_defs:
                            def_entry['sub_definitions'] = sub_defs

                        definitions.append(def_entry)

    return definitions


def main():
    project_dir = Path(__file__).parent.parent
    xml_path = project_dir / 'source' / 'Omgevingswet_clean.xml'
    output_path = project_dir / 'infra' / 'definitions.yaml'

    print(f"Extracting definitions from: {xml_path}")

    definitions = extract_definitions(xml_path)

    print(f"\nExtracted {len(definitions)} definitions")

    # Build YAML structure
    yaml_data = {
        '_metadata': {
            'id': 'ow-infra-definitions',
            'title': 'Omgevingswet Begripsbepalingen',
            'source': 'Bijlage bij artikel 1.1 Omgevingswet',
            'source_path': '/Bijlage/DivisieA',
            'extraction_date': '2026-01-28',
            'count': len(definitions)
        },
        'definitions': definitions
    }

    # Write YAML
    print(f"Writing to: {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        yaml.dump(yaml_data, f, allow_unicode=True, default_flow_style=False,
                  sort_keys=False, width=120)

    # Show sample
    print("\n=== SAMPLE DEFINITIONS ===")
    for d in definitions[:5]:
        print(f"\n{d['id']}:")
        print(f"  term: {d['term']}")
        print(f"  definition: {d['definition'][:100]}...")

    print(f"\n... and {len(definitions) - 5} more")

    # Stats
    with_subs = len([d for d in definitions if 'sub_definitions' in d])
    print(f"\nDefinitions with sub-definitions: {with_subs}")


if __name__ == '__main__':
    main()
