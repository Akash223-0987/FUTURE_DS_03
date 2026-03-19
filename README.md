# TASK-3

# 🚀 CRM Lead Scoring — Marketing Funnel Analysis

A professional end-to-end analytics project using **Python (Pandas, Seaborn/Matplotlib)** to transform raw CRM data into actionable marketing insights and a **Power BI dashboard**.

---

## 📊 Project Overview

This project analyzes how users move through a marketing funnel and identifies **conversion bottlenecks** and **high-performing channels**. We engineer behavioral features (time on site, page views) to segment leads and compute conversion metrics.

### 🔁 Funnel Definition

1. **Visitors** – Total leads (top of funnel)
2. **Engaged** – Time on site > 300 seconds
3. **Qualified** – Page Views per Visit > 3 (and Engaged)
4. **Customers** – Converted = 1 (and Qualified)

> Note: Funnel stages are modeled **sequentially** to maintain logical flow (Visitors ≥ Engaged ≥ Qualified ≥ Customers).

---

## 📂 Project Structure

```bash
├── data/
│   ├── raw/                  # Original CRM data (lead_scoring.csv)
│   └── processed/            # Cleaned/engineered CSVs (Power BI data source)
├── src/
│   ├── data_preprocessing.py # Cleaning, missing values, and data typing
│   ├── feature_engineering.py# Funnel logic & behavioral flags
│   └── funnel_analysis.py    # Channel KPIs and drop-off calculations
├── notebooks/
│   └── Funnel_Analysis_Visualization.ipynb # Interactive visual analysis
├── powerbi_dashboard/
│   └── Marketing Funnel & Conversion Performance Analysis.pbix # Interactive dashboard
├── outputs/                  # Exported static charts (PNG)
├── main.py                   # Master script to run the full pipeline
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## 🛠️ Setup & Run

```powershell
git clone <your-repo-link>
cd "future interns 3"
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python main.py
```
---
## 📂 Dataset

The project uses a **Lead Scoring (CRM) Dataset** containing user behavior, engagement metrics, and conversion information.

Source: Kaggle  
[https://www.kaggle.com/datasets/amritachatterjee09/lead-scoring-dataset]

### 📌 Key Features:

* **Lead Source** (Google, Direct, Facebook, etc.)
* **Time Spent on Website**
* **Page Views Per Visit**
* **Converted (0/1)**
* **Country / City**

### 🎯 Purpose:

Used to build a **marketing funnel (Visitors → Engaged → Qualified → Customers)**, analyze drop-offs, and evaluate conversion performance across channels.

---

---

## 📈 Key Results

### 1) Conversion Performance

* **Overall Conversion Rate**: ~38.54%
* **Top Channels**:

  * **Welingak Website** ~98%
  * **Reference** ~91%
  * **Google (high volume)** ~40%

### 2) Funnel Insights

* **Largest drop-off**: **Visitors → Engaged** (top-of-funnel friction)
* **Mid/Bottom funnel**: Strong progression and closing efficiency
* **Fast-buyer behavior**: A notable segment converts quickly with fewer page views (high intent)

---

## 📊 Power BI Dashboard

The processed outputs power an interactive dashboard featuring:

* KPI Cards (Visitors, Engaged, Qualified, Customers, Conversion %)
* Funnel Chart (stage-wise counts)
* Channel Conversion (bar chart)
* Drop-off Analysis (stage gaps)
* Geographic View (Country/City map)
* Key Insights & Recommendations

---

## 🧠 Key Insights (Top 6)

1. **Moderate User Engagement** – ~59.6% of visitors engage; room to improve first interaction.
2. **Critical Entry Drop-off** – Biggest loss at Visitors → Engaged.
3. **Strong Mid-Funnel Progression** – Effective nurturing to Qualified stage.
4. **High Close Rate** – Qualified leads convert at a high rate.
5. **Channel Variation** – Welingak Website & Reference lead; Facebook underperforms.
6. **Overall Effectiveness** – 38.54% conversion with top-of-funnel optimization opportunity.

---

## 🚀 Recommendations

1. **Improve Landing Experience** – Faster pages, clearer CTAs, better messaging.
2. **Refine Targeting** – Focus on high-intent audiences; optimize low-performing channels.
3. **Scale High-Performers** – Invest more in Welingak Website & Reference.
4. **Strengthen Nurturing** – Email/retargeting to move Engaged → Qualified.
5. **Re-engage Drop-offs** – Retarget visitors who didn’t engage (display/social/email).
6. **Geo Optimization** – Prioritize high-performing regions.

---

## 🧰 Tech Stack

* **Python 3.11+**
* **Pandas** (data wrangling)
* **Seaborn/Matplotlib/Plotly** (EDA & charts)
* **Power BI** (dashboard)

---

## 📦 Final Deliverables

The automated pipeline generates several outputs located in the `data/processed/` and `outputs/` directories:

*   **Cleaned Datasets**: All behavioral flags and funnel markers (`lead_data_final.csv`).
*   **KPI Exports**: Aggregated insights for Channel and Funnel performance.
*   **Static Visuals**: Professional charts for documentation and pre-viewing.
*   **Power BI File**: The primary interactive dashboard logic.

---

## 👨‍💻 Author

**Task 3 Solution developed by [D AKASH DORA]**
*Data Science Intern at Future Interns*
*Contact: [akashdora2@gmail.com]*
