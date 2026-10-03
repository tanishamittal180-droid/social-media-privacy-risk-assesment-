
from flask import Flask, jsonify, request, send_from_directory, make_response
from datetime import datetime, timezone
from pathlib import Path
import uuid

from backend.db import init_db, save_assessment, get_assessment, delete_assessment, stats
from backend.questionnaire import QUESTIONS
from backend.services.assessment_engine import assess
from backend.services.improvement_simulator import simulate
from backend.report import html_report, make_pdf

BASE = Path(__file__).resolve().parent.parent
app = Flask(__name__, static_folder=str(BASE / "frontend"), static_url_path="")
app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024
init_db()

ALLOWED_VALUES = {
    "PUBLIC_FRIENDS_PRIVATE": {"PUBLIC","FRIENDS","PRIVATE"},
    "YES_NO": {"YES","NO"},
    "OFTEN_SOMETIMES_RARELY": {"OFTEN","SOMETIMES","RARELY"},
}

def validate_answers(answers):
    if not isinstance(answers, dict):
        return ["answers must be an object"]
    errors = []
    for q in QUESTIONS:
        key, typ = q["id"], q["type"]
        if key not in answers:
            errors.append(f"Missing answer: {key}")
        elif str(answers[key]).upper() not in ALLOWED_VALUES[typ]:
            errors.append(f"Invalid value for {key}")
    return errors

@app.get("/")
def home():
    return send_from_directory(BASE / "frontend", "index.html")

@app.get("/assessment")
def assessment_page():
    return send_from_directory(BASE / "frontend", "assessment.html")

@app.get("/dashboard")
def dashboard_page():
    return send_from_directory(BASE / "frontend", "dashboard.html")

@app.get("/api/health")
def health():
    return jsonify({"status":"ok","service":"privacy-risk-framework"})

@app.get("/api/questions")
def questions():
    return jsonify({"questions": QUESTIONS})

@app.post("/api/assessment")
def create_assessment():
    body = request.get_json(silent=True) or {}
    answers = {k: str(v).upper() for k,v in (body.get("answers") or {}).items()}
    errors = validate_answers(answers)
    if errors:
        return jsonify({"error":"Validation failed","details":errors}), 400
    result = assess(answers)
    assessment_id = "PRA-" + uuid.uuid4().hex[:10].upper()
    created = datetime.now(timezone.utc).isoformat()
    save_assessment(assessment_id, result, created)
    return jsonify({"assessment_id": assessment_id, **result, "created_at": created})

@app.get("/api/assessment/<assessment_id>")
def assessment(assessment_id):
    data = get_assessment(assessment_id)
    if not data:
        return jsonify({"error":"Assessment not found"}), 404
    return jsonify(data)

@app.get("/api/assessment/<assessment_id>/recommendations")
def recommendations(assessment_id):
    data = get_assessment(assessment_id)
    if not data:
        return jsonify({"error":"Assessment not found"}), 404
    return jsonify({"assessment_id": assessment_id, "recommendations": data["recommendations"]})

@app.post("/api/assessment/simulate-improvement")
def improvement():
    body = request.get_json(silent=True) or {}
    answers = {k: str(v).upper() for k,v in (body.get("answers") or {}).items()}
    errors = validate_answers(answers)
    if errors:
        return jsonify({"error":"Validation failed","details":errors}), 400
    changes = {k: str(v).upper() for k,v in (body.get("changes") or {}).items()}
    allowed_keys = {q["id"]: q["type"] for q in QUESTIONS}
    for k,v in changes.items():
        if k not in allowed_keys or v not in ALLOWED_VALUES[allowed_keys[k]]:
            return jsonify({"error":f"Invalid simulation change: {k}"}), 400
    return jsonify(simulate(answers, changes))

@app.get("/api/dashboard/stats")
def dashboard_stats():
    return jsonify(stats())

@app.get("/api/privacy-checklist")
def checklist():
    return jsonify({"checklist":[
        "Review profile visibility","Hide unnecessary contact information",
        "Review birth-date visibility","Review location sharing",
        "Avoid unnecessary real-time location posts","Review tagging permissions",
        "Review followers/friends","Verify unfamiliar requests","Enable MFA",
        "Enable login alerts where available","Review active sessions",
        "Review connected apps","Remove unused integrations",
        "Review old public posts","Review photo privacy",
        "Be cautious with unexpected links","Never share verification codes",
        "Review privacy settings periodically"
    ]})

@app.get("/api/report/<assessment_id>/html")
def report_html(assessment_id):
    data = get_assessment(assessment_id)
    if not data: return jsonify({"error":"Assessment not found"}),404
    return make_response(html_report(data), 200, {"Content-Type":"text/html"})

@app.get("/api/report/<assessment_id>/pdf")
def report_pdf(assessment_id):
    data = get_assessment(assessment_id)
    if not data: return jsonify({"error":"Assessment not found"}),404
    path = make_pdf(data)
    return send_from_directory(path.parent, path.name, as_attachment=True)

@app.delete("/api/assessment/<assessment_id>")
def remove_assessment(assessment_id):
    return jsonify({"deleted": delete_assessment(assessment_id)})

if __name__ == "__main__":
    print("Starting Social Media Privacy Risk Assessment Framework...")
    print("Open http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000, debug=True)
