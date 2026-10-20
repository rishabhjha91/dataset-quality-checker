import unittest

from dataset_quality_checker import (
    duplicate_row_numbers,
    missing_value_counts,
    profile_rows,
    validate_required_columns,
)


class DatasetQualityTests(unittest.TestCase):
    def test_required_columns_preserve_requested_order(self):
        self.assertEqual(
            validate_required_columns(["name", "age"], ["id", "age", "email"]),
            ["id", "email"],
        )

    def test_missing_values_count_empty_whitespace_and_none(self):
        rows = [
            {"name": "Asha", "city": ""},
            {"name": None, "city": "Delhi"},
            {"name": " ", "city": None},
        ]
        self.assertEqual(
            missing_value_counts(rows),
            {"name": 2, "city": 2},
        )

    def test_duplicate_rows_report_only_repeated_occurrences(self):
        rows = [
            {"id": "1", "name": "Asha"},
            {"id": "2", "name": "Ravi"},
            {"id": "1", "name": "Asha"},
            {"id": "1", "name": "Asha"},
        ]
        self.assertEqual(duplicate_row_numbers(rows), [3, 4])

    def test_profile_empty_dataset(self):
        self.assertEqual(
            profile_rows([]),
            {
                "row_count": 0,
                "columns": [],
                "missing_values": {},
                "duplicate_rows": [],
            },
        )

    def test_profile_combines_quality_checks(self):
        rows = [
            {"name": "Asha", "email": ""},
            {"name": "Asha", "email": ""},
        ]
        report = profile_rows(rows)
        self.assertEqual(report["row_count"], 2)
        self.assertEqual(report["columns"], ["email", "name"])
        self.assertEqual(report["missing_values"]["email"], 2)
        self.assertEqual(report["duplicate_rows"], [2])


if __name__ == "__main__":
    unittest.main()
