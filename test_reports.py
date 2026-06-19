import tempfile
import unittest
from pathlib import Path

import main


class DatasetReportOutputTest(unittest.TestCase):
    def test_blocking_status_for_missing_required_fields(self):
        report = {
            "missing_required": {"source": 2},
            "duplicate_records": 0,
            "pii_findings": {},
            "declared_license": "MIT",
        }
        self.assertEqual(main.report_status(report), "blocking")

    def test_review_status_for_duplicates(self):
        report = {
            "missing_required": {},
            "duplicate_records": 1,
            "pii_findings": {},
            "declared_license": "MIT",
        }
        self.assertEqual(main.report_status(report), "review")

    def test_pass_status_for_clean_report(self):
        report = {
            "missing_required": {},
            "duplicate_records": 0,
            "pii_findings": {"email": 0},
            "declared_license": "MIT",
        }
        self.assertEqual(main.report_status(report), "pass")

    def test_markdown_report_contains_comparison(self):
        report = {
            "report_version": 1,
            "generated_at": "2026-06-20T00:00:00Z",
            "input": {"checksum": "abc"},
            "records": 2,
            "unique_records": 2,
            "duplicate_records": 0,
            "duplicate_rate": 0.0,
            "missing_required": {},
            "pii_findings": {"email": 0},
            "pii_risk": "low",
            "source_traceability": 1.0,
            "declared_license": "MIT",
            "review_status": "pass",
            "comparison": {
                "other_file": "test.jsonl",
                "exact_overlap_records": 1,
                "overlap_rate_of_smaller_set": 0.5,
            },
        }
        content = main.render_markdown(report)
        self.assertIn("# Dataset Passport", content)
        self.assertIn("Exact overlap records: 1", content)
        self.assertIn("Review status: **pass**", content)

    def test_markdown_format_inference_and_write(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "report.md"
            main.write_report(
                {
                    "report_version": 1,
                    "generated_at": "2026-06-20T00:00:00Z",
                    "input": {"checksum": "abc"},
                    "records": 0,
                    "unique_records": 0,
                    "duplicate_records": 0,
                    "missing_required": {},
                    "pii_findings": {},
                    "declared_license": "MIT",
                    "review_status": "pass",
                },
                str(path),
            )
            content = path.read_text(encoding="utf-8")
        self.assertIn("Dataset Passport", content)
        self.assertEqual(main.infer_report_format("report.md"), "markdown")


if __name__ == "__main__":
    unittest.main()
