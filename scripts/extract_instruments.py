#!/usr/bin/env python3
"""
Extract instrument types from Omgevingswet.

Key instruments:
- Omgevingsvisie (Art. 3.1) - Strategic vision
- Omgevingsplan (Art. 2.4) - Municipal zoning rules
- Waterschapsverordening (Art. 2.5) - Water board regulations
- Omgevingsverordening (Art. 2.6) - Provincial regulations
- Omgevingsvergunning (Chapter 5) - Permits
- Projectbesluit (Chapter 5) - Project decisions
- Programma (Art. 3.4+) - Programs
"""

from lxml import etree
from pathlib import Path
import yaml
import re


def clean_text(text):
    """Clean and normalize text."""
    if not text:
        return ""
    return re.sub(r'\s+', ' ', text).strip()


def get_article_text(root, article_path):
    """Get article text by bwb-ng-variabel-deel path."""
    artikel = root.find(f".//*[@bwb-ng-variabel-deel='{article_path}']")
    if artikel is not None:
        return clean_text(''.join(artikel.itertext()))
    return None


def find_article_by_label(root, label):
    """Find article by its label attribute (e.g., 'Artikel 2.4')."""
    artikel = root.find(f".//artikel[@label='{label}']")
    if artikel is not None:
        # Get title
        kop = artikel.find('kop')
        title = ""
        if kop is not None:
            titel_el = kop.find('titel')
            if titel_el is not None:
                title = clean_text(titel_el.text or '')

        # Get first paragraph text
        first_al = artikel.find('.//al')
        first_text = clean_text(''.join(first_al.itertext())) if first_al is not None else ""

        return {
            'path': artikel.get('bwb-ng-variabel-deel', ''),
            'title': title,
            'first_paragraph': first_text[:300]
        }
    return None


def extract_instruments(xml_path: Path) -> dict:
    """Extract instrument definitions from Omgevingswet."""
    tree = etree.parse(str(xml_path))
    root = tree.getroot()

    instruments = {}

    # 1. Omgevingsvisie - Art. 3.1
    art_3_1 = find_article_by_label(root, 'Artikel 3.1')
    instruments['omgevingsvisie'] = {
        'id': 'ow-instr-omgevingsvisie',
        'name': 'Omgevingsvisie',
        'name_nl': 'Omgevingsvisie',
        'type': 'beleidsvisie',
        'defining_article': '3.1',
        'article_title': art_3_1['title'] if art_3_1 else '',
        'description': 'Strategische visie document over de fysieke leefomgeving',
        'bevoegd_gezag': ['gemeente', 'provincie', 'rijk'],
        'related_articles': ['3.1', '3.2', '3.3'],
        'source_text': art_3_1['first_paragraph'] if art_3_1 else ''
    }

    # 2. Omgevingsplan - Art. 2.4
    art_2_4 = find_article_by_label(root, 'Artikel 2.4')
    instruments['omgevingsplan'] = {
        'id': 'ow-instr-omgevingsplan',
        'name': 'Omgevingsplan',
        'name_nl': 'Omgevingsplan',
        'type': 'verordening',
        'defining_article': '2.4',
        'article_title': art_2_4['title'] if art_2_4 else '',
        'description': 'Gemeentelijke regels over de fysieke leefomgeving',
        'bevoegd_gezag': ['gemeente'],
        'related_articles': ['2.4', '4.1', '4.2'],
        'source_text': art_2_4['first_paragraph'] if art_2_4 else ''
    }

    # 3. Waterschapsverordening - Art. 2.5
    art_2_5 = find_article_by_label(root, 'Artikel 2.5')
    instruments['waterschapsverordening'] = {
        'id': 'ow-instr-waterschapsverordening',
        'name': 'Waterschapsverordening',
        'name_nl': 'Waterschapsverordening',
        'type': 'verordening',
        'defining_article': '2.5',
        'article_title': art_2_5['title'] if art_2_5 else '',
        'description': 'Waterschapsregels over de fysieke leefomgeving',
        'bevoegd_gezag': ['waterschap'],
        'related_articles': ['2.5'],
        'source_text': art_2_5['first_paragraph'] if art_2_5 else ''
    }

    # 4. Omgevingsverordening - Art. 2.6
    art_2_6 = find_article_by_label(root, 'Artikel 2.6')
    instruments['omgevingsverordening'] = {
        'id': 'ow-instr-omgevingsverordening',
        'name': 'Omgevingsverordening',
        'name_nl': 'Omgevingsverordening',
        'type': 'verordening',
        'defining_article': '2.6',
        'article_title': art_2_6['title'] if art_2_6 else '',
        'description': 'Provinciale regels over de fysieke leefomgeving',
        'bevoegd_gezag': ['provincie'],
        'related_articles': ['2.6'],
        'source_text': art_2_6['first_paragraph'] if art_2_6 else ''
    }

    # 5. Omgevingsvergunning - Art. 5.1
    art_5_1 = find_article_by_label(root, 'Artikel 5.1')
    instruments['omgevingsvergunning'] = {
        'id': 'ow-instr-omgevingsvergunning',
        'name': 'Omgevingsvergunning',
        'name_nl': 'Omgevingsvergunning',
        'type': 'vergunning',
        'defining_article': '5.1',
        'article_title': art_5_1['title'] if art_5_1 else '',
        'description': 'Vergunning voor activiteiten in de fysieke leefomgeving',
        'bevoegd_gezag': ['gemeente', 'provincie', 'rijk', 'waterschap'],
        'related_articles': ['5.1', '5.2', '5.3', '5.4'],
        'chapter': 5,
        'source_text': art_5_1['first_paragraph'] if art_5_1 else ''
    }

    # 6. Projectbesluit - Art. 5.44
    art_5_44 = find_article_by_label(root, 'Artikel 5.44')
    instruments['projectbesluit'] = {
        'id': 'ow-instr-projectbesluit',
        'name': 'Projectbesluit',
        'name_nl': 'Projectbesluit',
        'type': 'besluit',
        'defining_article': '5.44',
        'article_title': art_5_44['title'] if art_5_44 else '',
        'description': 'Besluit voor complexe projecten met publiek belang',
        'bevoegd_gezag': ['provincie', 'rijk', 'waterschap'],
        'related_articles': ['5.44', '5.45', '5.46'],
        'chapter': 5,
        'source_text': art_5_44['first_paragraph'] if art_5_44 else ''
    }

    # 7. Programma - Art. 3.4
    art_3_4 = find_article_by_label(root, 'Artikel 3.4')
    instruments['programma'] = {
        'id': 'ow-instr-programma',
        'name': 'Programma',
        'name_nl': 'Programma',
        'type': 'programma',
        'defining_article': '3.4',
        'article_title': art_3_4['title'] if art_3_4 else '',
        'description': 'Maatregelenpakket voor bereiken van doelstellingen',
        'bevoegd_gezag': ['gemeente', 'provincie', 'rijk', 'waterschap'],
        'related_articles': ['3.4', '3.5', '3.6', '3.7'],
        'source_text': art_3_4['first_paragraph'] if art_3_4 else ''
    }

    return instruments


def main():
    project_dir = Path(__file__).parent.parent
    xml_path = project_dir / 'source' / 'Omgevingswet_clean.xml'
    output_path = project_dir / 'infra' / 'instruments.yaml'

    print(f"Extracting instruments from: {xml_path}")

    instruments = extract_instruments(xml_path)

    print(f"\nExtracted {len(instruments)} instruments")

    # Build YAML structure
    yaml_data = {
        '_metadata': {
            'id': 'ow-infra-instruments',
            'title': 'Omgevingswet Instrumenten',
            'description': 'Legal instruments defined by the Omgevingswet',
            'extraction_date': '2026-01-28',
            'count': len(instruments)
        },
        'instrument_types': {
            'beleidsvisie': 'Strategic policy vision document',
            'verordening': 'Regulatory ordinance with binding rules',
            'vergunning': 'Permit for specific activities',
            'besluit': 'Administrative decision',
            'programma': 'Program of measures'
        },
        'instruments': instruments
    }

    # Write YAML
    print(f"Writing to: {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        yaml.dump(yaml_data, f, allow_unicode=True, default_flow_style=False,
                  sort_keys=False, width=120)

    # Show summary
    print("\n=== INSTRUMENTS SUMMARY ===")
    for key, instr in instruments.items():
        print(f"\n{instr['id']}:")
        print(f"  name: {instr['name']}")
        print(f"  type: {instr['type']}")
        print(f"  article: {instr['defining_article']}")
        print(f"  bevoegd_gezag: {', '.join(instr['bevoegd_gezag'])}")


if __name__ == '__main__':
    main()
