from schemas import FraudInput


def evaluate_fraud(data: FraudInput) -> dict:
    score = 0
    reasons = []

    if data.duplicate_claim:
        score += 40
        reasons.append("Duplicate claim detected")

    if data.zone_mismatch:
        score += 30
        reasons.append("Worker zone does not match trigger zone")

    if data.outside_working_hours:
        score += 20
        reasons.append("Claim outside declared working hours")

    if data.unrealistic_income:
        score += 10
        reasons.append("Unrealistic weekly income reported")

    if data.suspicious_claim_frequency >= 3:
        score += 20
        reasons.append("Too many suspicious claims recently")

    if data.gps_spoof_suspected:
        score += 35
        reasons.append("Possible GPS spoofing detected")

    if score <= 29:
        level = "Low"
        action = "Auto-Approve"
    elif score <= 59:
        level = "Medium"
        action = "Soft Hold / Extra Verification"
    else:
        level = "High"
        action = "Manual Review"

    return {
        "fraud_score": score,
        "fraud_level": level,
        "reasons": reasons if reasons else ["No major fraud signals"],
        "action": action,
    }