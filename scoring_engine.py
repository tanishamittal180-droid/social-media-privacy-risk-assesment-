
CATEGORY_WEIGHTS = {
    "Profile Exposure": 10,
    "Personal Information": 15,
    "Location Privacy": 15,
    "Content Exposure": 10,
    "Connections": 10,
    "Tagging": 5,
    "Account Security": 15,
    "Third-Party Apps": 5,
    "Social Engineering": 10,
    "Digital Footprint": 5,
}

def clamp(value):
    return max(0, min(100, round(float(value))))

def risk_level(score):
    score = clamp(score)
    if score <= 20:
        return "LOW"
    if score <= 40:
        return "MODERATE"
    if score <= 70:
        return "HIGH"
    return "CRITICAL"

def _yes(a, key):
    return str(a.get(key, "NO")).upper() == "YES"

def _cat_scores(a):
    s = {k: 0 for k in CATEGORY_WEIGHTS}

    vis = str(a.get("profile_visibility", "PRIVATE")).upper()
    s["Profile Exposure"] += {"PUBLIC": 70, "FRIENDS": 35, "PRIVATE": 5}.get(vis, 50)
    for k in ["search_visibility","follower_visibility","friends_list_public"]:
        if _yes(a,k): s["Profile Exposure"] += 10

    for k in ["phone_public","email_public","birthday_public","home_info_public",
              "workplace_public","education_public","relationship_public"]:
        if _yes(a,k): s["Personal Information"] += 14
    s["Personal Information"] = clamp(s["Personal Information"])

    for k in ["location_public","realtime_location","geotagging","travel_posts","routine_patterns"]:
        if _yes(a,k): s["Location Privacy"] += 20 if k in ["realtime_location","routine_patterns"] else 16

    for k in ["posts_public","old_public_posts","documents_visible","family_content_public","child_photos_public"]:
        if _yes(a,k): s["Content Exposure"] += 20

    u = str(a.get("unknown_connections","RARELY")).upper()
    s["Connections"] += {"OFTEN": 75, "SOMETIMES": 40, "RARELY": 10}.get(u, 40)
    if _yes(a,"follower_review"): s["Connections"] -= 15
    s["Connections"] = max(0, s["Connections"])

    for k in ["tag_review","unknown_mentions","auto_tag_posts"]:
        if _yes(a,k): s["Tagging"] += 34

    for k in ["mfa_enabled","unique_password","password_manager","login_alerts","sessions_reviewed","recovery_reviewed"]:
        if not _yes(a,k): s["Account Security"] += 17

    if not _yes(a,"third_party_reviewed"): s["Third-Party Apps"] += 45
    if _yes(a,"unused_apps"): s["Third-Party Apps"] += 30
    if _yes(a,"broad_app_permissions"): s["Third-Party Apps"] += 25

    for k in ["unknown_links","verification_codes","unknown_dms","impersonation_awareness","giveaway_awareness"]:
        if _yes(a,k): s["Social Engineering"] += 20

    for k in ["privacy_reviewed","old_accounts","old_comments","photo_metadata"]:
        if not _yes(a,k): s["Digital Footprint"] += 25

    return {k: clamp(v) for k,v in s.items()}

def calculate_privacy_risk(answers):
    categories = _cat_scores(answers)
    overall = sum(categories[k] * CATEGORY_WEIGHTS[k] / 100 for k in categories)
    return {"overall_score": clamp(overall), "risk_level": risk_level(overall), "category_scores": categories}
