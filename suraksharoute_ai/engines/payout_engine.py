from schemas import PayoutInput
from utils import generate_reference


def estimate_payout(data: PayoutInput) -> dict:
    hourly_income = data.avg_weekly_income / data.weekly_hours
    gross_loss = hourly_income * data.disrupted_hours
    payout_amount = min(gross_loss * data.coverage_percentage, data.max_payout_cap)

    return {
        "hourly_income": round(hourly_income, 2),
        "gross_loss": round(gross_loss, 2),
        "payout_amount": round(payout_amount, 2),
        "payout_status": "Success",
        "payout_reference_id": generate_reference("PAY"),
    }