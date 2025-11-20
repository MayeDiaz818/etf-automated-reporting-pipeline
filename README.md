**📈 ETF Automated Reporting Pipeline**

Automated Data Pipeline for ETF Performance, Risk, and Anomaly Detection (Python)

This project is an end-to-end automated data analytics pipeline that downloads ETF market data, performs cleaning and transformation, computes financial KPIs, detects anomalies, generates visualizations, and exports a complete reporting package.

The pipeline is built in a modular, production-style architecture, similar to analytics workflows used in banking environments.



**🚀 Features**

✔ Automated daily data ingestion

Fetches historical ETF OHLC data using yfinance.


✔ Data cleaning & resampling

Extracts clean close-price tables

Computes daily returns

Computes monthly returns using "ME" (month-end)


✔ Financial KPIs

Annualized volatility

Maximum drawdown

YTD return

Cumulative returns

Rolling 30-day volatility


✔ Anomaly detection

Using z-score thresholding (|z| > 3), the system identifies extreme return events and produces:

full anomaly dataset

anomaly summary by ETF


✔ Automated reporting

Exports professional reports:

KPI_Summary.xlsx

Anomaly_Summary.xlsx

Charts (PNG) for cumulative returns, volatility, drawdowns, heatmaps, anomalies overlay


✔ Modular code architecture

src/
    data_ingestion.py
    
    data_cleaning.py
    
    kpi_calculations.py
    
    anomaly_detection.py
    
    reporting.py
    
    
✔ Configurable via YAML

The config.yaml file controls:

ETFs to analyze

Date range

All folder paths


**📊 ETF Universe Analyzed**

The project currently analyzes:

VCN.TO – Vanguard FTSE Canada Index ETF

XIC.TO – iShares Core S&P/TSX Capped Composite Index

BTCC-B.TO – Bitcoin ETF (Purpose)

ETHH-B.TO – Ethereum ETF (Purpose)

This mix includes equity ETFs + crypto ETFs to demonstrate contrasting behavior across asset classes.


**🧱 Project Structure**

````
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

**🛠️ How to Run the Pipeline**

1. Install dependencies
```
pip install -r requirements.txt
```

2. Run the pipeline
```
python main.py
```

   
  The full report will be generated in:
  output/final_report/
  output/charts/



**📈 Sample Outputs**

KPI Summary

Contains:

Annualized Volatility

Maximum Drawdown

YTD Return


Anomaly Summary For each ETF:

of anomalies

worst daily drop (with date)

largest positive jump (with date)


Visualizations included

Cumulative returns

Rolling 30-day volatility

Drawdown curves

Anomaly overlays

Monthly returns heatmaps



**🔍 Skills Demonstrated**

Python (pandas, numpy, matplotlib, seaborn, scipy)

Data cleaning & automation

Financial analytics & KPI computation

Anomaly detection

Modular pipeline design

YAML configuration management

Data visualization

Risk analytics concepts (volatility, drawdown, extreme events)


**👩🏻‍💻 Author**

Mayerlin Díaz

Data Analyst | Python | Financial Analytics

