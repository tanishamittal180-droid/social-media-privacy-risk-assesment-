
from backend.services.scoring_engine import calculate_privacy_risk, risk_level
from backend.services.assessment_engine import assess
from backend.questionnaire import QUESTIONS

def private_answers():
    a={}
    for q in QUESTIONS:
        a[q["id"]] = "PRIVATE" if q["type"]=="PUBLIC_FRIENDS_PRIVATE" else ("RARELY" if q["type"]=="OFTEN_SOMETIMES_RARELY" else "NO")
    for k in ["mfa_enabled","unique_password","password_manager","login_alerts","sessions_reviewed","recovery_reviewed",
              "third_party_reviewed","follower_review","privacy_reviewed"]:
        a[k]="YES"
    return a

def public_answers():
    a={}
    for q in QUESTIONS:
        a[q["id"]] = "PUBLIC" if q["type"]=="PUBLIC_FRIENDS_PRIVATE" else ("OFTEN" if q["type"]=="OFTEN_SOMETIMES_RARELY" else "YES")
    return a

def test_fully_private_is_low():
    r=calculate_privacy_risk(private_answers())
    assert r["risk_level"]=="LOW"
    assert r["overall_score"]<=20

def test_public_profile_is_high_or_critical():
    r=calculate_privacy_risk(public_answers())
    assert r["overall_score"]>40

def test_public_phone_increases_personal_info():
    a=private_answers(); base=calculate_privacy_risk(a)["category_scores"]["Personal Information"]
    a["phone_public"]="YES"
    assert calculate_privacy_risk(a)["category_scores"]["Personal Information"]>base

def test_public_location_increases_location():
    a=private_answers(); base=calculate_privacy_risk(a)["category_scores"]["Location Privacy"]
    a["location_public"]="YES"
    assert calculate_privacy_risk(a)["category_scores"]["Location Privacy"]>base

def test_realtime_location_high():
    a=private_answers(); a["realtime_location"]="YES"
    assert calculate_privacy_risk(a)["category_scores"]["Location Privacy"]>=20

def test_travel_posts():
    a=private_answers(); a["travel_posts"]="YES"
    assert calculate_privacy_risk(a)["category_scores"]["Location Privacy"]>0

def test_unknown_connections():
    a=private_answers(); a["unknown_connections"]="OFTEN"
    assert calculate_privacy_risk(a)["category_scores"]["Connections"]>50

def test_tag_review_disabled():
    a=private_answers(); a["tag_review"]="YES"
    assert calculate_privacy_risk(a)["category_scores"]["Tagging"]>0

def test_mfa_disabled_increases_security_risk():
    a=private_answers(); base=calculate_privacy_risk(a)["category_scores"]["Account Security"]
    a["mfa_enabled"]="NO"
    assert calculate_privacy_risk(a)["category_scores"]["Account Security"]>base

def test_login_alerts():
    a=private_answers(); a["login_alerts"]="NO"
    assert calculate_privacy_risk(a)["category_scores"]["Account Security"]>0

def test_third_party_not_reviewed():
    a=private_answers(); a["third_party_reviewed"]="NO"
    assert calculate_privacy_risk(a)["category_scores"]["Third-Party Apps"]>=45

def test_old_posts():
    a=private_answers(); a["old_public_posts"]="YES"
    assert calculate_privacy_risk(a)["category_scores"]["Content Exposure"]>0

def test_social_engineering():
    a=private_answers(); a["unknown_links"]="YES"
    assert calculate_privacy_risk(a)["category_scores"]["Social Engineering"]>0

def test_digital_footprint():
    a=private_answers(); a["privacy_reviewed"]="NO"
    assert calculate_privacy_risk(a)["category_scores"]["Digital Footprint"]>0

def test_score_boundary_low():
    assert risk_level(20)=="LOW"

def test_score_boundary_moderate():
    assert risk_level(21)=="MODERATE"

def test_score_boundary_high():
    assert risk_level(41)=="HIGH"

def test_score_boundary_critical():
    assert risk_level(71)=="CRITICAL"

def test_score_is_bounded():
    r=calculate_privacy_risk(public_answers())
    assert 0 <= r["overall_score"] <= 100

def test_assessment_contains_findings_and_recommendations():
    r=assess(public_answers())
    assert "findings" in r and "recommendations" in r
    assert len(r["findings"])>0

def test_recommendation_priority():
    r=assess(public_answers())
    assert all(x["priority"] in {"IMMEDIATE","IMPORTANT","GOOD PRACTICE"} for x in r["recommendations"])
