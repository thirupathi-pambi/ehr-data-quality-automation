# EHR Data Quality Audit

This is a Python script that checks patient and encounter data for the kinds of problems that quietly break reports: duplicate IDs, missing names, birth dates in the future, and visits pointing to patients that don't exist. Instead of finding these one by one when a dashboard looks wrong, I wanted a script that finds them all up front and puts them in a list someone can work through.

All the data is made up. There's no real patient information here.

## What it checks

**Patients** (`data/patients.csv`)

- missing patient ID
- duplicate patient ID
- missing first or last name
- birth date that's missing, isn't a real date, or is in the future

**Encounters** (`data/encounters.csv`)

- patient ID that doesn't match anyone in the patient file
- encounter date that's missing, isn't a real date, or is in the future

Every problem the script finds becomes one row in `output/issues.csv`, with the record type, the record ID and the issue code. That way the file can be sorted, assigned to people, and checked again after fixes.

## Running it

You need Python 3.10 or newer. There's nothing to install.

```bash
python src/main.py
python -m unittest discover -s tests
```

Run both commands from the repo root.

## What the sample data shows

I put a problem into most of the sample rows on purpose, to make sure every check actually fires. The script finds 9 issues:

| Entity    | Record | Issue                   |
|-----------|--------|-------------------------|
| patient   | P002   | duplicate_patient_id    |
| patient   | P002   | birth_missing_date      |
| patient   | P002   | duplicate_patient_id    |
| patient   | P004   | missing_name            |
| patient   | P004   | birth_future_date       |
| patient   | P005   | birth_invalid_date      |
| encounter | E002   | unmatched_patient_id    |
| encounter | E003   | encounter_future_date   |
| encounter | E004   | encounter_invalid_date  |

P001 and E001 are the only clean records. They're there to make sure the script doesn't flag good data.

## Some decisions I made

- **Duplicates get flagged on both rows.** P002 shows up twice in the output because there are two different people (Jordan Lee and Pat Reed) with the same ID. You can't tell which one is "right" without looking, so both rows need a review.
- **Missing, invalid and future dates are separate issues.** A blank date is a data entry gap, `not-a-date` is a format problem, and 2030 is probably a typo. Each one gets fixed differently, so each one gets its own code.
- **"Future" means after the day you run it.** The script compares against today's date. That's why the tests pass in a fixed date. Otherwise they could start failing on their own as time passes.
- **Every issue goes into the output.** The script doesn't stop at the first problem in a record. If P004 has two problems, you see both.

## Files

```
data/patients.csv      fictional patient demographics
data/encounters.csv    fictional encounters
src/main.py            audit checks and issue export
tests/test_main.py     unit tests for date checks and empty input
output/issues.csv      generated issue list
```

## What I'd add next

- Checks on encounter IDs themselves (missing or duplicated). Right now the script only checks the patient link and the date.
- Flag encounters that point at a duplicated patient ID. E004 links to P002, and there's no way to know which P002 it means.
- A severity column, so a duplicate ID ranks above a missing first name
- Saving each run's results so I can see if the number of issues goes down over time
