
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "privacy_assessment.db"

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS assessments (
        assessment_id TEXT PRIMARY KEY,
        overall_score REAL NOT NULL,
        risk_level TEXT NOT NULL,
        created_at TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS category_scores (
        category_score_id INTEGER PRIMARY KEY AUTOINCREMENT,
        assessment_id TEXT NOT NULL,
        category TEXT NOT NULL,
        score REAL NOT NULL,
        FOREIGN KEY(assessment_id) REFERENCES assessments(assessment_id)
    );
    CREATE TABLE IF NOT EXISTS findings (
        finding_id INTEGER PRIMARY KEY AUTOINCREMENT,
        assessment_id TEXT NOT NULL,
        category TEXT NOT NULL,
        finding_type TEXT NOT NULL,
        severity TEXT NOT NULL,
        description TEXT NOT NULL,
        FOREIGN KEY(assessment_id) REFERENCES assessments(assessment_id)
    );
    CREATE TABLE IF NOT EXISTS recommendations (
        recommendation_id INTEGER PRIMARY KEY AUTOINCREMENT,
        assessment_id TEXT NOT NULL,
        category TEXT NOT NULL,
        priority TEXT NOT NULL,
        recommendation TEXT NOT NULL,
        FOREIGN KEY(assessment_id) REFERENCES assessments(assessment_id)
    );
    """)
    conn.commit()
    conn.close()

def save_assessment(assessment_id, result, created_at):
    conn = get_conn()
    conn.execute("INSERT INTO assessments VALUES (?,?,?,?)",
                 (assessment_id, result["overall_score"], result["risk_level"], created_at))
    for category, score in result["category_scores"].items():
        conn.execute("INSERT INTO category_scores(assessment_id,category,score) VALUES(?,?,?)",
                     (assessment_id, category, score))
    for f in result["findings"]:
        conn.execute("""INSERT INTO findings(assessment_id,category,finding_type,severity,description)
                        VALUES(?,?,?,?,?)""",
                     (assessment_id, f["category"], f["finding_type"], f["severity"], f["description"]))
    for r in result["recommendations"]:
        conn.execute("""INSERT INTO recommendations(assessment_id,category,priority,recommendation)
                        VALUES(?,?,?,?)""",
                     (assessment_id, r["category"], r["priority"], r["recommendation"]))
    conn.commit()
    conn.close()

def get_assessment(assessment_id):
    conn = get_conn()
    a = conn.execute("SELECT * FROM assessments WHERE assessment_id=?", (assessment_id,)).fetchone()
    if not a:
        conn.close()
        return None
    cats = conn.execute("SELECT category,score FROM category_scores WHERE assessment_id=?",
                        (assessment_id,)).fetchall()
    findings = conn.execute("SELECT category,finding_type,severity,description FROM findings WHERE assessment_id=?",
                            (assessment_id,)).fetchall()
    recs = conn.execute("SELECT category,priority,recommendation FROM recommendations WHERE assessment_id=?",
                        (assessment_id,)).fetchall()
    conn.close()
    return {
        "assessment_id": a["assessment_id"], "overall_score": a["overall_score"],
        "risk_level": a["risk_level"], "created_at": a["created_at"],
        "category_scores": {r["category"]: r["score"] for r in cats},
        "findings": [dict(r) for r in findings],
        "recommendations": [dict(r) for r in recs]
    }

def delete_assessment(assessment_id):
    conn = get_conn()
    conn.execute("DELETE FROM recommendations WHERE assessment_id=?", (assessment_id,))
    conn.execute("DELETE FROM findings WHERE assessment_id=?", (assessment_id,))
    conn.execute("DELETE FROM category_scores WHERE assessment_id=?", (assessment_id,))
    cur = conn.execute("DELETE FROM assessments WHERE assessment_id=?", (assessment_id,))
    conn.commit()
    conn.close()
    return cur.rowcount > 0

def stats():
    conn = get_conn()
    total = conn.execute("SELECT COUNT(*) FROM assessments").fetchone()[0]
    avg = conn.execute("SELECT COALESCE(AVG(overall_score),0) FROM assessments").fetchone()[0]
    dist = conn.execute("SELECT risk_level,COUNT(*) c FROM assessments GROUP BY risk_level").fetchall()
    recent = conn.execute("SELECT assessment_id,overall_score,risk_level,created_at FROM assessments ORDER BY created_at DESC LIMIT 10").fetchall()
    conn.close()
    return {"total": total, "avg_score": round(avg,1),
            "distribution": {r["risk_level"]: r["c"] for r in dist},
            "recent": [dict(r) for r in recent]}
