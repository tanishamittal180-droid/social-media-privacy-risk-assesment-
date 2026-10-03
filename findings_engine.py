
def generate_privacy_findings(a):
    findings = []
    def add(category, severity, item, fix):
        findings.append({"category": category, "severity": severity, "finding_type": item,
                         "description": item, "fix": fix})

    yes = lambda k: str(a.get(k,"NO")).upper() == "YES"

    if a.get("profile_visibility") == "PUBLIC":
        add("Profile Exposure","HIGH","Profile is publicly visible",
            "Use a more restricted audience where appropriate and review discoverability controls.")
    if yes("phone_public"):
        add("Personal Information","HIGH","Phone number is reported as publicly visible",
            "Hide unnecessary phone visibility and use platform contact controls.")
    if yes("email_public"):
        add("Personal Information","MODERATE","Personal email is reported as publicly visible",
            "Remove unnecessary public email exposure or use a dedicated contact address.")
    if yes("birthday_public"):
        add("Personal Information","MODERATE","Full birthday is reported as publicly visible",
            "Limit birthday visibility to the smallest audience needed.")
    if yes("home_info_public"):
        add("Personal Information","HIGH","Detailed home-related information is publicly visible",
            "Remove precise residential details from public profile content.")
    if yes("location_public"):
        add("Location Privacy","HIGH","Current/general location is publicly shared",
            "Limit location sharing and avoid unnecessary precise location details.")
    if yes("realtime_location"):
        add("Location Privacy","CRITICAL","Real-time location/check-ins are enabled",
            "Avoid broadcasting real-time location unless intentionally required.")
    if yes("travel_posts"):
        add("Location Privacy","HIGH","Travel plans are posted before or during trips",
            "Consider posting trip content after leaving the location.")
    if yes("routine_patterns"):
        add("Location Privacy","HIGH","Repeated time/place routines are disclosed",
            "Avoid publishing predictable routines or schedules.")
    if yes("geotagging"):
        add("Location Privacy","MODERATE","Geotagging is enabled",
            "Disable unnecessary geotags and review location information before posting.")
    if yes("posts_public"):
        add("Content Exposure","HIGH","Many posts are publicly visible",
            "Review audience settings and reduce public visibility for unnecessary content.")
    if yes("old_public_posts"):
        add("Digital Footprint","HIGH","Old public posts have not been reviewed",
            "Review historical posts and restrict or remove unnecessary public content.")
    if yes("documents_visible"):
        add("Content Exposure","CRITICAL","Documents, badges, IDs, tickets, or screens may be public",
            "Remove or crop sensitive documents and screen content before publishing.")
    if yes("child_photos_public"):
        add("Content Exposure","HIGH","Children may appear in public photos",
            "Consider a restricted audience and avoid unnecessary identifying context.")
    if a.get("unknown_connections") == "OFTEN":
        add("Connections","HIGH","Unknown connection requests are often accepted",
            "Verify unfamiliar profiles before accepting requests.")
    if yes("tag_review"):
        add("Tagging","HIGH","Tag review is disabled",
            "Enable tag review so tagged content can be checked before appearing.")
    if yes("unknown_mentions"):
        add("Tagging","MODERATE","Unknown users can mention/tag the account",
            "Restrict mention/tag permissions where the platform allows.")
    if yes("mfa_enabled") is False:
        add("Account Security","CRITICAL","MFA is not enabled",
            "Enable multi-factor authentication using a strong supported method.")
    if yes("unique_password") is False:
        add("Account Security","HIGH","A unique password is not confirmed",
            "Use a unique strong password and avoid password reuse.")
    if yes("login_alerts") is False:
        add("Account Security","MODERATE","Login/security alerts are not enabled",
            "Enable login alerts where supported.")
    if yes("sessions_reviewed") is False:
        add("Account Security","MODERATE","Active sessions/devices are not regularly reviewed",
            "Review active sessions and remove unfamiliar devices.")
    if yes("third_party_reviewed") is False:
        add("Third-Party Apps","HIGH","Connected applications are not regularly reviewed",
            "Review integrations and revoke unnecessary access.")
    if yes("unused_apps"):
        add("Third-Party Apps","HIGH","Unused integrations may remain connected",
            "Remove applications that no longer have a legitimate purpose.")
    if yes("broad_app_permissions"):
        add("Third-Party Apps","MODERATE","Third-party permissions may be broader than necessary",
            "Apply least privilege and reduce unnecessary permissions.")
    if yes("unknown_links"):
        add("Social Engineering","HIGH","Unexpected links may be opened",
            "Pause and verify unexpected links independently before opening them.")
    if yes("verification_codes"):
        add("Social Engineering","CRITICAL","Verification codes may be shared with impersonators",
            "Never share authentication or verification codes with another person.")
    if yes("unknown_dms"):
        add("Social Engineering","MODERATE","Unexpected messages from unfamiliar accounts may receive responses",
            "Verify identity independently before continuing a sensitive conversation.")
    if yes("impersonation_awareness"):
        add("Social Engineering","MODERATE","Account-identity verification practices are uncertain",
            "Use official channels and independent verification for suspicious requests.")
    if yes("privacy_reviewed") is False:
        add("Digital Footprint","HIGH","Privacy settings have not been reviewed recently",
            "Schedule periodic privacy-setting reviews.")
    if yes("old_accounts") is False:
        add("Digital Footprint","MODERATE","Old account status is not confirmed/reviewed",
            "Review old accounts and close or secure unused accounts.")
    if yes("old_comments") is False:
        add("Digital Footprint","MODERATE","Old public comments have not been reviewed",
            "Review historical public comments and remove unnecessary exposure.")
    if yes("photo_metadata"):
        add("Digital Footprint","MODERATE","Photo metadata awareness is uncertain",
            "Review metadata handling and remove unnecessary metadata from copies before sharing.")

    severity_order = {"CRITICAL":0,"HIGH":1,"MODERATE":2,"LOW":3}
    findings.sort(key=lambda x: severity_order.get(x["severity"], 9))
    return findings
