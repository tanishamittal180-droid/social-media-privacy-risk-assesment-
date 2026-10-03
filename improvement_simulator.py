
from copy import deepcopy
from backend.services.assessment_engine import assess

def simulate(answers, changes):
    original = assess(answers)
    improved_answers = deepcopy(answers)
    for key, value in changes.items():
        improved_answers[key] = value
    simulated = assess(improved_answers)
    return {
        "original": original,
        "simulated": simulated,
        "risk_reduction": max(0, original["overall_score"] - simulated["overall_score"]),
        "changed_fields": changes
    }
