<div align="center">

# 🏦 TBSM BANK · ATM Operational Intelligence

### *Transforming raw ATM data into actionable banking decisions*

[![Live App](https://img.shields.io/badge/🌐_Live_App-tbsmbank9171.streamlit.app-22D3EE?style=for-the-badge)](https://tbsmbank9171.streamlit.app/)
[![GitHub](https://img.shields.io/badge/GitHub-Ankit4981-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Ankit4981/IDAI102-100390-TBSM-Bank)
[![Drive](https://img.shields.io/badge/Google_Drive-Assets-34A853?style=for-the-badge&logo=googledrive&logoColor=white)](https://drive.google.com/drive/folders/1yffC_PSJ6vgRyNTXsW_1qdFrdxMbHdEi?usp=sharing)

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35.0-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.4.2-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Pandas](https://img.shields.io/badge/Pandas-2.2.2-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![License](https://img.shields.io/badge/License-Academic-8B5CF6?style=for-the-badge)](.)

---

## 🔗 Quick Links

| | Link |
|---|---|
| 🌐 **Live App** | [tbsmbank9171.streamlit.app](https://tbsmbank9171.streamlit.app/) |
| 💻 **GitHub Repository** | [Ankit4981/IDAI102-100390-TBSM-Bank](https://github.com/Ankit4981/IDAI102-100390-TBSM-Bank) |
| 📁 **Google Drive (Assets)** | [Open Drive Folder](https://drive.google.com/drive/folders/1yffC_PSJ6vgRyNTXsW_1qdFrdxMbHdEi?usp=sharing) |

---

> **Course:** Data Mining · Formative Assessment 2  
> **Institution:** CRS · Artificial Intelligence Programme  
> **App Version:** v6 · Deep-Space Nebula Theme

</div>

---

## 📖 Table of Contents

- [🎯 Project Overview](#-project-overview)
- [✨ Features](#-features)
- [🖥️ Screenshots & Pages](#️-screenshots--pages)
- [📂 Project Structure](#-project-structure)
- [📊 Dataset](#-dataset)
- [🚀 Getting Started](#-getting-started)
- [🔐 Login Credentials](#-login-credentials)
- [🧠 Data Mining Pipeline](#-data-mining-pipeline)
- [📈 Key Insights](#-key-insights)
- [🛠️ Tech Stack](#️-tech-stack)
- [👥 User Roles](#-user-roles)

---

## 🎯 Project Overview

**TBSM Bank ATM Intelligence** is an interactive data mining dashboard built for **FinTrust Bank Ltd.** (fictionalised as TBSM Bank). It analyses a network of **100 ATMs** across Urban, Suburban, and Rural locations — uncovering cash demand patterns, detecting anomalies, and delivering intelligent replenishment recommendations.

This project covers the full data science workflow:

```
Raw Data  ──►  Cleaning  ──►  EDA  ──►  Clustering  ──►  Anomaly Detection  ──►  Forecasting  ──►  Insights
```

| Metric | Value |
|---|---|
| 📋 Records Analysed | 1,200 ATM transactions |
| 🏧 ATMs Monitored | 100 machines |
| 📅 Date Range | January – December 2023 |
| 🔍 Anomalies Detected | ~3% of dataset (Z-score + IQR dual method) |
| 🎯 Clusters Identified | 3 demand segments (High / Medium / Low) |
| 💰 Projected Annual Savings | ₹12.4 Cr from optimised refill scheduling |

---

## ✨ Features

### 🔐 Secure Multi-Role Login
- Role-based access: **Administrator**, **Data Analyst**, **Branch Manager**
- Animated login screen with live data stream effects
- Session management with clean sign-out

### 🏠 Live Dashboard Home
- Real-time KPI cards (Total Withdrawals, Deposits, Active ATMs, Anomalies)
- Full-year daily withdrawal trend with 7-day moving average
- One-click navigation to all analysis modules

### 📤 Data Upload & Validation
- Dataset preview with field mapping reference
- Data health report (missing values, record count, unique ATMs)
- Export sample CSV (first 100 rows)

### 🧹 Data Cleaning Pipeline
- Step-by-step processing log with completion tracking
- Date conversion, label encoding, normalisation, and error checking
- Visual progress bar — run individual steps or all at once

### 📊 Exploratory Data Analysis (EDA)
Interactive, filter-driven exploration across 5 analysis tabs:

| Tab | What You'll Find |
|---|---|
| 📍 By Location | Avg withdrawals per location type + ATM drill-down |
| 📅 By Day & Time | Day-of-week patterns + time-of-day peaks |
| 🌤️ Weather Impact | Withdrawal variation by weather condition |
| 🌡️ Correlations | Full correlation heatmap of numeric features |
| 📐 Distributions | Histogram, median/mean lines, daily trend with MA |

### ⚠️ Anomaly Detection
- **Dual-method detection:** Z-score (|z| > 3.0) + IQR (Q3 + 1.5×IQR)
- Risk-scored anomaly cards (High / Medium / Low) with holiday correlation
- Interactive investigation workflow — mark anomalies as reviewed
- Z-score distribution chart + anomaly timeline plot

### 🔮 Forecasting
- 14-day cash demand forecast per location (Urban / Suburban / Rural)
- 7-day and 30-day moving averages with ±7% confidence bands
- Month × Day-of-week demand heatmap for seasonal planning
- Top 5 ATMs by average demand per location

### 💡 Insights & Strategy
- Hero optimisation protocol with 1-click strategy application
- Interactive simulation slider — model the financial impact of any cash increase %
- Cluster scatter plot (Withdrawals vs Deposits, k=3)
- Elbow method chart confirming optimal cluster count

### 📖 Data Storyboard
- 8-step analytical narrative from problem definition to recommendations
- Summary completion panel with key project stats
- Export full storyboard as CSV

---

## 🖥️ Screenshots & Pages

| Page | Description |
|---|---|
| 🔐 Login | Animated deep-space login with role selection |
| 🏠 Home | Live dashboard with network KPIs and trend chart |
| 🎯 Project Scope | Business context, stakeholders, and key questions |
| 📤 Data Upload | Dataset preview and field validation |
| 🧹 Data Cleaning | Step-by-step cleaning pipeline with progress tracking |
| 📊 Exploration | 5-tab interactive EDA with dynamic filters |
| ⚠️ Anomaly Detection | Triage dashboard with risk-scored anomaly cards |
| 🔮 Forecasting | 14-day demand forecasts per location |
| 💡 Insights | Strategy panel, simulation, and cluster analysis |
| 📖 Storyboard | Full project narrative from data to decisions |

---

## 📂 Project Structure

```
tbsm-atm-intelligence/
│
├── app.py                          # Main Streamlit application (v6)
├── requirements.txt                # Python dependencies
├── atm_cash_management_dataset.csv # ATM transaction dataset (1,200 records)
└── README.md                       # You are here!
```

---

## 📊 Dataset

The dataset (`atm_cash_management_dataset.csv`) contains **1,200 ATM transaction records** with the following features:

| Column | Type | Description |
|---|---|---|
| `ATM_ID` | String | Unique ATM identifier (ATM001 – ATM100) |
| `Date` | Date | Transaction date (Jan–Dec 2023) |
| `Day_of_Week` | Category | Monday through Sunday |
| `Time_of_Day` | Category | Morning / Afternoon / Evening / Night |
| `Total_Withdrawals` | Numeric | Total cash withdrawn (₹) |
| `Total_Deposits` | Numeric | Total cash deposited (₹) |
| `Location_Type` | Category | Urban / Suburban / Rural |
| `Holiday_Flag` | Boolean | 1 if public holiday, 0 otherwise |
| `Special_Event_Flag` | Boolean | 1 if special event nearby, 0 otherwise |
| `Previous_Day_Cash_Level` | Numeric | Cash level at end of previous day (₹) |
| `Weather_Condition` | Category | Sunny / Cloudy / Rainy / Stormy |
| `Nearby_Competitor_ATMs` | Integer | Count of competitor ATMs within vicinity |
| `Cash_Demand_Next_Day` | Numeric | Target variable — next-day cash demand (₹) |

> **Note:** The app also generates a synthetic dataset of 1,200 records at runtime (for reproducibility) using `numpy` with `random_seed=42`.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- pip package manager

### 1️⃣ Clone or Download the Repository

```bash
git clone https://github.com/Ankit4981/IDAI102-100390-TBSM-Bank.git
cd IDAI102-100390-TBSM-Bank
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

The following packages will be installed:

```
streamlit==1.35.0
numpy==1.26.4
pandas==2.2.2
matplotlib==3.8.4
seaborn==0.13.2
scikit-learn==1.4.2
scipy==1.13.0
```

### 3️⃣ Run the Application

```bash
streamlit run app.py
```

### 4️⃣ Open in Browser

The app will automatically open at:
```
http://localhost:8501
```

---

## 🔐 Login Credentials

Use any of the following demo accounts to access the dashboard:

| Role | Username | Password | Access Level |
|---|---|---|---|
| 🔴 Administrator | `admin` | `1234` | Full access to all modules |
| 🔵 Data Analyst | `analyst` | `analyst123` | Analysis & exploration |
| 🟢 Branch Manager | `manager` | `mgr123` | Reports & insights |

---

## 🧠 Data Mining Pipeline

This project implements a complete 8-stage data mining workflow:

```
Stage 1 ── Project Scope Definition
           └── Business questions, stakeholders, KPIs

Stage 2 ── Data Collection & Upload
           └── 1,200 ATM records, 13 features, Jan–Dec 2023

Stage 3 ── Data Cleaning & Preparation
           └── Date parsing, label encoding, normalisation, error detection

Stage 4 ── Exploratory Data Analysis (EDA)
           └── Distribution plots, time trends, weather impact, heatmaps

Stage 5 ── K-Means Clustering (k=3)
           └── Elbow method, silhouette validation, demand segmentation

Stage 6 ── Anomaly Detection
           └── Z-score (|z|>3.0) + IQR dual flagging, holiday correlation

Stage 7 ── Demand Forecasting
           └── 7/30-day moving averages, 14-day linear trend forecast

Stage 8 ── Insights & Recommendations
           └── Replenishment protocol, simulation model, storyboard export
```

---

## 📈 Key Insights

Findings from the analysis of the ATM network:

- 🏙️ **Urban ATMs** average **₹50,000/day** — 3× higher than Rural (₹15,000/day)
- 📅 **Weekends** drive **18% higher demand** — pre-load cash every Friday evening
- ⏰ **Afternoon & Evening** slots account for **60% of all transactions**
- 🎉 **Holiday periods** spike withdrawals by approximately **+15%**
- ⚠️ **~3% of transactions** are anomalous — primarily driven by holiday + event combinations
- 🔵 **3 clear demand clusters** identified — enabling targeted, cost-efficient refill strategies
- 💰 Applying the recommended **Urban +20% Friday pre-load** protocol projects **₹12.4 Cr annual savings**

---

## 🛠️ Tech Stack

| Technology | Version | Purpose |
|---|---|---|
| [Streamlit](https://streamlit.io) | 1.35.0 | Interactive web application framework |
| [Pandas](https://pandas.pydata.org) | 2.2.2 | Data manipulation and analysis |
| [NumPy](https://numpy.org) | 1.26.4 | Numerical computing and synthetic data generation |
| [Matplotlib](https://matplotlib.org) | 3.8.4 | Custom dark-theme data visualisations |
| [Seaborn](https://seaborn.pydata.org) | 0.13.2 | Heatmaps and statistical plots |
| [Scikit-Learn](https://scikit-learn.org) | 1.4.2 | K-Means clustering, StandardScaler, LabelEncoder |
| [SciPy](https://scipy.org) | 1.13.0 | Z-score anomaly detection |

**UI & Design:**
- Custom CSS with Deep-Space Nebula animated background
- Glassmorphism KPI cards with neon glow effects
- Fonts: Orbitron, Syne, Rajdhani, JetBrains Mono (Google Fonts)
- Animated circuit-grid overlay and floating ambient orbs

---

## 👥 User Roles

| Role | Capabilities |
|---|---|
| **Administrator** | Full access — all pages, data export, strategy application |
| **Data Analyst** | EDA, clustering, anomaly investigation, forecasting |
| **Branch Manager** | Insights dashboard, simulation, storyboard, report export |

---

## 📋 Academic Context

| Field | Detail |
|---|---|
| Course | Data Mining |
| Programme | Artificial Intelligence |
| Assessment | Formative Assessment 2 (FA-2) |
| Marks | 20 Marks |
| Learning Outcomes | EDA · Clustering · Anomaly Detection · Interactive Python Script |

**Intended Learning Outcomes Assessed:**
- ✅ Conduct exploratory data analysis (EDA) to identify patterns and trends
- ✅ Apply clustering techniques to group ATMs by demand behaviour
- ✅ Detect anomalies in withdrawals during holidays and events

---

<div align="center">

**© 2026 TBSM BANK · ATM Operational Intelligence · v6.0**

*Built with ❤️ using Python & Streamlit*

</div># IDAI102-100390-TBSM-Bank
