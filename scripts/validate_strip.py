#!/usr/bin/env python3
"""
Validate that metadata stripping preserved all legally relevant content.

Compares original vs. clean XML to ensure:
1. All articles preserved (count match)
2. All text content intact (al elements)
3. Cross-references preserved (intref, extref)
4. Structure complete (hoofdstuk, afdeling, artikel, lid)
"""

from lxml import etree
from pathlib import Path
import hashlib


def get_text_content(element):
    """Get all text content from element, stripping whitespace."""
    return ''.join(element.itertext()).strip()


def count_elements(root, tag):
    """Count elements with given tag."""
    return len(list(root.iter(tag)))


def extract_article_texts(root):
    """Extract article number -> text content mapping."""
    articles = {}
    for artikel in root.iter('artikel'):
        # Get article number
        kop = artikel.find('kop')
        if kop is not None:
            nr = kop.find('nr')
            if nr is not None and nr.text:
                art_nr = nr.text.strip()
                # Get all text content
                text = get_text_content(artikel)
                articles[art_nr] = text
    return articles


def extract_references(root):
    """Extract all cross-references (intref, extref)."""
    refs = []
    for ref in root.iter('intref'):
        text = get_text_content(ref)
        bwb_id = ref.get('bwb-id', '')
        refs.append(('intref', text, bwb_id))
    for ref in root.iter('extref'):
        text = get_text_content(ref)
        bwb_id = ref.get('bwb-id', '')
        refs.append(('extref', text, bwb_id))
    return refs


def validate(original_path: Path, clean_path: Path):
    """Run validation checks."""
    print("Loading original XML...")
    orig_tree = etree.parse(str(original_path))
    orig_root = orig_tree.getroot()

    print("Loading clean XML...")
    clean_tree = etree.parse(str(clean_path))
    clean_root = clean_tree.getroot()

    results = []
    all_passed = True

    # 1. Structure element counts
    print("\n=== STRUCTURE VALIDATION ===")
    structure_tags = ['hoofdstuk', 'afdeling', 'paragraaf', 'artikel', 'lid', 'al', 'lijst', 'li']

    for tag in structure_tags:
        orig_count = count_elements(orig_root, tag)
        clean_count = count_elements(clean_root, tag)
        status = "PASS" if orig_count == clean_count else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  {tag:12} : {orig_count:5} -> {clean_count:5}  [{status}]")
        results.append((tag, orig_count, clean_count, status))

    # 2. Article text content
    print("\n=== ARTICLE TEXT VALIDATION ===")
    orig_articles = extract_article_texts(orig_root)
    clean_articles = extract_article_texts(clean_root)

    missing_articles = set(orig_articles.keys()) - set(clean_articles.keys())
    extra_articles = set(clean_articles.keys()) - set(orig_articles.keys())

    if missing_articles:
        print(f"  FAIL: Missing articles: {missing_articles}")
        all_passed = False
    else:
        print(f"  PASS: All {len(orig_articles)} articles present")

    if extra_articles:
        print(f"  WARN: Extra articles (unexpected): {extra_articles}")

    # Check text content matches
    text_mismatches = []
    for art_nr in orig_articles:
        if art_nr in clean_articles:
            orig_text = orig_articles[art_nr]
            clean_text = clean_articles[art_nr]
            if orig_text != clean_text:
                text_mismatches.append(art_nr)

    if text_mismatches:
        print(f"  FAIL: Text content differs in {len(text_mismatches)} articles")
        all_passed = False
        # Show first few
        for art_nr in text_mismatches[:3]:
            print(f"    - Article {art_nr}")
    else:
        print(f"  PASS: Text content matches in all articles")

    # 3. Cross-references
    print("\n=== CROSS-REFERENCE VALIDATION ===")
    orig_refs = extract_references(orig_root)
    clean_refs = extract_references(clean_root)

    print(f"  Original: {len(orig_refs)} references")
    print(f"  Clean:    {len(clean_refs)} references")

    if len(orig_refs) == len(clean_refs):
        print("  PASS: Reference count matches")
    else:
        print(f"  FAIL: Reference count mismatch (diff: {len(orig_refs) - len(clean_refs)})")
        all_passed = False

    # Check intref and extref separately
    orig_intref = [r for r in orig_refs if r[0] == 'intref']
    clean_intref = [r for r in clean_refs if r[0] == 'intref']
    orig_extref = [r for r in orig_refs if r[0] == 'extref']
    clean_extref = [r for r in clean_refs if r[0] == 'extref']

    print(f"    intref: {len(orig_intref)} -> {len(clean_intref)}")
    print(f"    extref: {len(orig_extref)} -> {len(clean_extref)}")

    # 4. Bijlage (definitions appendix)
    print("\n=== BIJLAGE VALIDATION ===")
    orig_bijlage = orig_root.find('.//bijlage')
    clean_bijlage = clean_root.find('.//bijlage')

    if orig_bijlage is not None and clean_bijlage is not None:
        orig_bijlage_text = get_text_content(orig_bijlage)
        clean_bijlage_text = get_text_content(clean_bijlage)

        orig_hash = hashlib.md5(orig_bijlage_text.encode()).hexdigest()[:12]
        clean_hash = hashlib.md5(clean_bijlage_text.encode()).hexdigest()[:12]

        if orig_hash == clean_hash:
            print(f"  PASS: Bijlage content matches (hash: {orig_hash})")
        else:
            print(f"  FAIL: Bijlage content differs")
            print(f"    Original hash: {orig_hash}")
            print(f"    Clean hash:    {clean_hash}")
            all_passed = False

        # Count definitions in bijlage
        orig_def_count = len(list(orig_bijlage.iter('li')))
        clean_def_count = len(list(clean_bijlage.iter('li')))
        print(f"  Definition items (li): {orig_def_count} -> {clean_def_count}")
    else:
        print("  FAIL: Bijlage not found in one or both files")
        all_passed = False

    # 5. Sample spot check - show a few articles
    print("\n=== SAMPLE SPOT CHECK ===")
    spot_check_articles = ['1.1', '5.1', '16.1']
    for art_nr in spot_check_articles:
        if art_nr in orig_articles and art_nr in clean_articles:
            orig_len = len(orig_articles[art_nr])
            clean_len = len(clean_articles[art_nr])
            match = "MATCH" if orig_len == clean_len else f"DIFF ({orig_len} vs {clean_len})"
            print(f"  Article {art_nr}: {match}")

    # Final result
    print("\n" + "=" * 50)
    if all_passed:
        print("VALIDATION PASSED: All legally relevant content preserved")
    else:
        print("VALIDATION FAILED: Some content may be missing or altered")
    print("=" * 50)

    return all_passed


if __name__ == '__main__':
    project_dir = Path(__file__).parent.parent
    original = project_dir / 'source' / 'Omgevingswet.xml'
    clean = project_dir / 'source' / 'Omgevingswet_clean.xml'

    validate(original, clean)
