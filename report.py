
from html import escape
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm

REPORT_DIR = Path(__file__).resolve().parent.parent / "reports" / "generated"
REPORT_DIR.mkdir(parents=True, exist_ok=True)

def html_report(data):
    cats = "".join(f"<tr><td>{escape(k)}</td><td>{v:.0f}</td></tr>" for k,v in data["category_scores"].items())
    findings = "".join(f"<li><b>{escape(f['severity'])}</b> — {escape(f['description'])}</li>" for f in data["findings"][:15])
    recs = "".join(f"<li><b>{escape(r['priority'])}</b> — {escape(r['recommendation'])}</li>" for r in data["recommendations"][:15])
    return f"""<!doctype html><html><head><meta charset='utf-8'><title>Privacy Assessment</title>
    <style>body{{font-family:Arial,sans-serif;max-width:900px;margin:40px auto;line-height:1.5}}
    .score{{font-size:42px;font-weight:bold}}table{{border-collapse:collapse;width:100%}}
    td,th{{border:1px solid #ddd;padding:8px;text-align:left}}.note{{background:#f5f5f5;padding:14px}}</style></head>
    <body><h1>Social Media Privacy Risk Assessment</h1>
    <p><b>Assessment ID:</b> {escape(data['assessment_id'])}<br>
    <b>Date:</b> {escape(data['created_at'])}</p>
    <div class='score'>{data['overall_score']:.0f}/100 — {escape(data['risk_level'])}</div>
    <h2>Category Scores</h2><table><tr><th>Category</th><th>Risk</th></tr>{cats}</table>
    <h2>Top Findings</h2><ul>{findings or '<li>No major findings.</li>'}</ul>
    <h2>Recommendations</h2><ul>{recs or '<li>No recommendations.</li>'}</ul>
    <h2>Privacy Checklist</h2><ul>
    <li>Review profile visibility</li><li>Hide unnecessary contact information</li>
    <li>Review location sharing and geotags</li><li>Review tagging permissions</li>
    <li>Verify unfamiliar requests</li><li>Enable MFA and login alerts</li>
    <li>Review active sessions and connected apps</li><li>Review old public posts</li>
    <li>Never share verification codes</li></ul>
    <div class='note'><b>Educational disclaimer:</b> This score is a framework simulation based on self-reported answers.
    It is not a guarantee of compromise or safety and should not be treated as a professional security verdict.</div>
    </body></html>"""

def make_pdf(data):
    path = REPORT_DIR / f"{data['assessment_id']}.pdf"
    doc = SimpleDocTemplate(str(path), pagesize=A4, rightMargin=15*mm,leftMargin=15*mm,topMargin=15*mm,bottomMargin=15*mm)
    styles = getSampleStyleSheet()
    story = [Paragraph("Social Media Privacy Risk Assessment", styles["Title"]),
             Paragraph(f"Assessment ID: {escape(data['assessment_id'])}", styles["Normal"]),
             Paragraph(f"Risk: {data['overall_score']:.0f}/100 — {escape(data['risk_level'])}", styles["Heading2"]),
             Spacer(1, 8)]
    rows = [["Category","Score"]] + [[k, f"{v:.0f}"] for k,v in data["category_scores"].items()]
    t = Table(rows, repeatRows=1)
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),colors.lightgrey),("GRID",(0,0),(-1,-1),0.5,colors.grey)]))
    story += [t, Spacer(1,10), Paragraph("Top Findings", styles["Heading2"])]
    for f in data["findings"][:15]:
        story.append(Paragraph(f"- {escape(f['severity'])}: {escape(f['description'])}", styles["BodyText"]))
    story.append(Paragraph("Recommendations", styles["Heading2"]))
    for r in data["recommendations"][:15]:
        story.append(Paragraph(f"- {escape(r['priority'])}: {escape(r['recommendation'])}", styles["BodyText"]))
    story.append(Spacer(1,10))
    story.append(Paragraph("Educational disclaimer: framework simulation only; not a guarantee of safety or compromise.", styles["BodyText"]))
    doc.build(story)
    return path
