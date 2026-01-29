#!/usr/bin/env python3
"""
Deep validation: compare actual legal text only (excluding metadata).
"""

from lxml import etree
from pathlib import Path

# Elements that contain metadata (not legal text)
METADATA_TAGS = {'meta-data', 'brondata', 'jcis', 'jci', 'publicatie',
                 'oorspronkelijk', 'inwerkingtreding', 'dossierref'}

def get_legal_text(element, exclude_metadata=True):
    """
    Extract text from element, optionally excluding metadata elements.
    """
    if exclude_metadata:
        # Clone element and remove metadata
        elem_copy = etree.fromstring(etree.tostring(element))
        for meta_tag in METADATA_TAGS:
            for meta in elem_copy.iter(meta_tag):
                parent = meta.getparent()
                if parent is not None:
                    parent.remove(meta)
        return ''.join(elem_copy.itertext()).strip()
    else:
        return ''.join(element.itertext()).strip()


def compare_article(orig_artikel, clean_artikel):
    """Compare a single article's legal text."""
    # Get article number
    kop = orig_artikel.find('kop')
    nr = kop.find('nr').text if kop is not None and kop.find('nr') is not None else '?'

    # Extract legal text only (excluding metadata from original)
    orig_text = get_legal_text(orig_artikel, exclude_metadata=True)
    clean_text = get_legal_text(clean_artikel, exclude_metadata=False)  # Clean has no metadata

    return {
        'nr': nr,
        'orig_len': len(orig_text),
        'clean_len': len(clean_text),
        'match': orig_text == clean_text,
        'orig_text': orig_text[:200],
        'clean_text': clean_text[:200]
    }


def main():
    project_dir = Path(__file__).parent.parent
    original = project_dir / 'source' / 'Omgevingswet.xml'
    clean = project_dir / 'source' / 'Omgevingswet_clean.xml'

    print("Loading files...")
    orig_tree = etree.parse(str(original))
    clean_tree = etree.parse(str(clean))

    orig_articles = {a.get('label', ''): a for a in orig_tree.iter('artikel')}
    clean_articles = {a.get('label', ''): a for a in clean_tree.iter('artikel')}

    print(f"\nComparing {len(orig_articles)} articles...\n")

    matches = 0
    mismatches = []

    for label in sorted(orig_articles.keys()):
        if label in clean_articles:
            result = compare_article(orig_articles[label], clean_articles[label])
            if result['match']:
                matches += 1
            else:
                mismatches.append(result)

    print(f"=== RESULTS ===")
    print(f"Matching articles:    {matches}")
    print(f"Mismatched articles:  {len(mismatches)}")

    if mismatches:
        print(f"\n=== FIRST 5 MISMATCHES ===")
        for m in mismatches[:5]:
            print(f"\nArticle {m['nr']}:")
            print(f"  Length: {m['orig_len']} vs {m['clean_len']} (diff: {m['orig_len'] - m['clean_len']})")
            print(f"  Original starts: {m['orig_text'][:100]}...")
            print(f"  Clean starts:    {m['clean_text'][:100]}...")
    else:
        print("\nALL LEGAL TEXT MATCHES PERFECTLY!")

    # Also check the 'al' element count issue
    print("\n=== AL ELEMENT INVESTIGATION ===")

    # Count al elements inside vs outside metadata
    orig_al_in_meta = 0
    orig_al_outside_meta = 0

    for al in orig_tree.iter('al'):
        # Check if any ancestor is metadata
        in_meta = False
        for ancestor in al.iterancestors():
            if ancestor.tag in METADATA_TAGS:
                in_meta = True
                break
        if in_meta:
            orig_al_in_meta += 1
        else:
            orig_al_outside_meta += 1

    clean_al_count = len(list(clean_tree.iter('al')))

    print(f"Original 'al' in metadata:     {orig_al_in_meta}")
    print(f"Original 'al' outside metadata: {orig_al_outside_meta}")
    print(f"Clean 'al' count:               {clean_al_count}")

    if orig_al_outside_meta == clean_al_count:
        print("PASS: All legal 'al' elements preserved")
    else:
        print(f"DIFF: {orig_al_outside_meta - clean_al_count} 'al' elements difference")


if __name__ == '__main__':
    main()
