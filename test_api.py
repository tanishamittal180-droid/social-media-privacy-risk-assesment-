
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from backend.app import app
from backend.questionnaire import QUESTIONS

def valid_answers():
    a={}
    for q in QUESTIONS:
        a[q["id"]] = "PRIVATE" if q["type"]=="PUBLIC_FRIENDS_PRIVATE" else ("RARELY" if q["type"]=="OFTEN_SOMETIMES_RARELY" else "NO")
    return a

def test_health():
    c=app.test_client()
    assert c.get("/api/health").status_code==200

def test_questions():
    c=app.test_client()
    r=c.get("/api/questions")
    assert r.status_code==200
    assert len(r.get_json()["questions"])>=40

def test_validation_rejects_missing():
    c=app.test_client()
    r=c.post("/api/assessment",json={"answers":{}})
    assert r.status_code==400

def test_create_assessment():
    c=app.test_client()
    r=c.post("/api/assessment",json={"answers":valid_answers()})
    assert r.status_code==200
    assert r.get_json()["assessment_id"].startswith("PRA-")

def test_dashboard_stats():
    c=app.test_client()
    assert c.get("/api/dashboard/stats").status_code==200

def test_checklist():
    c=app.test_client()
    assert len(c.get("/api/privacy-checklist").get_json()["checklist"])>=15

def test_simulation():
    c=app.test_client()
    answers=valid_answers()
    r=c.post("/api/assessment/simulate-improvement",json={"answers":answers,"changes":{"mfa_enabled":"YES"}})
    assert r.status_code==200
    assert "risk_reduction" in r.get_json()
