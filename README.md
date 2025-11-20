# UN-SDG East Africa Dashboard Project

## 📌 Overview
This project builds a reproducible **data science + Power BI dashboard** to track progress on the United Nations Sustainable Development Goals (SDGs) across East African countries. It integrates open datasets from the UN, World Bank, WHO, and UNICEF, applies AI/ML forecasting, and delivers actionable insights for policymakers, NGOs, and donors.

## 🎯 Objectives
- Collect and harmonize official UN/World Bank indicators.
- Build a **star schema** for clean analytics.
- Apply **AI/ML models** (Prophet, anomaly detection, composite scoring).
- Visualize results in **Power BI** with interactive maps, KPIs, and forecasts.
- Provide transparent documentation and governance for reproducibility.

## 🌍 Scope
Countries covered: Kenya, Uganda, Tanzania, Rwanda, Burundi, South Sudan, and optionally DRC.  
Indicators: Health (SDG 3), Education (SDG 4), Water & Sanitation (SDG 6), Climate (SDG 13).

## 🛠️ Tech Stack
- **Python** (pandas, pyarrow, scikit-learn, prophet)
- **Conda** for environment management
- **Power BI Desktop** for visualization
- **GitHub** for version control & CI/CD
- **Open-source tools**: Prefect (pipelines), MkDocs (documentation)

## 📊 Key Insights
- Forecasts show which countries are **on track vs. off track** for 2030 SDG targets.
- Anomaly detection highlights **sudden declines** in food security or health.
- Composite SDG Index enables **prioritization of funding** and interventions.
- Dashboards connect SDG data to **UN challenges** like famine, conflict, and climate shocks.

## 📂 Project Structure

un-sdg-eastafrica/
├─ src/ # Python scripts (ingest, transform, ML)
├─ notebooks/ # Jupyter notebooks for analysis
├─ data_raw/ # Raw datasets (excluded from Git)
├─ data_curated/ # Cleaned parquet/CSV files
├─ bi/ # Power BI models and reports
├─ docs/ # Documentation (dictionary, governance, runbook)
