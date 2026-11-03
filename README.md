# EHR Data Quality Audit Automation

![Python](https://img.shields.io/badge/python-3.10%2B-blue) ![License](https://img.shields.io/badge/license-MIT-green)

A Python audit script that scans patient and encounter data for common integrity problems and produces an issue register you can hand to a data owner for remediation.

> Built on synthetic data only. No real patient information is included.

## Why this exists

Reporting is only as trustworthy as the underlying EHR data. Missing identifiers, duplicate IDs, and impossible dates quietly corrupt dashboards and downstream interfaces. This project automates the first-pass checks so problems are found and tracked instead of discovered in a report.

## What it checks

- Missing patient or encounter identifiers
- Duplicate IDs
- Invalid dates
- Future-dated visits

Every finding is written as a row in an issue register CSV so it can be triaged, assigned, and re-checked after fixes.

## Project structure

```
.
├── data/
│   ├── patients.csv           # fictional patient demographics
│   └── encounters.csv         # fictional encounters
├── src/
│   └── main.py                # audit checks and issue register export
├── tests/
│   └── test_main.py
├── output/
│   └── issues.csv             # generated issue register
├── LICENSE
└── README.md
```

## Quick start

Requires Python 3.10+ (standard library only). Run from the repository root.

```bash
python src/main.py                      # writes output/issues.csv
python -m unittest discover -s tests
```

## Limitations and next steps

- Rules are fixed in code; a production version would load them from configuration.
- Checks are record-level only; cross-record rules (for example overlapping encounters) are not covered.
- Possible extensions: severity levels, trend reporting across runs, a SQL data source in place of CSV, and scheduled runs with alerting.

## License

MIT. See [LICENSE](LICENSE).
