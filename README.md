# EHR Data Quality Audit Automation

> **Portfolio demonstration | Synthetic / fictional data only**

Audits synthetic patient demographics and encounters for missing identifiers, duplicate IDs, invalid dates, and future-dated visits.

## What this demonstrates
- Run configurable record-level checks
- Produce machine-readable exception reports
- Document remediation priorities

## Quick start
```bash
python src/main.py
python -m unittest discover -s tests
```

Python 3.10+ is recommended. Core functionality uses the Python standard library; no API keys or patient records are required. Run commands from the repository root.

## Repository contents
- `data/`: fictional patient and encounter CSVs
- `src/main.py`: auditing checks
- `output/issues.csv`: generated issue register

## Relevant skills
Python, data integrity, EHR, clinical analytics, auditability

## Data and privacy
All records, facilities, identifiers, events and organizations in this repository are fabricated for demonstrations. This is **not** a production clinical system and does not contain real protected health information (PHI). Do not upload real patient data or confidential employer files. Outputs do not substitute for clinical, privacy, security, or regulatory review.

## How to discuss in an interview
Explain the input, validations or transformations, measurable outputs, tests, and what you would change for a real deployment (authentication, audit logs, monitoring, regulatory review, and secure storage). Describe this as a **personal portfolio project**, not as an implementation at an employer.

## License
MIT — see [LICENSE](LICENSE).
