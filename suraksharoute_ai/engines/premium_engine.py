from schemas import PremiumInput


PLAN_COMPONENTS = {
    "Basic": 0,
    "Smart": 15,
    "Plus": 30,
}


def calculate_weekly_premium(data: PremiumInput) -> dict:
    if data.plan_type not in PLAN_COMPONENTS:
        raise ValueError("Invalid plan type. Use Basic, Smart, or Plus.")

    base_premium = 25
    risk_component = data.risk_score * 0.4
    income_component = data.avg_weekly_income * 0.002
    plan_component = PLAN_COMPONENTS[data.plan_type]

    premium = round(base_premium + risk_component + income_component + plan_component, 2)

    return {
        "weekly_premium": premium,
        "plan_type": data.plan_type,
        "premium_breakdown": {
            "base_premium": base_premium,
            "risk_component": round(risk_component, 2),
            "income_component": round(income_component, 2),
            "plan_component": plan_component,
        },
    }