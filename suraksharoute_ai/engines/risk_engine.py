from typing import List, Tuple
from config import RISK_WEIGHTS, RISK_THRESHOLDS
from schemas import WorkerRiskInput


def _risk_level(score: float) -> str:
    if score <= RISK_THRESHOLDS["low_max"]:
        return "Low"
    if score <= RISK_THRESHOLDS["medium_max"]:
        return "Medium"
    return "High"


def _top_reasons(worker: WorkerRiskInput) -> List[str]:
    feature_map = {
        "rainfall_risk": "High rainfall exposure",
        "flood_risk": "Flood-prone zone",
        "aqi_risk": "Severe pollution exposure",
        "heatwave_risk": "Heatwave exposure",
        "road_closure_risk": "Frequent road closure risk",
        "outage_risk": "Platform outage tendency",
        "shift_exposure_risk": "Risky shift timing overlap",
        "income_dependency_risk": "High dependence on weekly income",
    }

    scored_features: List[Tuple[str, float]] = [
        ("rainfall_risk", worker.rainfall_risk),
        ("flood_risk", worker.flood_risk),
        ("aqi_risk", worker.aqi_risk),
        ("heatwave_risk", worker.heatwave_risk),
        ("road_closure_risk", worker.road_closure_risk),
        ("outage_risk", worker.outage_risk),
        ("shift_exposure_risk", worker.shift_exposure_risk),
        ("income_dependency_risk", worker.income_dependency_risk),
    ]

    scored_features.sort(key=lambda x: x[1], reverse=True)
    return [feature_map[name] for name, _ in scored_features[:3]]


def calculate_risk_score(worker: WorkerRiskInput) -> dict:
    score = (
        worker.rainfall_risk * RISK_WEIGHTS["rainfall_risk"] +
        worker.flood_risk * RISK_WEIGHTS["flood_risk"] +
        worker.aqi_risk * RISK_WEIGHTS["aqi_risk"] +
        worker.heatwave_risk * RISK_WEIGHTS["heatwave_risk"] +
        worker.road_closure_risk * RISK_WEIGHTS["road_closure_risk"] +
        worker.outage_risk * RISK_WEIGHTS["outage_risk"] +
        worker.shift_exposure_risk * RISK_WEIGHTS["shift_exposure_risk"] +
        worker.income_dependency_risk * RISK_WEIGHTS["income_dependency_risk"]
    )

    score = round(score, 2)
    return {
        "risk_score": score,
        "risk_level": _risk_level(score),
        "top_reasons": _top_reasons(worker),
    }