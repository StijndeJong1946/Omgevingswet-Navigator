#!/usr/bin/env python3
"""
Extract bevoegdheden (competent authority) mappings from Omgevingswet Chapter 2.

Bevoegd gezag types:
- gemeente (municipality) - gemeenteraad, college van B&W
- provincie (province) - provinciale staten, gedeputeerde staten
- rijk (national) - Minister, Onze Minister
- waterschap (water board) - algemeen bestuur, dagelijks bestuur
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


def extract_bevoegdheden(xml_path: Path) -> dict:
    """Extract bevoegdheden from Chapter 2."""
    tree = etree.parse(str(xml_path))
    root = tree.getroot()

    # Find Chapter 2
    ch2 = root.find(".//hoofdstuk[@label='Hoofdstuk 2']")
    if ch2 is None:
        print("ERROR: Chapter 2 not found")
        return {}

    # Extract afdelingen structure
    afdelingen = []
    for afd in ch2.findall('.//afdeling'):
        kop = afd.find('kop')
        if kop is not None:
            nr = kop.find('nr')
            titel = kop.find('titel')
            afd_data = {
                'nr': nr.text if nr is not None else '',
                'titel': clean_text(titel.text) if titel is not None else '',
                'path': afd.get('bwb-ng-variabel-deel', ''),
                'artikelen': []
            }

            # Get articles in this afdeling
            for art in afd.findall('.//artikel'):
                art_kop = art.find('kop')
                if art_kop is not None:
                    art_nr = art_kop.find('nr')
                    art_titel = art_kop.find('titel')
                    art_text = clean_text(''.join(art.itertext()))[:200]

                    afd_data['artikelen'].append({
                        'nr': art_nr.text if art_nr is not None else '',
                        'titel': clean_text(art_titel.text) if art_titel is not None else '',
                        'preview': art_text
                    })

            afdelingen.append(afd_data)

    # Define core bevoegdheden based on key articles
    bevoegdheden = {
        'gemeente': {
            'id': 'ow-bg-gemeente',
            'name': 'Gemeente',
            'name_nl': 'Gemeente',
            'organs': {
                'gemeenteraad': 'Vertegenwoordigend orgaan, vaststellen omgevingsplan',
                'college_bw': 'College van burgemeester en wethouders, dagelijks bestuur'
            },
            'core_competencies': [
                {
                    'instrument': 'omgevingsplan',
                    'article': '2.4',
                    'description': 'Vaststellen omgevingsplan voor gehele grondgebied'
                },
                {
                    'instrument': 'omgevingsvergunning',
                    'article': '5.1',
                    'description': 'Verlenen omgevingsvergunning (default bevoegd gezag)'
                },
                {
                    'instrument': 'omgevingsvisie',
                    'article': '3.1',
                    'description': 'Vaststellen gemeentelijke omgevingsvisie'
                }
            ]
        },
        'provincie': {
            'id': 'ow-bg-provincie',
            'name': 'Provincie',
            'name_nl': 'Provincie',
            'organs': {
                'provinciale_staten': 'Vertegenwoordigend orgaan, vaststellen omgevingsverordening',
                'gedeputeerde_staten': 'Dagelijks bestuur, uitvoering'
            },
            'core_competencies': [
                {
                    'instrument': 'omgevingsverordening',
                    'article': '2.6',
                    'description': 'Vaststellen omgevingsverordening'
                },
                {
                    'instrument': 'instructieregels',
                    'article': '2.22',
                    'description': 'Stellen van instructieregels aan gemeente en waterschap'
                },
                {
                    'instrument': 'projectbesluit',
                    'article': '5.44',
                    'description': 'Vaststellen projectbesluit voor provinciale projecten'
                },
                {
                    'instrument': 'omgevingsvisie',
                    'article': '3.1',
                    'description': 'Vaststellen provinciale omgevingsvisie'
                }
            ]
        },
        'rijk': {
            'id': 'ow-bg-rijk',
            'name': 'Rijk',
            'name_nl': 'Rijk (nationaal)',
            'organs': {
                'minister_bzk': 'Minister van Binnenlandse Zaken en Koninkrijksrelaties',
                'minister_ienw': 'Minister van Infrastructuur en Waterstaat',
                'ministers': 'Overige betrokken ministers'
            },
            'core_competencies': [
                {
                    'instrument': 'amvb',
                    'article': '2.24',
                    'description': 'Stellen van rijksinstructieregels bij AMvB'
                },
                {
                    'instrument': 'omgevingsvisie',
                    'article': '3.1',
                    'description': 'Vaststellen nationale omgevingsvisie'
                },
                {
                    'instrument': 'projectbesluit',
                    'article': '5.44',
                    'description': 'Vaststellen projectbesluit voor rijksprojecten'
                }
            ]
        },
        'waterschap': {
            'id': 'ow-bg-waterschap',
            'name': 'Waterschap',
            'name_nl': 'Waterschap',
            'organs': {
                'algemeen_bestuur': 'Vertegenwoordigend orgaan, vaststellen waterschapsverordening',
                'dagelijks_bestuur': 'Dagelijks bestuur, uitvoering'
            },
            'core_competencies': [
                {
                    'instrument': 'waterschapsverordening',
                    'article': '2.5',
                    'description': 'Vaststellen waterschapsverordening'
                },
                {
                    'instrument': 'omgevingsvergunning',
                    'article': '5.1',
                    'description': 'Verlenen watervergunning (lozingen, waterkeringen)'
                },
                {
                    'instrument': 'projectbesluit',
                    'article': '5.44',
                    'description': 'Vaststellen projectbesluit voor waterschapsprojecten'
                }
            ]
        }
    }

    return {
        'afdelingen_ch2': afdelingen,
        'bevoegd_gezag': bevoegdheden
    }


def main():
    project_dir = Path(__file__).parent.parent
    xml_path = project_dir / 'source' / 'Omgevingswet.xml'
    output_path = project_dir / 'infra' / 'bevoegdheden.yaml'

    print(f"Extracting bevoegdheden from: {xml_path}")

    data = extract_bevoegdheden(xml_path)

    print(f"\nChapter 2 structure:")
    for afd in data['afdelingen_ch2']:
        print(f"  {afd['nr']}: {afd['titel']} ({len(afd['artikelen'])} artikelen)")

    print(f"\nBevoegd gezag types: {len(data['bevoegd_gezag'])}")

    # Build YAML
    yaml_data = {
        '_metadata': {
            'id': 'ow-infra-bevoegdheden',
            'title': 'Omgevingswet Bevoegdheden',
            'description': 'Competent authority mappings from Chapter 2',
            'source_chapter': 'Hoofdstuk 2: Taken en bevoegdheden van bestuursorganen',
            'extraction_date': '2026-01-28'
        },
        'chapter_2_structure': data['afdelingen_ch2'],
        'bevoegd_gezag': data['bevoegd_gezag']
    }

    print(f"\nWriting to: {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        yaml.dump(yaml_data, f, allow_unicode=True, default_flow_style=False,
                  sort_keys=False, width=120)

    # Summary
    print("\n=== BEVOEGD GEZAG SUMMARY ===")
    for key, bg in data['bevoegd_gezag'].items():
        print(f"\n{bg['name']}:")
        print(f"  Organs: {', '.join(bg['organs'].keys())}")
        print(f"  Core competencies: {len(bg['core_competencies'])}")
        for comp in bg['core_competencies']:
            print(f"    - {comp['instrument']} (Art. {comp['article']})")


if __name__ == '__main__':
    main()
