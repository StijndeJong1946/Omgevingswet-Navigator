#!/usr/bin/env python3
"""
Verify all Phase 1 extractions against source XML.
"""

from lxml import etree
from pathlib import Path
import yaml


def load_yaml(path):
    """Load YAML file."""
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def verify_definitions(xml_root, definitions_path):
    """Verify definitions extraction."""
    print("\n" + "=" * 50)
    print("DEFINITIONS VERIFICATION")
    print("=" * 50)

    data = load_yaml(definitions_path)
    definitions = data['definitions']
    issues = []

    # 1. Check count matches bijlage li count
    bijlage = xml_root.find('.//bijlage')
    divisie_a = None
    for div in bijlage.findall('.//divisie'):
        kop = div.find('kop')
        if kop is not None:
            nr = kop.find('nr')
            if nr is not None and nr.text == 'A':
                divisie_a = div
                break

    if divisie_a is not None:
        xml_li_count = len(divisie_a.findall('./lijst/li'))
        yaml_count = len(definitions)
        print(f"\n1. Count check:")
        print(f"   XML li elements in Divisie A: {xml_li_count}")
        print(f"   YAML definitions: {yaml_count}")
        if xml_li_count == yaml_count:
            print("   STATUS: PASS")
        else:
            print(f"   STATUS: FAIL (diff: {xml_li_count - yaml_count})")
            issues.append(f"Count mismatch: XML={xml_li_count}, YAML={yaml_count}")

    # 2. Check all definitions have required fields
    print(f"\n2. Required fields check:")
    missing_fields = []
    for d in definitions:
        for field in ['term', 'definition', 'id', 'path']:
            if not d.get(field):
                missing_fields.append(f"{d.get('id', '?')}: missing {field}")

    if missing_fields:
        print(f"   STATUS: FAIL - {len(missing_fields)} missing fields")
        for mf in missing_fields[:5]:
            print(f"      - {mf}")
        issues.extend(missing_fields[:5])
    else:
        print("   STATUS: PASS - all definitions have required fields")

    # 3. Check for empty definitions
    print(f"\n3. Empty definition check:")
    empty_defs = [d for d in definitions if len(d.get('definition', '')) < 5]
    if empty_defs:
        print(f"   STATUS: WARN - {len(empty_defs)} very short definitions")
        for ed in empty_defs[:3]:
            print(f"      - {ed['term']}: '{ed['definition']}'")
    else:
        print("   STATUS: PASS - no empty definitions")

    # 4. Spot check - verify a few definitions match XML
    print(f"\n4. Spot check (sample definitions):")
    spot_checks = ['omgevingsplan', 'bouwwerk', 'milieubelastende activiteit']
    for term in spot_checks:
        yaml_def = next((d for d in definitions if d['term'] == term), None)
        if yaml_def:
            # Find in XML
            path = yaml_def['path']
            xml_li = xml_root.find(f".//*[@bwb-ng-variabel-deel='{path}']")
            if xml_li is not None:
                xml_text = ''.join(xml_li.itertext()).strip()[:50]
                print(f"   '{term}': found in both (XML starts: {xml_text}...)")
            else:
                print(f"   '{term}': MISSING in XML at path {path}")
                issues.append(f"Path not found: {path}")
        else:
            print(f"   '{term}': not in YAML definitions")

    return len(issues) == 0, issues


def verify_instruments(xml_root, instruments_path):
    """Verify instruments extraction."""
    print("\n" + "=" * 50)
    print("INSTRUMENTS VERIFICATION")
    print("=" * 50)

    data = load_yaml(instruments_path)
    instruments = data['instruments']
    issues = []

    # 1. Check all instruments have defining article
    print(f"\n1. Defining articles check:")
    for key, instr in instruments.items():
        art_label = f"Artikel {instr['defining_article']}"
        xml_art = xml_root.find(f".//artikel[@label='{art_label}']")
        status = "FOUND" if xml_art is not None else "NOT FOUND"
        if xml_art is None:
            issues.append(f"{key}: article {art_label} not found")
        print(f"   {instr['name']}: Art. {instr['defining_article']} - {status}")

    # 2. Check source_text is populated
    print(f"\n2. Source text check:")
    empty_source = [k for k, v in instruments.items() if not v.get('source_text')]
    if empty_source:
        print(f"   STATUS: WARN - {len(empty_source)} instruments without source_text")
        for es in empty_source:
            print(f"      - {es}")
            issues.append(f"{es}: no source_text")
    else:
        print("   STATUS: PASS - all instruments have source_text")

    # 3. Check bevoegd_gezag values
    print(f"\n3. Bevoegd gezag check:")
    valid_bg = {'gemeente', 'provincie', 'rijk', 'waterschap'}
    for key, instr in instruments.items():
        bg = set(instr.get('bevoegd_gezag', []))
        invalid = bg - valid_bg
        if invalid:
            print(f"   {key}: invalid bevoegd_gezag: {invalid}")
            issues.append(f"{key}: invalid bevoegd_gezag")
    print(f"   STATUS: {'PASS' if not any('bevoegd_gezag' in i for i in issues) else 'FAIL'}")

    # 4. Count check
    print(f"\n4. Instrument count:")
    print(f"   Total instruments: {len(instruments)}")
    by_type = {}
    for instr in instruments.values():
        t = instr['type']
        by_type[t] = by_type.get(t, 0) + 1
    for t, c in by_type.items():
        print(f"      - {t}: {c}")

    return len(issues) == 0, issues


def verify_external_systems(external_path):
    """Verify external systems file."""
    print("\n" + "=" * 50)
    print("EXTERNAL SYSTEMS VERIFICATION")
    print("=" * 50)

    data = load_yaml(external_path)
    systems = data.get('external_systems', {})
    issues = []

    print(f"\n1. External systems count: {len(systems)}")
    for key, sys in systems.items():
        bwb = sys.get('bwb_id', 'N/A')
        status = sys.get('integration_status', 'unknown')
        print(f"   - {key}: {sys.get('name', '?')} (BWB: {bwb}, status: {status})")

    # Check required fields
    print(f"\n2. Required fields check:")
    for key, sys in systems.items():
        if not sys.get('bwb_id'):
            issues.append(f"{key}: missing bwb_id")
            print(f"   {key}: MISSING bwb_id")

    if not issues:
        print("   STATUS: PASS")

    return len(issues) == 0, issues


def main():
    project_dir = Path(__file__).parent.parent
    xml_path = project_dir / 'source' / 'Omgevingswet.xml'

    print("Loading XML source...")
    tree = etree.parse(str(xml_path))
    root = tree.getroot()

    all_passed = True
    all_issues = []

    # Verify definitions
    defs_ok, defs_issues = verify_definitions(
        root,
        project_dir / 'infra' / 'definitions.yaml'
    )
    all_passed &= defs_ok
    all_issues.extend(defs_issues)

    # Verify instruments
    instr_ok, instr_issues = verify_instruments(
        root,
        project_dir / 'infra' / 'instruments.yaml'
    )
    all_passed &= instr_ok
    all_issues.extend(instr_issues)

    # Verify external systems
    ext_ok, ext_issues = verify_external_systems(
        project_dir / 'infra' / 'external-systems.yaml'
    )
    all_passed &= ext_ok
    all_issues.extend(ext_issues)

    # Summary
    print("\n" + "=" * 50)
    print("VERIFICATION SUMMARY")
    print("=" * 50)

    if all_passed:
        print("\nALL VERIFICATIONS PASSED")
    else:
        print(f"\nISSUES FOUND: {len(all_issues)}")
        for issue in all_issues:
            print(f"  - {issue}")

    return all_passed


if __name__ == '__main__':
    import sys
    success = main()
    sys.exit(0 if success else 1)
