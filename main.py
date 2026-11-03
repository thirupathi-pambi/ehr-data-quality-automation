import csv
from collections import Counter
from datetime import date
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def date_problem(value, today):
    if not value:return 'missing_date'
    try: d=date.fromisoformat(value)
    except ValueError:return 'invalid_date'
    return 'future_date' if d>today else None

def audit(patients, encounters, today):
    patients=list(patients);encounters=list(encounters);issues=[]
    ids=Counter(p['patient_id'] for p in patients if p['patient_id'])
    for p in patients:
        pid=p['patient_id']
        if not pid: issues.append(('patient',pid,'missing_patient_id'))
        if pid and ids[pid]>1:issues.append(('patient',pid,'duplicate_patient_id'))
        if not p['first_name'] or not p['last_name']:issues.append(('patient',pid,'missing_name'))
        problem=date_problem(p['birth_date'],today)
        if problem:issues.append(('patient',pid,'birth_'+problem))
    for e in encounters:
        eid=e['encounter_id']
        if not e['patient_id'] or e['patient_id'] not in ids:issues.append(('encounter',eid,'unmatched_patient_id'))
        problem=date_problem(e['encounter_date'],today)
        if problem:issues.append(('encounter',eid,'encounter_'+problem))
    return issues

def main():
    with (ROOT/'data/patients.csv').open() as f:p=list(csv.DictReader(f))
    with (ROOT/'data/encounters.csv').open() as f:e=list(csv.DictReader(f))
    issues=audit(p,e,date.today())
    out=ROOT/'output/issues.csv';out.parent.mkdir(exist_ok=True)
    with out.open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['entity','record_id','issue']);w.writerows(issues)
    print(f'{len(issues)} data quality findings saved to {out}')
if __name__=='__main__':main()
