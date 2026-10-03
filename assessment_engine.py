
from backend.services.scoring_engine import calculate_privacy_risk
from backend.services.findings_engine import generate_privacy_findings
from backend.services.recommendation_engine import generate_recommendations

def assess(answers):
    result = calculate_privacy_risk(answers)
    findings = generate_privacy_findings(answers)
    recommendations = generate_recommendations(findings)
    return {**result, "findings": findings, "recommendations": recommendations}
