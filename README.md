# 📈 ETF Automated Reporting Pipeline  
### Automated Data Pipeline for ETF Performance, Risk, and Anomaly Detection (Python)

This project is an **end-to-end automated data analytics pipeline** that downloads ETF market data, cleans and structures it, computes financial KPIs, detects anomalous events, generates visualizations, and exports a comprehensive reporting package.

The design follows a **modular, production-style architecture**, similar to reporting workflows used in financial institutions.

---

## 🚀 Features

### ✔ Automated data ingestion  
Downloads historical OHLC data for selected ETFs using `yfinance`.

### ✔ Data cleaning & transformation  
- Extracts structured close-price tables  
- Computes **daily returns**  
- Computes **monthly returns** using updated `"ME"` (month-end) resampling  
- Saves clean datasets for downstream analysis

### ✔ Financial KPIs  
Includes:
- Cumulative returns  
- Annualized volatility  
- Maximum drawdown  
- Year-to-date (YTD) return  
- Rolling 30-day volatility  

### ✔ Anomaly detection  
Using z-scores (`|z| > 3`), the pipeline identifies extreme return events and produces:
- A **full anomaly dataset**
- A **summary report** with worst drops and largest jumps

### ✔ Automated reporting  
Exports:
- `KPI_Summary.xlsx`  
- `Anomaly_Summary.xlsx`  
- All visualizations (PNG):  
  - Cumulative returns  
  - Drawdown curves  
  - Rolling volatility  
  - Monthly heatmaps  
  - Anomaly overlays  

---

## 📊 ETF Universe Analyzed

The project evaluates the following ETFs:

- **VCN.TO** — Vanguard FTSE Canada Index  
- **XIC.TO** — iShares Core S&P/TSX Composite Index  
- **BTCC-B.TO** — Purpose Bitcoin ETF  
- **ETHH-B.TO** — Purpose Ethereum ETF  

A mix of equity and crypto ETFs highlights differences in risk and return behavior.

---

## 🧱 Project Structure

main.py
config.yaml

src/
data_ingestion.py
data_cleaning.py
kpi_calculations.py
anomaly_detection.py
reporting.py

data/
raw/
clean/

output/
charts/
final_report/

---

## 🛠️ How to Run the Pipeline

### 1. Install dependencies

pip install -r requirements.txt


### 2. Run the automated pipeline

python main.py


Output files will be generated in:

output/charts/
output/final_report/


---

## 📈 Sample Outputs

### KPI Summary (Excel)
Includes:
- Annualized Volatility  
- Maximum Drawdown  
- YTD Return  

### Anomaly Summary (Excel)
Includes, per ETF:
- Number of anomalies  
- Worst drop + date  
- Largest jump + date  

### Visualizations (PNG)
- `cumulative_returns.png`  
- `drawdown_curves.png`  
- `rolling_volatility_30d.png`  
- `monthly_heatmaps.png`  
- `anomaly_overlay_subplots.png`  

---

## 🔍 Skills Demonstrated

- Python (Pandas, NumPy, Matplotlib, Seaborn, SciPy)  
- Data automation & pipeline design  
- Financial analytics (risk, volatility, drawdown)  
- Anomaly detection  
- Data visualization best practices  
- Modular programming (multi-file architecture)  
- YAML configuration handling  
- Reporting automation  

---

## 👩🏻‍💻 Author

**Mayerlin Díaz**  
Data Analyst • Python • Financial Analytics  
Toronto, Canada  

