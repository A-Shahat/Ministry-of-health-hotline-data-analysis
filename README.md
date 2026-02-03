# Egyptian Ministry of Health — Hotline Analysis
### Analyzing Citizen Complaints & Service Efficiency (2025)

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Key Findings](#-key-findings)
- [Monte Carlo Forecasting](#-monte-carlo-forecasting)
- [Methodology](#-methodology)
- [Technologies](#-technologies)
- [Recommendations](#-recommendations)
- [About the Analyst](#-about-the-analyst)

---

## 🎯 Project Overview

### The Problem

The Egyptian Ministry of Health operates a national citizen hotline handling ~48,000 calls per year. 
Leadership needs clear answers to:
- What are citizens calling about most frequently?
- When is the hotline busiest — and are we staffed accordingly?
- Are complaints being resolved, or is the backlog growing?
- Which employees are overloaded, and which have capacity?
- What should we expect in the coming months?

### The Solution

End-to-end analysis of one full year of real operational hotline data — from 
raw Arabic data through translation, anonymization, deep exploration, 
statistical testing, and Monte Carlo forecasting of future volumes.

### Dataset

| Property | Value |
|----------|-------|
| Source | Ministry of Health Hotline System (live operational data) |
| Records | ~48,000 citizen calls |
| Period | Full year 2025 (13 months) |
| Columns | 20 features (timestamps, categories, employees, status) |
| Privacy | Caller names and phone numbers cryptographically hashed |

> **Note:** This is **real workplace data**, not a synthetic or Kaggle dataset. 
> All personally identifiable information has been anonymized before analysis.

---

## 🔍 Key Findings

### 1. Call Volume Patterns

- Clear **peak hours** identified — hotline receives 87 times more calls 
  during the busiest window than the quietest
- **Weekday vs weekend** split shows significant operational difference 
  (Egypt weekend: Friday–Saturday)

---

### 2.  Complaint Landscape

- **Treatment, general inquiries and minister's council complaints** account for over 60% of all calls
- **44 distinct entities** (departments) receive complaints — but the top 10 handle 80%+ of volume

---

### 3.  Employee Workload Imbalance

- Workload is **not evenly distributed** — some employees handle 2–3x 
  more calls than others
- Monte Carlo forecasts show this imbalance will **persist and widen** 
  if left unaddressed

---

### 4. Statistical Validation

- **ANOVA test:** Monthly call volumes differ significantly across months 
  (p < 0.05) — seasonal planning is necessary

---

## Monte Carlo Forecasting

### What It Is

Monte Carlo simulation runs **10,000 random scenarios** based on historical 
call volume patterns. Instead of a single prediction, it produces a 
**probability distribution** — showing the realistic range of future outcomes.

### What We Forecasted

| Forecast | Purpose |
|----------|---------|
| **Total monthly volume** | How many calls next 6 months? |
| **Per-employee volume** | Individual workload predictions |
|

---

## 🔬 Methodology

### Analysis Pipeline

```
Raw Arabic Data (Excel)
        ↓
  Anonymization (hash PII)
        ↓
  Translation (Arabic → English)
        ↓
  Data Cleaning (nulls, duplicates, dtypes)
        ↓
  Feature Engineering (time components)
        ↓
  ┌─────────────────────────────────┐
  │  Exploratory Data Analysis      │
  │    - Volume & temporal patterns  │
  │    - Complaint classification   │
  │    - Employee performance       │
  └─────────────────────────────────┘
        ↓
  Statistical Testing
    - ANOVA (monthly volume differences)
        ↓
  Monte Carlo Simulation
    - 10,000 simulations per forecast
    - Total + per-employee forecasts
    - Confidence interval generation
        ↓
  Recommendations & Staffing Insights
```
### Statistical Methods

| Method | Purpose | Result |
|--------|---------|--------|
| ANOVA | Monthly volume equality | Significant / Not |
| Monte Carlo | Future volume forecasting | 6-month probability bands |
| Percentile Analysis | Confidence intervals | 5/25/50/75/95 bands |

---

##  Technologies

| Tool | Role |
|------|------|
| **Python 3.9+** | Primary language |
| **Pandas** | Data manipulation, grouping, pivoting |
| **NumPy** | Monte Carlo simulation, statistical calculations |
| **Matplotlib** | Static charts (heatmaps, forecast plots) |
| **Plotly** | Interactive bar/line charts |
| **SciPy** |  ANOVA hypothesis tests |
| **googletrans** | Arabic → English translation |

---

##  Recommendations

### Immediate Actions (This Week)
* Start a marketing campaign immediately ensuring that hotline works during weekends
* Increase staffing during peak hours
* Add 2 agents during identified peak window
* Expected impact: Reduce wait times by ~30%
* Prioritize top complaint type
* Allocate dedicated team for most common complaint category
* Create fast-track resolution process

### Short-Term (1–3 Months)
* Balance employee workload
* Redistribute calls between high performers and low ones
* Implement round-robin assignment during peak hours
* Track weekly to identify bottlenecks of complaint resolution

### Long-Term (3–12 Months)

* Predictive staffing model
* Use historical volume patterns to forecast future demand
* Automate shift scheduling based on predicted call volume
* Complaint automation
* For most common, simple complaint types: explore chatbot or automated FAQ routing
* Reserve human agents for complex or sensitive cases

---

## 👤 About the Analyst

**Ahmed Abdelmoneim El-Shahat**  
Pharmacist & Healthcare Data Analyst | Egyptian Ministry of Health

This analysis was built using **real operational data from my day job**. 
It combines domain knowledge (pharmacy, public health, government operations) 
with technical skills (Python, statistics, Monte Carlo simulation) to 
deliver actionable insights for the Ministry.

| | |
|---|---|
| 📧 Email | ahmed.elshahat.eru2016@gmail.com |
| 💼 LinkedIn | [linkedin.com/in/ahmed-shahat](https://linkedin.com/in/ahmed-shahat) |
| 🐱 GitHub | [github.com/A-Shahat](https://github.com/A-Shahat) |
| 🌐 Other Project | [Egyptian Healthcare Distribution Analysis](https://github.com/A-Shahat/egyptian-healthcare-analysis) |

---

## 🙏 Acknowledgments

- **Ministry of Health** — for the operational data and real-world context
- **Open source community** — Python, Pandas, Plotly, SciPy
- **Harvard CS50, Stanford SQL, Prof. Brunton** — foundational skills

---
