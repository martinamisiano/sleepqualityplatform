
from core.analyzer import SleepAnalyzer

def test_total_and_eval():
    a = SleepAnalyzer(400, [(10,100,50,240)])
    assert a.count_good() >= 0
    assert a.evaluate((10,100,50,240)) in ["SCADENTE","DISCRETA","BUONA","ECCELLENTE"]
