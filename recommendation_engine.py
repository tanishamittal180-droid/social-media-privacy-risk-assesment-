
PRIORITY = {"CRITICAL":"IMMEDIATE", "HIGH":"IMMEDIATE", "MODERATE":"IMPORTANT", "LOW":"GOOD PRACTICE"}

def generate_recommendations(findings):
    out = []
    seen = set()
    for f in findings:
        key = f["fix"]
        if key in seen: continue
        seen.add(key)
        out.append({"priority": PRIORITY.get(f["severity"],"GOOD PRACTICE"),
                    "category": f["category"], "recommendation": f["fix"]})
    return out
