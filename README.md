# Dataset Quality Checker

A small, dependency-free Python toolkit for checking tabular dataset quality.

## Features

- Identify required columns that are missing.
- Count empty strings, whitespace-only strings, and `None` values.
- Find repeated rows while retaining the first occurrence.
- Produce a compact report containing row count, columns, missing values, and duplicate rows.

## Quick start

Python 3.10 or newer is required.

```python
from dataset_quality_checker import profile_rows, validate_required_columns

rows = [
    {"name": "Asha", "email": ""},
    {"name": "Ravi", "email": "ravi@example.com"},
]

print(validate_required_columns(rows[0].keys(), ["name", "email", "age"]))
print(profile_rows(rows))
```

## Run tests

From the repository root:

```bash
python -m unittest discover -s tests -v
```

The test suite uses Python's standard library and does not require a test framework.

## Scope and limitations

These utilities work on in-memory mappings. They do not infer data types, modify source data, or replace domain-specific validation rules.
