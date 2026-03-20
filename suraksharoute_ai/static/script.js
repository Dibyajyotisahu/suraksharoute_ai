async function postData(url = "", data = {}) {
    const response = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });
    return response.json();
}

function setSummary(id, value) {
    document.getElementById(id).textContent = value;
}

function statusClass(value) {
    const v = String(value).toLowerCase();
    if (v.includes("low")) return "status-low";
    if (v.includes("medium")) return "status-medium";
    if (v.includes("high")) return "status-high";
    if (v.includes("success")) return "status-success";
    if (v.includes("approve")) return "status-success";
    if (v.includes("hold")) return "status-warning";
    if (v.includes("review")) return "status-high";
    if (v.includes("true")) return "status-success";
    if (v.includes("false")) return "status-warning";
    return "status-info";
}

function renderRiskResult(result) {
    return `
    <div class="result-grid">
      <div class="metric-card">
        <span class="metric-label">Risk Score</span>
        <div class="metric-value">${result.risk_score ?? "-"}</div>
      </div>
      <div class="metric-card">
        <span class="metric-label">Risk Level</span>
        <span class="status-badge ${statusClass(result.risk_level)}">${result.risk_level ?? "-"}</span>
      </div>
    </div>

    <div class="result-section">
      <h4>Top Risk Drivers</h4>
      <div class="reason-list">
        ${(result.top_reasons || []).map(r => `<span class="reason-pill">${r}</span>`).join("")}
      </div>
    </div>
  `;
}

function renderPremiumResult(result) {
  const breakdown = result.premium_breakdown || {};
  return `
    <div class="result-grid">
      <div class="metric-card">
        <span class="metric-label">Weekly Premium</span>
        <div class="metric-value">₹${result.weekly_premium ?? "-"}</div>
      </div>
      <div class="metric-card">
        <span class="metric-label">Selected Plan</span>
        <span class="status-badge status-info">${result.plan_type ?? "-"}</span>
      </div>
    </div>

    <div class="result-section">
      <h4>Premium Breakdown</h4>
      <div class="keyvalue-list">
        <div class="keyvalue-card"><span class="k">Base Premium</span><span class="v">₹${breakdown.base_premium ?? "-"}</span></div>
        <div class="keyvalue-card"><span class="k">Risk Component</span><span class="v">₹${breakdown.risk_component ?? "-"}</span></div>
        <div class="keyvalue-card"><span class="k">Income Component</span><span class="v">₹${breakdown.income_component ?? "-"}</span></div>
        <div class="keyvalue-card"><span class="k">Plan Component</span><span class="v">₹${breakdown.plan_component ?? "-"}</span></div>
      </div>
    </div>
  `;
}

function renderFraudResult(result) {
  return `
    <div class="result-grid">
      <div class="metric-card">
        <span class="metric-label">Fraud Score</span>
        <div class="metric-value">${result.fraud_score ?? "-"}</div>
      </div>
      <div class="metric-card">
        <span class="metric-label">Fraud Level</span>
        <span class="status-badge ${statusClass(result.fraud_level)}">${result.fraud_level ?? "-"}</span>
      </div>
    </div>

    <div class="decision-box">
      <strong>Recommended Action</strong>
      <span class="status-badge ${statusClass(result.action)}">${result.action ?? "-"}</span>
    </div>

    <div class="result-divider"></div>

    <div class="result-section">
      <h4>Fraud Signals</h4>
      <div class="reason-list">
        ${(result.reasons || []).map(r => `<span class="reason-pill">${r}</span>`).join("")}
      </div>
    </div>
  `;
}

function renderTriggerResult(result) {
  return `
    <div class="result-grid">
      <div class="metric-card">
        <span class="metric-label">Trigger Matched</span>
        <span class="status-badge ${statusClass(result.trigger_matched)}">${String(result.trigger_matched)}</span>
      </div>
      <div class="metric-card">
        <span class="metric-label">Create Claim</span>
        <span class="status-badge ${statusClass(result.claim_should_be_created)}">${String(result.claim_should_be_created)}</span>
      </div>
    </div>

    <div class="decision-box">
      <strong>Decision Reason</strong>
      <span>${result.reason ?? "-"}</span>
    </div>
  `;
}

function renderPayoutResult(result) {
  return `
    <div class="result-grid">
      <div class="metric-card">
        <span class="metric-label">Payout Amount</span>
        <div class="metric-value">₹${result.payout_amount ?? "-"}</div>
      </div>
      <div class="metric-card">
        <span class="metric-label">Payout Status</span>
        <span class="status-badge ${statusClass(result.payout_status)}">${result.payout_status ?? "-"}</span>
      </div>
    </div>

    <div class="result-section">
      <h4>Payout Details</h4>
      <div class="keyvalue-list">
        <div class="keyvalue-card"><span class="k">Hourly Income</span><span class="v">₹${result.hourly_income ?? "-"}</span></div>
        <div class="keyvalue-card"><span class="k">Gross Loss</span><span class="v">₹${result.gross_loss ?? "-"}</span></div>
        <div class="keyvalue-card"><span class="k">Reference ID</span><span class="v">${result.payout_reference_id ?? "-"}</span></div>
      </div>
    </div>
  `;
}

async function runRiskScore() {
  const data = {
    city: document.getElementById("risk_city").value,
    zone: document.getElementById("risk_zone").value,
    rainfall_risk: Number(document.getElementById("rainfall_risk").value),
    flood_risk: Number(document.getElementById("flood_risk").value),
    aqi_risk: Number(document.getElementById("aqi_risk").value),
    heatwave_risk: Number(document.getElementById("heatwave_risk").value),
    road_closure_risk: Number(document.getElementById("road_closure_risk").value),
    outage_risk: Number(document.getElementById("outage_risk").value),
    shift_exposure_risk: Number(document.getElementById("shift_exposure_risk").value),
    income_dependency_risk: Number(document.getElementById("income_dependency_risk").value)
  };

  const result = await postData("/risk-score", data);
  document.getElementById("risk_output").innerHTML = renderRiskResult(result);

  if (result.risk_score !== undefined) {
    document.getElementById("premium_risk_score").value = result.risk_score;
    setSummary("summaryRisk", `${result.risk_level} (${result.risk_score})`);
  }
}

async function runPremium() {
  const data = {
    risk_score: Number(document.getElementById("premium_risk_score").value),
    avg_weekly_income: Number(document.getElementById("avg_weekly_income").value),
    plan_type: document.getElementById("plan_type").value
  };

  const result = await postData("/weekly-premium", data);
  document.getElementById("premium_output").innerHTML = renderPremiumResult(result);

  if (result.weekly_premium !== undefined) {
    setSummary("summaryPremium", `₹${result.weekly_premium} / week`);
  }
}

async function runFraud() {
  const data = {
    duplicate_claim: document.getElementById("duplicate_claim").checked,
    zone_mismatch: document.getElementById("zone_mismatch").checked,
    outside_working_hours: document.getElementById("outside_working_hours").checked,
    unrealistic_income: document.getElementById("unrealistic_income").checked,
    suspicious_claim_frequency: Number(document.getElementById("suspicious_claim_frequency").value),
    gps_spoof_suspected: document.getElementById("gps_spoof_suspected").checked
  };

  const result = await postData("/fraud-check", data);
  document.getElementById("fraud_output").innerHTML = renderFraudResult(result);

  if (result.action) {
    setSummary("summaryFraud", result.action);
  }
}

async function runTrigger() {
  const data = {
    event_type: document.getElementById("event_type").value,
    event_zone: document.getElementById("event_zone").value,
    event_severity: Number(document.getElementById("event_severity").value),
    worker_zone: document.getElementById("worker_zone").value,
    policy_active: document.getElementById("policy_active").value === "true",
    covered_triggers: document.getElementById("covered_triggers").value.split(",").map(x => x.trim()),
    shift_start_hour: Number(document.getElementById("shift_start_hour").value),
    shift_end_hour: Number(document.getElementById("shift_end_hour").value),
    event_hour: Number(document.getElementById("event_hour").value)
  };

  const result = await postData("/trigger-check", data);
  document.getElementById("trigger_output").innerHTML = renderTriggerResult(result);
}

async function runPayout() {
  const data = {
    avg_weekly_income: Number(document.getElementById("payout_avg_weekly_income").value),
    weekly_hours: Number(document.getElementById("weekly_hours").value),
    disrupted_hours: Number(document.getElementById("disrupted_hours").value),
    coverage_percentage: Number(document.getElementById("coverage_percentage").value),
    max_payout_cap: Number(document.getElementById("max_payout_cap").value)
  };

  const result = await postData("/estimate-payout", data);
  document.getElementById("payout_output").innerHTML = renderPayoutResult(result);

  if (result.payout_amount !== undefined) {
    setSummary("summaryPayout", `₹${result.payout_amount}`);
  }
}

async function runQuickDemo() {
  await runRiskScore();
  await runPremium();
  await runFraud();
  await runTrigger();
  await runPayout();
}