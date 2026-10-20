"""Small, dependency-free checks for tabular datasets."""

from collections.abc import Iterable, Mapping, Sequence
from typing import Any


def validate_required_columns(
    headers: Sequence[str],
    required_columns: Sequence[str],
) -> list[str]:
    """Return required column names that are absent, preserving requested order."""
    available = set(headers)
    return [column for column in required_columns if column not in available]


def missing_value_counts(
    rows: Iterable[Mapping[str, Any]],
) -> dict[str, int]:
    """Count empty or missing values in each column encountered."""
    counts: dict[str, int] = {}

    for row in rows:
        for column, value in row.items():
            counts.setdefault(column, 0)
            if value is None or (isinstance(value, str) and not value.strip()):
                counts[column] += 1

    return counts


def duplicate_row_numbers(
    rows: Iterable[Mapping[str, Any]],
) -> list[int]:
    """Return 1-based data-row numbers for duplicate rows after their first occurrence."""
    seen: set[tuple[tuple[str, Any], ...]] = set()
    duplicates: list[int] = []

    for row_number, row in enumerate(rows, start=1):
        key = tuple(sorted(row.items()))
        if key in seen:
            duplicates.append(row_number)
        else:
            seen.add(key)

    return duplicates


def profile_rows(rows: Iterable[Mapping[str, Any]]) -> dict[str, Any]:
    """Return a compact quality report for a collection of row mappings."""
    materialized = list(rows)
    columns = sorted({column for row in materialized for column in row})

    return {
        "row_count": len(materialized),
        "columns": columns,
        "missing_values": missing_value_counts(materialized),
        "duplicate_rows": duplicate_row_numbers(materialized),
    }
