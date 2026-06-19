import json
import tempfile
import unittest
from pathlib import Path

import main


class DatasetAuditTest(unittest.TestCase):
    def test_report_contains_version_checksum_and_coverage(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "data.jsonl"
            path.write_text(
                json.dumps({"id": "1", "text": "hello", "source": "demo"}) + "\n",
                encoding="utf-8",
            )
            report = main.audit(str(path), ["id", "text", "source"], "MIT")
        self.assertEqual(report["report_version"], 1)
        self.assertEqual(len(report["input"]["checksum"]), 64)
        self.assertEqual(report["field_coverage"]["source"], 1.0)

    def test_exact_overlap_comparison(self):
        with tempfile.TemporaryDirectory() as directory:
            first = Path(directory) / "first.jsonl"
            second = Path(directory) / "second.jsonl"
            first.write_text('{"id":"1","text":"same"}\n{"id":"2","text":"first"}\n', encoding="utf-8")
            second.write_text('{"id":"1","text":"same"}\n{"id":"3","text":"second"}\n', encoding="utf-8")
            result = main.compare_datasets(str(first), str(second))
        self.assertEqual(result["exact_overlap_records"], 1)
        self.assertEqual(result["overlap_rate_of_smaller_set"], 0.5)

    def test_json_array_rejects_non_object_records(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "data.json"
            path.write_text('[{"id":"1"}, "invalid"]', encoding="utf-8")
            with self.assertRaises(ValueError):
                list(main.iter_records(str(path)))


if __name__ == "__main__":
    unittest.main()
