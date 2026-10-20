"""Validate optional educational metadata without executing code or networking."""
from pathlib import Path
import argparse
import hashlib
import json
import re


def check(value, message):
    if not value:
        raise ValueError(message)


def local(root, name):
    check(isinstance(name, str) and name and not re.search(r'[\\:%?#\x00-\x1f]', name)
          and all(p not in ('', '.', '..') for p in name.split('/')), 'Unsafe guide path')
    target = (root / name).resolve()
    check(target.is_relative_to(root.resolve()) and target.is_file(), 'Missing/outside guide file')
    return target


def validate_item(root, item):
    if 'preview' in item:
        p = item['preview']
        check(isinstance(p, dict) and set(p) <= {'type', 'board', 'caption', 'steps'}, 'Unknown preview field')
        check(p.get('type') == 'led-sequence' and p.get('board') in ('NEXTRON', 'GENERIC'), 'Invalid preview type/board')
        if 'caption' in p:
            check(isinstance(p['caption'], str) and 0 < len(p['caption']) <= 240, 'Invalid caption')
        steps = p.get('steps')
        check(isinstance(steps, list) and 2 <= len(steps) <= 16, 'Invalid steps')
        total = 0
        for s in steps:
            check(isinstance(s, dict) and set(s) == {'label', 'color', 'durationMs'}, 'Invalid step fields')
            check(isinstance(s['label'], str) and 0 < len(s['label']) <= 40, 'Invalid step label')
            check(isinstance(s['color'], str) and re.fullmatch(r'#[a-fA-F0-9]{6}', s['color']), 'Invalid color')
            check(type(s['durationMs']) is int and 200 <= s['durationMs'] <= 10000, 'Invalid duration')
            total += s['durationMs']
        check(total <= 60000, 'Sequence too long')
    if 'codeGuide' not in item:
        return
    meta = item['codeGuide']
    check(isinstance(meta, dict) and set(meta) == {'path', 'sizeBytes', 'sha256'}, 'Invalid guide fields')
    check(type(meta['sizeBytes']) is int and 0 < meta['sizeBytes'] <= 128000, 'Invalid guide size')
    check(isinstance(meta['sha256'], str) and re.fullmatch(r'[a-f0-9]{64}', meta['sha256']), 'Invalid guide digest')
    target = local(root, meta['path'])
    check(target.stat().st_size == meta['sizeBytes'], 'Guide size mismatch')
    raw = target.read_bytes()
    check(hashlib.sha256(raw).hexdigest() == meta['sha256'], 'Guide SHA-256 mismatch')
    g = json.loads(raw.decode('utf-8'))
    check(g.get('schemaVersion') == 1 and g.get('projectSha256') == item['package']['sha256'], 'Guide project mismatch')
    check(isinstance(g.get('file'), str) and re.fullmatch(r'[A-Za-z_][\w.-]*\.ino', g['file']), 'Invalid source name')
    check(isinstance(g.get('source'), str) and hashlib.sha256(g['source'].encode('utf-8')).hexdigest() == g.get('sourceSha256'), 'Source hash mismatch')
    lines = g['source'].replace('\r\n', '\n').replace('\r', '\n').removesuffix('\n').split('\n')
    notes = g.get('explanations')
    check(len(lines) <= 1000 and isinstance(notes, list) and len(notes) == len(lines), 'Line count mismatch')
    check(all(isinstance(n, str) and len(n) <= 1000 and (not line.strip() or n.strip()) for line, n in zip(lines, notes)), 'Missing line explanation')
    project_raw = local(root, item['package']['path']).read_bytes()
    check(hashlib.sha256(project_raw).hexdigest() == g['projectSha256'], 'Project hash mismatch')
    project = json.loads(project_raw)
    check(project.get('files', {}).get(g['file']) == g['source'], 'Explained source differs from package')
    source_path = (target.parent / g['file']).relative_to(root.resolve()).as_posix()
    check(local(root, source_path).read_bytes() == g['source'].encode('utf-8'), 'Standalone source mismatch')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--entry', type=Path, help='Validate one pending entry instead of the live catalog')
    args = parser.parse_args()
    items = [json.loads(args.entry.read_text(encoding='utf-8'))] if args.entry else json.loads((args.root / 'catalog.json').read_text(encoding='utf-8'))['examples']
    for item in items:
        validate_item(args.root.resolve(), item)
    print('PASS optional presentation metadata and exact guide/package source integrity:', len(items), 'entries')


if __name__ == '__main__':
    main()
