import sys,unittest
from datetime import date
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from main import audit,date_problem
class QualityTests(unittest.TestCase):
 def test_invalid(self):self.assertEqual(date_problem('xyz',date(2026,1,1)),'invalid_date')
 def test_future(self):self.assertEqual(date_problem('2099-01-01',date(2026,1,1)),'future_date')
 def test_empty(self):self.assertEqual(audit([],[],date(2026,1,1)),[])
