"""Check local suite records, links, pilot resources and generated consistency."""
import json
import re
import sys
import tomllib
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote
from compile_blueslate import ROOT, compile_tokens, load_tokens


def validate(root):
    errors = []
    counts = dict(toml=0, json=0, xaml=0, links=0)
    for p in root.rglob('*'):
        if not p.is_file() or '__pycache__' in p.parts:
            continue
        try:
            if p.suffix == '.toml':
                tomllib.loads(p.read_text(encoding='utf-8-sig'))
                counts['toml'] += 1
            elif p.suffix == '.json':
                json.loads(p.read_text(encoding='utf-8-sig'))
                counts['json'] += 1
            elif p.suffix == '.xaml':
                tree = ET.parse(p)
                counts['xaml'] += 1
                for elem in tree.iter():
                    source = elem.get('Source')
                    if elem.tag.endswith('ResourceDictionary') and source and not (p.parent/source).is_file():
                        errors.append(f'{p.relative_to(root)}: missing dictionary {source}')
            elif p.suffix == '.md':
                for href in re.findall(r'\]\(([^)]+)\)', p.read_text(encoding='utf-8-sig')):
                    target = unquote(href.strip('<>').split('#')[0])
                    if not target or re.match(r'\w+:', target):
                        continue
                    counts['links'] += 1
                    if not (p.parent/target).exists():
                        errors.append(f'{p.relative_to(root)}: broken Markdown link {target}')
        except (ValueError, ET.ParseError) as exc:
            errors.append(f'{p.relative_to(root)}: {exc}')
    manifest = tomllib.loads((root/'BlueSlate.manifest.toml').read_text(encoding='utf-8-sig'))
    data = load_tokens(root/'spec/tokens/BlueSlate.Tokens.toml')
    version = data['meta']['version']
    if manifest['standard']['version'] != version:
        errors.append('Manifest and token versions differ')
    for name in ('README.md','spec/BlueSlate.DesignSystem.md','spec/BlueSlate.Overview.md'):
        if version not in (root/name).read_text(encoding='utf-8'):
            errors.append(f'{name}: missing current source version')
    for group in ('artifacts','documentation'):
        for key, value in manifest[group].items():
            for path in value if isinstance(value, list) else [value]:
                if path and not (root/path).exists():
                    errors.append(f'{group}.{key}: missing {path}')
    for key in ('framework_notes','starter_packs','visual_references','agent_skill','adoption_template'):
        value = manifest['deliverables'][key]
        for path in value if isinstance(value, list) else [value]:
            if not (root/path).exists():
                errors.append(f'deliverables.{key}: missing {path}')
    # Static resource lookup across each baseline pilot, excluding the separate local profile.
    for framework in ('wpf','winui'):
        keys, references = set(), set()
        for p in (root/'starter-packs'/framework).rglob('*.xaml'):
            if 'FileCabinetPilot' in p.name:
                continue
            text = p.read_text(encoding='utf-8')
            keys.update(re.findall(r'x:Key="([^"]+)"', text))
            references.update(re.findall(r'\{(?:StaticResource|ThemeResource) ([^}]+)\}', text))
        for missing in references-keys:
            errors.append(f'{framework}: unresolved pilot resource {missing}')
    template = tomllib.loads((root/'templates/BlueSlate-Adoption.toml').read_text())
    if template['governance']['visual_system']['adoption_level'] not in ('pilot','active','project-profile'):
        errors.append('Invalid adoption level in template')
    compile_tokens(root/'spec/tokens/BlueSlate.Tokens.toml', root/'generated', check=True)
    return counts, errors


if __name__ == '__main__':
    counts, errors = validate(Path(sys.argv[1]).resolve() if len(sys.argv)>1 else ROOT)
    print(json.dumps(dict(status='fail' if errors else 'pass', counts=counts, errors=errors), indent=2))
    sys.exit(bool(errors))
