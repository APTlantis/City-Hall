"""Compile the Blue Slate token contract with Python 3.11+ (standard library only)."""
from __future__ import annotations
import argparse
import json
import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LAYERS = ('palette', 'semantic', 'component', 'foundation', 'typography')
REFERENCE = re.compile(r'^\{([^}]+)\}$')


def leaves(node: dict, prefix: str):
    for key, value in node.items():
        path = f'{prefix}.{key}'
        if isinstance(value, dict):
            yield from leaves(value, path)
        else:
            yield path, value


def resolve(data: dict, value, stack=(), color_format='oklch'):
    match = REFERENCE.fullmatch(value) if isinstance(value, str) else None
    if not match:
        return value
    path = match[1]
    if path.split('.')[0] not in LAYERS:
        raise ValueError(f'Reference must target a canonical layer: {path}')
    if path in stack:
        raise ValueError(f'Cyclic token reference: {" -> ".join((*stack, path))}')
    node = data
    for key in path.split('.'):
        if not isinstance(node, dict) or key not in node:
            raise ValueError(f'Unknown token reference: {path}')
        node = node[key]
    if isinstance(node, dict):
        if path.startswith('palette.') and color_format in node:
            return node[color_format]
        raise ValueError(f'Reference resolves to a table, not a value: {path}')
    return resolve(data, node, (*stack, path), color_format)


def load_tokens(source: Path) -> dict:
    data = tomllib.loads(source.read_text(encoding='utf-8-sig'))
    for section in ('meta', 'policy', *LAYERS, 'framework', 'audit'):
        if not isinstance(data.get(section), dict) or not data[section]:
            raise ValueError(f'Missing or empty token table: {section}')
    if data['meta'].get('schema') != 'aptlantis.blue-slate.tokens' or data['meta'].get('schema_version') != '1.0':
        raise ValueError('Unsupported token schema or schema version')
    if data['meta'].get('theme_mode') != 'dark-only':
        raise ValueError('This compiler implements the dark-only Blue Slate contract')
    if not re.fullmatch(r'\d+\.\d+\.\d+', data['meta'].get('version', '')):
        raise ValueError('Expected semantic source version')
    if data['policy'].get('canonical_layers') != list(LAYERS):
        raise ValueError('Canonical layers differ from the supported contract')
    if data['policy'].get('framework_names_are_canonical') is not False:
        raise ValueError('Framework aliases cannot be canonical')
    for name, color in data['palette'].items():
        if not isinstance(color, dict) or not re.fullmatch(r'#[0-9a-fA-F]{6}', color.get('hex', '')):
            raise ValueError(f'Palette {name} requires exact six-digit sRGB hex')
        if not re.fullmatch(r'oklch\([0-9.]+ [0-9.]+ [0-9.]+\)', color.get('oklch', '')) or not color.get('role'):
            raise ValueError(f'Palette {name} requires OKLCH and a role')
    for name in ('tailwind', 'siyuan'):
        if not data['framework'].get(name):
            raise ValueError(f'Missing framework map: {name}')
    for layer in ('semantic', 'component', 'foundation', 'typography', 'framework'):
        for path, value in leaves(data[layer], layer):
            if not isinstance(value, (str, int, float)) or isinstance(value, bool):
                raise ValueError(f'Unsupported token value: {path}')
            resolve(data, value)
    for group in ('normal-text', 'indicators'):
        pairs = data['audit'].get('pairs', {}).get(group)
        if not isinstance(pairs, list) or not pairs:
            raise ValueError(f'Missing audit pairs: {group}')
        for pair in pairs:
            parts = pair.split('|')
            if len(parts) != 2:
                raise ValueError(f'Invalid audit pair: {pair}')
            for path in parts:
                if not re.fullmatch(r'#[0-9a-fA-F]{6}', str(resolve(data, '{' + path + '}', color_format='hex'))):
                    raise ValueError(f'Audit pair must resolve to an opaque palette color: {path}')
    return data


def render(data: dict) -> dict[str, str]:
    version = data['meta']['version']
    header = f'/* Generated from BlueSlate.Tokens.toml v{version}. Do not edit. */'
    css = [header, ':root {', '  color-scheme: dark;']
    for name, value in data['palette'].items():
        prefix = '--bs-palette-' + name.replace('_', '-')
        css.extend(f'  {prefix}{suffix}: {value[key]};' for suffix, key in (('-hex', 'hex'), ('-oklch', 'oklch'), ('', 'oklch')))
    for layer in ('semantic', 'component', 'foundation'):
        for path, value in leaves(data[layer], layer):
            css.append(f'  --bs-{path.replace(".", "-").replace("_", "-")}: {resolve(data, value)};')
    css.extend(f'  --bs-font-{key}: {value};' for key, value in data['typography'].items())
    css.append('}')
    tailwind = [header, '@import "./BlueSlate.Tokens.css";', '@theme {']
    tailwind.extend(f'  --color-bs-{key}: {resolve(data, value)};' for key, value in data['framework']['tailwind'].items())
    tailwind.append('}')
    siyuan = [header, ':root {']
    siyuan.extend(f'  {key}: {resolve(data, value)};' for key, value in data['framework']['siyuan'].items())
    siyuan.append('}')
    compat = dict(version=version, name=data['meta']['name'], canonicalSource='BlueSlate.Tokens.toml', themeMode=data['meta']['theme_mode'])
    compat.update({key: data[key] for key in LAYERS})
    return {
        'BlueSlate.Tokens.css': '\n'.join(css) + '\n',
        'BlueSlate.Tailwind.css': '\n'.join(tailwind) + '\n',
        'BlueSlate.SiYuan.css': '\n'.join(siyuan) + '\n',
        'BlueSlate.Tokens.json': json.dumps(compat, indent=2, ensure_ascii=False) + '\n',
    }


def compile_tokens(source: Path, output: Path, check=False):
    outputs = render(load_tokens(source))
    if check:
        stale = [name for name, content in outputs.items() if not (output / name).is_file() or (output / name).read_bytes() != content.encode('utf-8')]
        if stale:
            raise ValueError('Missing or stale generated outputs: ' + ', '.join(stale))
    else:
        output.mkdir(parents=True, exist_ok=True)
        for name, content in outputs.items():
            (output / name).write_bytes(content.encode('utf-8'))
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=ROOT / 'spec/tokens/BlueSlate.Tokens.toml')
    parser.add_argument('--output', type=Path, default=ROOT / 'generated')
    parser.add_argument('--check', action='store_true', help='Read-only exact-byte freshness and contract check')
    args = parser.parse_args()
    try:
        compile_tokens(args.source, args.output, args.check)
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print(('Checked' if args.check else 'Generated') + f' four outputs from {args.source}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
