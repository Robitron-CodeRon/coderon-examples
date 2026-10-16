"""Synthetic bytes exist only in temporary test directories, never in the catalog."""
import copy
import hashlib
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from tools.validate_catalog import validate

ROOT = Path(__file__).resolve().parents[1]


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copy(ROOT / 'catalog.schema.json', self.root)
        (self.root / 'description.md').write_text('Synthetic test fixture')
        (self.root / 'bytes.bin').write_bytes(b'fixture bytes')
        self.item = {
            'id': 'test.fixture', 'title': 'Fixture', 'summary': 'Test only',
            'topic': 'test', 'tags': [], 'difficulty': 'beginner',
            'version': '1.0.0', 'language': 'tr', 'kind': 'general',
            'compatibleBoards': [], 'hardware': [], 'libraries': [],
            'coderon': {'requirements': [], 'support': []},
            'descriptionPath': 'description.md', 'imagePaths': [],
            'package': {'path': 'bytes.bin', 'format': 'test-only',
                        'sizeBytes': 13, 'sha256': hashlib.sha256(b'fixture bytes').hexdigest()},
            'license': {'status': 'undecided'},
            'validation': {name: {'status': 'unverified', 'details': 'Not executed'}
                           for name in ('build', 'hardware')},
        }

    def run_catalog(self, items=None, **overrides):
        data = {'schemaVersion': 1, 'examples': [self.item] if items is None else items}
        data.update(overrides)
        (self.root / 'catalog.json').write_text(json.dumps(data))
        return validate(self.root)

    def test_empty_and_valid_catalog(self):
        self.assertEqual([], self.run_catalog([]))
        self.assertEqual([], self.run_catalog())

    def test_schema_rejects_invalid_data(self):
        for mutation in ('missing', 'type', 'unknown', 'hash'):
            with self.subTest(mutation=mutation):
                item = copy.deepcopy(self.item)
                if mutation == 'missing': del item['title']
                if mutation == 'type': item['package']['sizeBytes'] = '13'
                if mutation == 'unknown': item['unknown'] = True
                if mutation == 'hash': item['package']['sha256'] = 'no'
                self.assertTrue(self.run_catalog([item]))
        self.assertTrue(self.run_catalog(schemaVersion=2))

    def test_duplicate_ids(self):
        self.assertTrue(any('Yinelenen kimlik' in e for e in self.run_catalog([self.item, self.item])))

    def test_unsafe_paths(self):
        for path in ('../outside', '/etc/passwd', 'a/../../x', 'a/./x',
                     'a//x', 'C:/x', 'https://example.com/x', 'a\\x',
                     '%2e%2e/x', 'bytes.bin?x', 'bytes.bin#x'):
            with self.subTest(path=path):
                self.item['descriptionPath'] = path
                self.assertTrue(self.run_catalog())

    def test_symlink_escape(self):
        (self.root / 'escape').symlink_to(self.root.parent)
        self.item['descriptionPath'] = 'escape/outside'
        self.assertTrue(any('Depo dışına' in e for e in self.run_catalog()))

    def test_missing_files(self):
        for target in ('descriptionPath', 'imagePaths', 'package', 'license', 'validation'):
            with self.subTest(target=target):
                item = copy.deepcopy(self.item)
                if target == 'descriptionPath': item[target] = 'missing'
                if target == 'imagePaths': item[target] = ['missing']
                if target == 'package': item[target]['path'] = 'missing'
                if target == 'license': item[target]['path'] = 'missing'
                if target == 'validation': item[target]['build']['evidencePath'] = 'missing'
                self.assertTrue(self.run_catalog([item]))

    def test_integrity(self):
        self.item['package']['sizeBytes'] += 1
        self.assertTrue(any('boyutu' in e for e in self.run_catalog()))
        self.item['package']['sizeBytes'] -= 1
        (self.root / 'bytes.bin').write_bytes(b'altered bytes')
        self.assertTrue(any('SHA-256' in e for e in self.run_catalog()))

    def test_evidence_and_license(self):
        self.item['validation']['build']['status'] = 'passed'
        self.assertTrue(any('evidencePath' in e for e in self.run_catalog()))
        self.item['validation']['build']['evidencePath'] = 'description.md'
        self.assertEqual([], self.run_catalog())
        self.item['license']['status'] = 'declared'
        self.assertTrue(any('identifier' in e for e in self.run_catalog()))

    def test_support_references(self):
        self.item['coderon']['support'] = [{
            'boardId': 'nonexistent', 'platform': 'pc', 'coderonVersionRange': 'unknown',
            'compile': {'status': 'unverified', 'details': 'No test'},
            'upload': {'status': 'unverified', 'details': 'No test'},
        }]
        self.assertTrue(any('tanımlanmamış' in e for e in self.run_catalog()))
        self.assertTrue(any('gereksinimi' in e for e in self.run_catalog()))


if __name__ == '__main__':
    unittest.main()
