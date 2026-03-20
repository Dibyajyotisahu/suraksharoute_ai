from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from schemas import (
    WorkerRiskInput,
    PremiumInput,
    FraudInput,
    TriggerEventInput,
    PayoutInput,
)
from engines.risk_engine import calculate_risk_score
from engines.premium_engine import calculate_weekly_premium
from engines.fraud_engine import evaluate_fraud
from engines.trigger_engine import check_trigger
from engines.payout_engine import estimate_payout

app = FastAPI(title="SurakshaRoute AI/ML Engine")

# Static + templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/risk-score")
def risk_score_api(data: WorkerRiskInput):
    return calculate_risk_score(data)


@app.post("/weekly-premium")
def weekly_premium_api(data: PremiumInput):
    try:
        return calculate_weekly_premium(data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/fraud-check")
def fraud_check_api(data: FraudInput):
    return evaluate_fraud(data)


@app.post("/trigger-check")
def trigger_check_api(data: TriggerEventInput):
    return check_trigger(data)


@app.post("/estimate-payout")
def estimate_payout_api(data: PayoutInput):
    return estimate_payout(data)