from schemas import TriggerEventInput


TRIGGER_THRESHOLDS = {
    "rain": 60,
    "aqi": 70,
    "road_closure": 50,
    "flood": 50,
    "outage": 40,
}


def _is_within_shift(start_hour: int, end_hour: int, event_hour: int) -> bool:
    if start_hour <= end_hour:
        return start_hour <= event_hour <= end_hour
    return event_hour >= start_hour or event_hour <= end_hour


def check_trigger(data: TriggerEventInput) -> dict:
    if not data.policy_active:
        return {
            "trigger_matched": False,
            "claim_should_be_created": False,
            "reason": "No active policy",
        }

    if data.event_type not in data.covered_triggers:
        return {
            "trigger_matched": False,
            "claim_should_be_created": False,
            "reason": "Trigger type not covered by plan",
        }

    if data.worker_zone != data.event_zone:
        return {
            "trigger_matched": False,
            "claim_should_be_created": False,
            "reason": "Worker zone not affected",
        }

    if not _is_within_shift(data.shift_start_hour, data.shift_end_hour, data.event_hour):
        return {
            "trigger_matched": False,
            "claim_should_be_created": False,
            "reason": "Event outside worker shift time",
        }

    threshold = TRIGGER_THRESHOLDS.get(data.event_type, 999)
    if data.event_severity < threshold:
        return {
            "trigger_matched": False,
            "claim_should_be_created": False,
            "reason": "Event severity below threshold",
        }

    return {
        "trigger_matched": True,
        "claim_should_be_created": True,
        "reason": "Covered event matched active policy and shift window",
    }