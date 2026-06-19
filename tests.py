import tempfile
import unittest
from pathlib import Path
import main


class DatasetPassportTest(unittest.TestCase):
    def test_duplicate_and_email_detection(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "data.jsonl"
            path.write_text('{"text":"a@example.com","source":"x"}\n{"text":"a@example.com","source":"x"}\n', encoding="utf-8")
            report = main.audit(str(path), ["text"])
            self.assertEqual(report["duplicate_records"], 1)
            self.assertEqual(report["pii_findings"]["email"], 2)


if __name__ == "__main__":
    unittest.main()
