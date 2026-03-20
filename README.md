# SurakshaRoute  
### AI-Powered Parametric Income Protection for Food Delivery Workers

> **Guidewire DEVTrails 2026 — Phase 1 Submission**  
> A smart weekly income-protection platform for food delivery workers in India, built to respond to external disruptions through AI-driven risk scoring, parametric triggers, fraud defense, and fast payout logic.

---

## Problem Statement

Food delivery workers in India depend heavily on daily and weekly earnings. However, their ability to work is frequently disrupted by external factors such as:

- heavy rain
- floods
- severe air pollution
- heatwaves
- curfews
- road closures
- platform or app outages

For gig workers, **no work often means no income**. Traditional insurance products are not designed for this kind of short-term, event-driven income disruption. They are slow, paperwork-heavy, and focused on damage, health, or accident claims rather than **real-time loss of earnings**.

The Guidewire DEVTrails 2026 challenge asks us to design a solution that protects **income loss only**, uses a **weekly pricing model**, and serves a specific delivery-worker persona. Our chosen persona is:

## Chosen Persona

**Food Delivery Workers**  
Examples: riders working on food delivery platforms in urban and semi-urban India.

We selected this persona because food delivery workers:
- are highly exposed to outdoor environmental disruption
- depend on fast-moving daily earnings
- face repeated location-based risk
- need immediate and lightweight protection, not delayed insurance claim processing

---

## Our Solution

## What is SurakshaRoute?

**SurakshaRoute** is an **AI-powered parametric insurance platform** designed specifically for **food delivery workers**.

It provides **weekly income protection** by:
1. analyzing the worker’s zone and work profile
2. estimating disruption risk
3. generating a fair weekly premium
4. monitoring external disruption triggers
5. automatically checking claim eligibility
6. detecting fraud or spoofing behavior
7. estimating payout for lost income

Unlike traditional insurance, SurakshaRoute uses **parametric logic**.  
That means a payout is not dependent on manual claim investigation alone. Instead, it is triggered when a measurable external event crosses defined thresholds and affects the worker during covered working hours.

---

## Why Parametric Insurance?

Parametric insurance is ideal for this problem because it is:

- **fast** — event-based logic allows quicker claims
- **scalable** — suitable for large gig-worker populations
- **transparent** — based on predefined trigger conditions
- **automation-friendly** — supports low-touch claims workflows
- **worker-centric** — useful for small but immediate financial disruption

### Traditional Insurance vs SurakshaRoute

| Traditional Insurance | SurakshaRoute |
|---|---|
| Manual claims process | Automated trigger-based flow |
| Slow settlement | Fast decision support |
| Designed for damage/accident | Designed for income disruption |
| Often monthly/complex | Weekly, worker-aligned pricing |
| Limited real-time relevance | Event-driven and location-aware |

---

## What Phase 1 Covers

Phase 1 focuses on:
- understanding the delivery-worker problem deeply
- choosing a precise persona
- defining the weekly premium model
- designing parametric trigger logic
- planning AI/ML integration
- building the complete system architecture
- defining the anti-spoofing and fraud-defense strategy
- preparing a clear product workflow and implementation roadmap

This phase is about **foundation, clarity, and architecture**, not just UI.

---

## Core Objectives

Our Phase 1 objectives were:

- build a clear problem-to-solution mapping
- keep the solution strictly aligned with the official use case
- focus only on **income protection**
- build around a **weekly pricing model**
- define AI/ML modules with explainable roles
- design a secure and scalable architecture
- address the newly introduced **GPS spoofing fraud challenge**
- create a strong base for Phase 2 implementation

---

## Key Features Planned

SurakshaRoute is designed with the following core features:

### 1. Worker Onboarding
A worker can enter:
- city
- delivery zone
- shift timing
- average weekly income
- average work hours
- platform/work profile

### 2. AI-Based Risk Scoring
The platform estimates disruption risk using:
- rainfall exposure
- flood-prone area score
- AQI history
- heatwave frequency
- road closure tendency
- outage tendency
- shift timing risk
- income dependency

### 3. Dynamic Weekly Premium
Using risk and earnings profile, the system calculates a **weekly premium** for coverage.

### 4. Parametric Trigger Monitoring
The system monitors disruption events such as:
- heavy rain
- flood alerts
- severe AQI spike
- heatwave threshold
- road closure
- platform outage
- curfew/closure event

### 5. Automatic Claim Eligibility Logic
When a disruption overlaps with:
- worker zone
- active policy
- shift timing
- covered trigger type

the system decides whether a claim should be initiated.

### 6. Fraud Detection & Anti-Spoofing
The platform detects suspicious claim patterns such as:
- GPS spoofing
- duplicate claims
- zone mismatch
- outside-shift claims
- unrealistic income profile
- suspicious repeated claims

### 7. Payout Estimation
The system estimates lost income using:
- weekly earnings
- weekly work hours
- disrupted hours
- coverage percentage
- payout cap

---

## Product Workflow

Below is the planned end-to-end flow of SurakshaRoute:

```text
Worker Signup / Onboarding
        ↓
AI Risk Scoring
        ↓
Dynamic Weekly Premium Generation
        ↓
Policy Activation
        ↓
Real-Time Trigger Monitoring
        ↓
Trigger Match Check
        ↓
Automatic Claim Eligibility
        ↓
Fraud / Anti-Spoofing Verification
        ↓
Payout Estimation
        ↓
Worker & Admin Dashboard Update

# SurakshaRoute  
### AI-Powered Parametric Income Protection for Food Delivery Workers

> **Guidewire DEVTrails 2026 — Phase 1 Submission**  
> A smart weekly income-protection platform for food delivery workers in India, built to respond to external disruptions through AI-driven risk scoring, parametric triggers, fraud defense, and fast payout logic.

---

## Problem Statement

Food delivery workers in India depend heavily on daily and weekly earnings. However, their ability to work is frequently disrupted by external factors such as:

- heavy rain
- floods
- severe air pollution
- heatwaves
- curfews
- road closures
- platform or app outages

For gig workers, **no work often means no income**. Traditional insurance products are not designed for this kind of short-term, event-driven income disruption. They are slow, paperwork-heavy, and focused on damage, health, or accident claims rather than **real-time loss of earnings**.

The Guidewire DEVTrails 2026 challenge asks us to design a solution that protects **income loss only**, uses a **weekly pricing model**, and serves a specific delivery-worker persona. Our chosen persona is:

## Chosen Persona

**Food Delivery Workers**  
Examples: riders working on food delivery platforms in urban and semi-urban India.

We selected this persona because food delivery workers:
- are highly exposed to outdoor environmental disruption
- depend on fast-moving daily earnings
- face repeated location-based risk
- need immediate and lightweight protection, not delayed insurance claim processing

---

## Our Solution

## What is SurakshaRoute?

**SurakshaRoute** is an **AI-powered parametric insurance platform** designed specifically for **food delivery workers**.

It provides **weekly income protection** by:
1. analyzing the worker’s zone and work profile
2. estimating disruption risk
3. generating a fair weekly premium
4. monitoring external disruption triggers
5. automatically checking claim eligibility
6. detecting fraud or spoofing behavior
7. estimating payout for lost income

Unlike traditional insurance, SurakshaRoute uses **parametric logic**.  
That means a payout is not dependent on manual claim investigation alone. Instead, it is triggered when a measurable external event crosses defined thresholds and affects the worker during covered working hours.

---

## Why Parametric Insurance?

Parametric insurance is ideal for this problem because it is:

- **fast** — event-based logic allows quicker claims
- **scalable** — suitable for large gig-worker populations
- **transparent** — based on predefined trigger conditions
- **automation-friendly** — supports low-touch claims workflows
- **worker-centric** — useful for small but immediate financial disruption

### Traditional Insurance vs SurakshaRoute

| Traditional Insurance | SurakshaRoute |
|---|---|
| Manual claims process | Automated trigger-based flow |
| Slow settlement | Fast decision support |
| Designed for damage/accident | Designed for income disruption |
| Often monthly/complex | Weekly, worker-aligned pricing |
| Limited real-time relevance | Event-driven and location-aware |

---

## What Phase 1 Covers

Phase 1 focuses on:
- understanding the delivery-worker problem deeply
- choosing a precise persona
- defining the weekly premium model
- designing parametric trigger logic
- planning AI/ML integration
- building the complete system architecture
- defining the anti-spoofing and fraud-defense strategy
- preparing a clear product workflow and implementation roadmap

This phase is about **foundation, clarity, and architecture**, not just UI.

---

## Core Objectives

Our Phase 1 objectives were:

- build a clear problem-to-solution mapping
- keep the solution strictly aligned with the official use case
- focus only on **income protection**
- build around a **weekly pricing model**
- define AI/ML modules with explainable roles
- design a secure and scalable architecture
- address the newly introduced **GPS spoofing fraud challenge**
- create a strong base for Phase 2 implementation

---

## Key Features Planned

SurakshaRoute is designed with the following core features:

### 1. Worker Onboarding
A worker can enter:
- city
- delivery zone
- shift timing
- average weekly income
- average work hours
- platform/work profile

### 2. AI-Based Risk Scoring
The platform estimates disruption risk using:
- rainfall exposure
- flood-prone area score
- AQI history
- heatwave frequency
- road closure tendency
- outage tendency
- shift timing risk
- income dependency

### 3. Dynamic Weekly Premium
Using risk and earnings profile, the system calculates a **weekly premium** for coverage.

### 4. Parametric Trigger Monitoring
The system monitors disruption events such as:
- heavy rain
- flood alerts
- severe AQI spike
- heatwave threshold
- road closure
- platform outage
- curfew/closure event

### 5. Automatic Claim Eligibility Logic
When a disruption overlaps with:
- worker zone
- active policy
- shift timing
- covered trigger type

the system decides whether a claim should be initiated.

### 6. Fraud Detection & Anti-Spoofing
The platform detects suspicious claim patterns such as:
- GPS spoofing
- duplicate claims
- zone mismatch
- outside-shift claims
- unrealistic income profile
- suspicious repeated claims

### 7. Payout Estimation
The system estimates lost income using:
- weekly earnings
- weekly work hours
- disrupted hours
- coverage percentage
- payout cap

---

## Product Workflow

Below is the planned end-to-end flow of SurakshaRoute:

```text
Worker Signup / Onboarding
        ↓
AI Risk Scoring
        ↓
Dynamic Weekly Premium Generation
        ↓
Policy Activation
        ↓
Real-Time Trigger Monitoring
        ↓
Trigger Match Check
        ↓
Automatic Claim Eligibility
        ↓
Fraud / Anti-Spoofing Verification
        ↓
Payout Estimation
        ↓
Worker & Admin Dashboard Update

**System Architecture**

SurakshaRoute follows a modular architecture with separate layers for user interaction,
business logic, AI/ML decision engines, and event integration.

                    ┌──────────────────────────────┐
                    │         Public Website        │
                    │  About | How it works | Plans │
                    └──────────────┬───────────────┘
                                   │
                  ┌────────────────┴────────────────┐
                  │                                 │
      ┌───────────▼───────────┐         ┌──────────▼──────────┐
      │     Worker Portal      │         │   Admin Dashboard   │
      │  Onboarding            │         │  Claims Review      │
      │  Weekly Plans          │         │  Fraud Monitoring   │
      │  Policy Status         │         │  Trigger Monitor    │
      │  Alerts & Claims       │         │  Analytics          │
      └───────────┬───────────┘         └──────────┬──────────┘
                  │                                 │
                  └──────────────┬──────────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │     Backend API Layer    │
                    │ Auth | Worker | Claims   │
                    │ Policy | Triggers        │
                    │ Fraud | Premium | Payout │
                    └────────────┬────────────┘
                                 │
         ┌───────────────────────┼─────────────────────────┐
         │                       │                         │
 ┌───────▼────────┐     ┌────────▼────────┐      ┌────────▼────────┐
 │   Database      │     │   AI/ML Layer   │      │ External / Mock │
 │ Workers         │     │ Risk Scoring    │      │ Weather API     │
 │ Profiles        │     │ Premium Engine  │      │ AQI API         │
 │ Policies        │     │ Fraud Engine    │      │ Traffic Data    │
 │ Trigger Events  │     │ Trigger Logic   │      │ Outage Signals  │
 │ Claims          │     │ Payout Engine   │      │ Notification    │
 │ Payouts         │     └─────────────────┘      └─────────────────┘
 └─────────────────┘

## AI/ML Architecture

Phase 1 defines **five core AI/ML-driven modules** that together enable weekly income protection for food delivery workers.

---

### 1. Risk Scoring Model

#### Objective
Estimate how risky a worker’s delivery zone and work pattern are for **next-week income disruption**.

#### Inputs
- city  
- zone  
- rainfall risk  
- flood risk  
- AQI risk  
- heatwave risk  
- road closure risk  
- outage risk  
- shift exposure  
- income dependency  

#### Processing Logic
```text
Input Features
      ↓
Feature Engineering / Weighting
      ↓
Risk Score Computation
      ↓
Risk Level Classification
      ↓
Top Reason Extraction

Risk Score + Worker Income + Plan Type
                ↓
        Premium Calculation Logic
                ↓
      Plan-Level Adjustment Layer
                ↓
         Weekly Premium Output

Claim Signals + Worker Signals + Location Signals
                     ↓
             Fraud Rule Evaluation
                     ↓
              Fraud Score Generation
                     ↓
          Approval / Hold / Review Routing

Event Feed
   ↓
Threshold Check
   ↓
Zone Match
   ↓
Shift Window Match
   ↓
Claim Eligibility Decision

Weekly Income
     ↓
Hourly Income Estimation
     ↓
Loss Estimation
     ↓
Coverage Application
     ↓
Cap Validation
     ↓
Final Payout
