from pydantic import BaseModel, Field
from typing import List, Optional


class WorkerRiskInput(BaseModel):
    city: str
    zone: str
    rainfall_risk: float = Field(..., ge=0, le=100)
    flood_risk: float = Field(..., ge=0, le=100)
    aqi_risk: float = Field(..., ge=0, le=100)
    heatwave_risk: float = Field(..., ge=0, le=100)
    road_closure_risk: float = Field(..., ge=0, le=100)
    outage_risk: float = Field(..., ge=0, le=100)
    shift_exposure_risk: float = Field(..., ge=0, le=100)
    income_dependency_risk: float = Field(..., ge=0, le=100)


class RiskOutput(BaseModel):
    risk_score: float
    risk_level: str
    top_reasons: List[str]

class PremiumInput(BaseModel):
    risk_score: float = Field(..., ge=0, le=100)
    avg_weekly_income: float = Field(..., gt=0)
    plan_type: str  # Basic, Smart, Plus


class PremiumOutput(BaseModel):
    weekly_premium: float
    plan_type: str
    premium_breakdown: dict

class FraudInput(BaseModel):
    duplicate_claim: bool
    zone_mismatch: bool
    outside_working_hours: bool
    unrealistic_income: bool
    suspicious_claim_frequency: int = Field(..., ge=0)
    gps_spoof_suspected: bool = False


class FraudOutput(BaseModel):
    fraud_score: int
    fraud_level: str
    reasons: List[str]
    action: str

class TriggerEventInput(BaseModel):
    event_type: str  # rain, aqi, road_closure, flood, outage
    event_zone: str
    event_severity: float = Field(..., ge=0, le=100)
    worker_zone: str
    policy_active: bool
    covered_triggers: List[str]
    shift_start_hour: int = Field(..., ge=0, le=23)
    shift_end_hour: int = Field(..., ge=0, le=23)
    event_hour: int = Field(..., ge=0, le=23)


class TriggerOutput(BaseModel):
    trigger_matched: bool
    claim_should_be_created: bool
    reason: str

class PayoutInput(BaseModel):
    avg_weekly_income: float = Field(..., gt=0)
    weekly_hours: float = Field(..., gt=0)
    disrupted_hours: float = Field(..., gt=0)
    coverage_percentage: float = Field(..., gt=0, le=1)
    max_payout_cap: float = Field(..., gt=0)


class PayoutOutput(BaseModel):
    hourly_income: float
    gross_loss: float
    payout_amount: float
    payout_status: str
    payout_reference_id: str