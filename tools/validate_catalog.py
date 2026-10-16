"""Validate metadata and local file integrity; never execute project contents."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import sys
from urllib.parse import unquote

from jsonschema import Draft202012Validator, FormatChecker


def local_file(root, value):
    # Reject URI/drive syntax, encoded traversal, backslashes and noncanonical paths.
    if (not value or unquote(value) != value or '\\' in value or ':' in value
            or '?' in value or '#' in value):
        raise ValueError(f'Geçersiz depo yolu: {value!r}')
    path = PurePosixPath(value)
    if path.is_absolute() or any(p in ('', '.', '..') for p in value.split('/')):
        raise ValueError(f'Geçersiz depo yolu: {value!r}')
    target = (root / value).resolve()
    if not target.is_relative_to(root.resolve()):
        raise ValueError(f'Depo dışına çıkan yol: {value!r}')
    if not target.is_file():
        raise ValueError(f'Dosya bulunamadı: {value!r}')
    return target


def validate(root):
    root = Path(root).resolve()
    schema = json.loads((root / 'catalog.schema.json').read_text())
    catalog = json.loads((root / 'catalog.json').read_text())
    Draft202012Validator.check_schema(schema)
    errors = [f'{list(e.absolute_path)}: {e.message}' for e in
              Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(catalog)]
    if errors:
        return errors
    ids = set()
    for item in catalog['examples']:
        prefix = item['id']
        def error(message):
            errors.append(f'{prefix}: {message}')
        if prefix in ids:
            error('Yinelenen kimlik')
        ids.add(prefix)
        paths = [item['descriptionPath'], *item['imagePaths'], item['package']['path']]
        license_info = item['license']
        if license_info['status'] == 'declared' and not license_info.get('identifier'):
            error('Beyan edilmiş lisans için identifier gerekli')
        if license_info.get('path'):
            paths.append(license_info['path'])
        checks = list(item['validation'].values())
        boards = [b['id'] for b in item['compatibleBoards']]
        if len(boards) != len(set(boards)):
            error('Yinelenen kart kimliği')
        support_keys = set()
        requirements = {r['platform'] for r in item['coderon']['requirements']}
        for support in item['coderon']['support']:
            key = (support['boardId'], support['platform'], support['coderonVersionRange'])
            if key in support_keys:
                error('Yinelenen CodeRon destek kaydı')
            support_keys.add(key)
            if support['boardId'] not in boards:
                error('Destek kaydı tanımlanmamış bir karta başvuruyor')
            if support['platform'] not in requirements:
                error('Destek platformu için CodeRon gereksinimi gerekli')
            checks.extend([support['compile'], support['upload']])
        for check in checks:
            if check['status'] in ('passed', 'failed') and not check.get('evidencePath'):
                error('Test sonucu için evidencePath gerekli')
            if check.get('evidencePath'):
                paths.append(check['evidencePath'])
        for path in paths:
            try:
                local_file(root, path)
            except ValueError as exc:
                error(str(exc))
        try:
            package = local_file(root, item['package']['path'])
            if package.stat().st_size != item['package']['sizeBytes']:
                error('Paket boyutu uyuşmuyor')
            with package.open('rb') as stream:
                digest = hashlib.file_digest(stream, 'sha256').hexdigest()
            if digest != item['package']['sha256']:
                error('Paket SHA-256 uyuşmuyor')
        except ValueError:
            pass  # Already reported in the path checks.
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        errors = validate(args.root)
    except (OSError, ValueError, RecursionError) as exc:
        errors = [str(exc)]
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print('Katalog geçerli (şema, kimlikler, yollar ve paket bütünlüğü).')
    return 0


if __name__ == '__main__':
    sys.exit(main())
