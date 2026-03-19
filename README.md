# 🚀 CRM Lead Scoring — Marketing Funnel Analysis

A professional data analytics pipeline using **Python (Pandas, Seaborn)** to perform lead scoring, feature engineering, and marketing funnel analysis. This project converts raw CRM data into clean insights ready for a **Power BI Dashboard**.

---

## 📊 Project Overview
The goal of this analysis is to identify key drop-off stages in the marketing funnel and pinpoint high-converting lead sources. We analyze lead behavior—such as time spent on site and page views—to categorize leads and calculate conversion rates.

### **The Marketing Funnel Define**
1.  **Visitors**: Total leads (initial awareness).
2.  **Engaged**: Leads who spent more than 300 seconds (5 minutes) on the website.
3.  **Qualified**: Leads with over 3 page views per visit.
4.  **Customers**: Successfully converted leads (`Converted` column == 1).

---

## 📂 Project Structure
```bash
├── data/
│   ├── raw/                 # Original CRM data (Lead Scoring.csv)
│   └── processed/           # Cleaned CSVs ready for Power BI
├── src/
│   ├── data_preprocessing.py # Handles cleaning and missing values
│   ├── feature_engineering.py# Creates funnel flags and metrics
│   └── funnel_analysis.py   # Conducts channel and drop-off analysis
├── notebooks/
│   └── Funnel_Analysis_Visualization.ipynb # Interactive analysis & charts
├── outputs/                 # Visualization charts (PNG)
├── requirements.txt         # Project dependencies
└── main.py                  # Master pipeline script
```

---

## 🛠️ Installation & Setup

1. **Clone and Navigate**:
   ```powershell
   git clone <your-repo-link>
   cd "future interns 3"
   ```

2. **Setup Virtual Environment**:
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```

4. **Run the Pipeline**:
   ```powershell
   python main.py
   ```

---

## 📈 Key Insights & Results

### **1. Conversion Performance**
*   **Overall Conversion Rate**: ~38.5%
*   **Top Converting Channels**:
    *   **Welingak Website**: 98% Conversion
    *   **Reference Leads**: 91% Conversion
    *   **Google (High Volume)**: 40% Conversion

### **2. Funnel Drop-off Analysis**
*   **Biggest Bottleneck**: The jump from **Visitors → Engaged**. 
*   **The "Fast" Buyer Factor**: We found that over 2,000 customers converted *without* browsing many pages, suggesting that your best prospects make quick, direct decisions.

---

## 🧰 Tools Used
*   **Python 3.11+**
*   **Pandas**: Data manipulation and cleaning
*   **Seaborn & Matplotlib**: Advanced data visualization
*   **Power BI**: (Intended) Final dashboard visualization

---
*Created for the Future Interns 3 Marketing Analytics Project.*
