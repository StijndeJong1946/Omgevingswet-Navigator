#!/usr/bin/env python3
"""
Extract and analyze cross-references (extref) to other laws/AMvBs.

This identifies which external laws are referenced and from which articles,
enabling integration mapping with BAL Navigator and other systems.
"""

from lxml import etree
from pathlib import Path
import yaml
from collections import defaultdict
import re


def clean_text(text):
    """Clean and normalize text."""
    if not text:
        return ""
    return re.sub(r'\s+', ' ', text).strip()


def extract_crossrefs(xml_path: Path) -> dict:
    """Extract all extref elements and analyze references."""
    tree = etree.parse(str(xml_path))
    root = tree.getroot()

    # Collect all extrefs grouped by bwb-id
    refs_by_bwb = defaultdict(list)

    for extref in root.iter('extref'):
        bwb_id = extref.get('bwb-id', '')
        if not bwb_id:
            continue

        # Get the link text
        link_text = clean_text(''.join(extref.itertext()))

        # Find the containing article
        article = None
        for ancestor in extref.iterancestors():
            if ancestor.tag == 'artikel':
                art_label = ancestor.get('label', '')
                article = art_label
                break

        refs_by_bwb[bwb_id].append({
            'text': link_text,
            'from_article': article,
            'doc': extref.get('doc', '')
        })

    return dict(refs_by_bwb)


def categorize_references(refs_by_bwb: dict) -> dict:
    """Categorize references by type of law."""
    # Known BWB IDs
    known_laws = {
        # Omgevingswet AMvBs
        'BWBR0043298': {'name': 'Besluit activiteiten leefomgeving', 'abbrev': 'Bal', 'type': 'amvb'},
        'BWBR0043301': {'name': 'Besluit kwaliteit leefomgeving', 'abbrev': 'Bkl', 'type': 'amvb'},
        'BWBR0043297': {'name': 'Besluit bouwwerken leefomgeving', 'abbrev': 'Bbl', 'type': 'amvb'},
        'BWBR0043451': {'name': 'Omgevingsregeling', 'abbrev': 'Or', 'type': 'ministeriële regeling'},

        # Related laws
        'BWBR0003245': {'name': 'Wet milieubeheer', 'abbrev': 'Wm', 'type': 'wet'},
        'BWBR0005537': {'name': 'Algemene wet bestuursrecht', 'abbrev': 'Awb', 'type': 'wet'},
        'BWBR0001840': {'name': 'Grondwet', 'abbrev': 'Gw', 'type': 'wet'},
        'BWBR0005555': {'name': 'Wet luchtvaart', 'abbrev': 'Wlv', 'type': 'wet'},
        'BWBR0037521': {'name': 'Erfgoedwet', 'abbrev': 'Efw', 'type': 'wet'},
        'BWBR0006622': {'name': 'Wegenverkeerswet 1994', 'abbrev': 'Wvw', 'type': 'wet'},
        'BWBR0014168': {'name': 'Mijnbouwwet', 'abbrev': 'Mbw', 'type': 'wet'},
        'BWBR0037885': {'name': 'Omgevingswet', 'abbrev': 'Ow', 'type': 'wet'},  # self-reference

        # EU
        'EU_IED': {'name': 'Richtlijn industriële emissies', 'abbrev': 'RIE', 'type': 'eu-richtlijn'},
    }

    categorized = {
        'amvb': [],
        'wet': [],
        'ministeriële regeling': [],
        'eu-richtlijn': [],
        'unknown': []
    }

    for bwb_id, refs in refs_by_bwb.items():
        info = known_laws.get(bwb_id, None)

        entry = {
            'bwb_id': bwb_id,
            'reference_count': len(refs),
            'sample_texts': list(set(r['text'] for r in refs[:5])),
            'from_articles': list(set(r['from_article'] for r in refs if r['from_article']))[:10]
        }

        if info:
            entry['name'] = info['name']
            entry['abbrev'] = info['abbrev']
            categorized[info['type']].append(entry)
        else:
            categorized['unknown'].append(entry)

    # Sort by reference count
    for cat in categorized:
        categorized[cat].sort(key=lambda x: x['reference_count'], reverse=True)

    return categorized


def main():
    project_dir = Path(__file__).parent.parent
    xml_path = project_dir / 'source' / 'Omgevingswet.xml'

    print(f"Extracting cross-references from: {xml_path}")

    refs_by_bwb = extract_crossrefs(xml_path)
    print(f"\nFound references to {len(refs_by_bwb)} unique BWB IDs")

    categorized = categorize_references(refs_by_bwb)

    # Summary
    print("\n=== CROSS-REFERENCE SUMMARY ===")
    total_refs = sum(len(refs) for refs in refs_by_bwb.values())
    print(f"Total references: {total_refs}")

    for cat, entries in categorized.items():
        if entries:
            print(f"\n{cat.upper()} ({len(entries)} laws):")
            for entry in entries[:5]:
                name = entry.get('name', entry['bwb_id'])
                print(f"  - {name}: {entry['reference_count']} refs")

    # Update external-systems.yaml with reference counts
    ext_systems_path = project_dir / 'infra' / 'external-systems.yaml'
    with open(ext_systems_path, 'r', encoding='utf-8') as f:
        ext_data = yaml.safe_load(f)

    # Add cross-reference analysis
    ext_data['cross_reference_analysis'] = {
        'extraction_date': '2026-01-28',
        'total_extref_count': total_refs,
        'unique_bwb_ids': len(refs_by_bwb),
        'by_category': {
            cat: [
                {
                    'bwb_id': e['bwb_id'],
                    'name': e.get('name', 'Unknown'),
                    'abbrev': e.get('abbrev', ''),
                    'reference_count': e['reference_count'],
                    'sample_from_articles': e['from_articles'][:5]
                }
                for e in entries
            ]
            for cat, entries in categorized.items()
            if entries
        }
    }

    # Update integration status for AMvBs we found
    amvb_bwb_ids = {e['bwb_id'] for e in categorized['amvb']}
    for key, sys in ext_data.get('external_systems', {}).items():
        if sys.get('bwb_id') in amvb_bwb_ids:
            # Find ref count
            for entry in categorized['amvb']:
                if entry['bwb_id'] == sys.get('bwb_id'):
                    sys['reference_count_in_ow'] = entry['reference_count']
                    break

    print(f"\nUpdating: {ext_systems_path}")
    with open(ext_systems_path, 'w', encoding='utf-8') as f:
        yaml.dump(ext_data, f, allow_unicode=True, default_flow_style=False,
                  sort_keys=False, width=120)

    print("\nDone!")


if __name__ == '__main__':
    main()
