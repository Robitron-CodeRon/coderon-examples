import copy
import json
from pathlib import Path
import unittest
import tempfile
import shutil
from validate_presentation import validate_item

ROOT = Path(__file__).resolve().parents[1]
ENTRY = json.loads((ROOT / 'examples/nextron-led-cycle/catalog-entry.pending.json').read_text(encoding='utf-8'))


class PresentationTests(unittest.TestCase):
    def test_real_entry(self):
        validate_item(ROOT, ENTRY)

    def test_optional_legacy_entry(self):
        e = copy.deepcopy(ENTRY)
        e.pop('preview')
        e.pop('codeGuide')
        validate_item(ROOT, e)

    def test_bad_preview(self):
        for key, value in [('color', 'url(evil)'), ('durationMs', 199), ('durationMs', True), ('label', '')]:
            with self.subTest(key=key, value=value):
                e = copy.deepcopy(ENTRY)
                e['preview']['steps'][0][key] = value
                with self.assertRaises(ValueError):
                    validate_item(ROOT, e)

    def test_long_preview(self):
        e = copy.deepcopy(ENTRY)
        e['preview']['steps'] = [dict(label='Long', color='#ffffff', durationMs=10000)] * 7
        with self.assertRaises(ValueError):
            validate_item(ROOT, e)

    def test_bad_guide(self):
        for key, value in [('path', '../outside.json'), ('path', '/etc/passwd'), ('path', 'a\\b'), ('path', '%2e%2e/x'), ('sizeBytes', 128001), ('sha256', '0'*64), ('sizeBytes', 1)]:
            with self.subTest(key=key):
                e = copy.deepcopy(ENTRY)
                e['codeGuide'][key] = value
                with self.assertRaises(ValueError):
                    validate_item(ROOT, e)


    def test_source_symlink_escape(self):
        with tempfile.TemporaryDirectory() as workspace:
            root = Path(workspace) / 'repo'
            folder = root / 'examples/nextron-led-cycle'
            shutil.copytree(ROOT / 'examples/nextron-led-cycle', folder)
            source = folder / 'NextronLed.ino'
            outside = Path(workspace) / 'outside.ino'
            outside.write_bytes(source.read_bytes())
            source.unlink()
            source.symlink_to(outside)
            with self.assertRaises(ValueError):
                validate_item(root, ENTRY)


if __name__ == '__main__':
    unittest.main()
