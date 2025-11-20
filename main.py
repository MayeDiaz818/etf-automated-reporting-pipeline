import os
import yaml
from datetime import datetime

from src.data_ingestion import download_etf_data
from src.data_cleaning import clean_data
from src.kpi_calculations import calculate_kpis
from src.anomaly_detection import detect_anomalies
from src.reporting import save_kpi_report, save_anomaly_report, save_charts


# ------------------------------------------------------------
# Load YAML configuration
# ------------------------------------------------------------
def load_config(path="config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)


# ------------------------------------------------------------
# Create required directories
# ------------------------------------------------------------
def ensure_directories(paths):
    for p in paths.values():
        os.makedirs(p, exist_ok=True)


# ------------------------------------------------------------
# MAIN PIPELINE
# ------------------------------------------------------------
def main():
    print("\n🚀 Starting Automated ETF Reporting Pipeline...\n")

    config = load_config()
    etfs = config["etfs"]

    start = config["start_date"]
    end = (
        datetime.today().strftime("%Y-%m-%d")
        if config["end_date"] == "today"
        else config["end_date"]
    )

    paths = config["paths"]
    ensure_directories(paths)

    print("📥 Step 1 — Downloading ETF Data")
    df_raw = download_etf_data(etfs, start, end)
    df_raw.to_csv(os.path.join(paths["raw"], "etf_raw.csv"))

    print("🧹 Step 2 — Cleaning Data")
    close_df, daily_returns, monthly_returns = clean_data(df_raw, paths)

    print("📊 Step 3 — Calculating KPIs")
    kpi_summary, cumulative_returns, rolling_vol_30d = calculate_kpis(close_df, daily_returns)

    print("⚠️ Step 4 — Detecting Anomalies")
    anomaly_df, anomaly_summary = detect_anomalies(daily_returns)

    print("📑 Step 5 — Exporting Reports & Charts")
    save_kpi_report(kpi_summary, paths)
    save_anomaly_report(anomaly_summary, paths)

    save_charts(
        close_df,
        daily_returns,
        cumulative_returns,
        rolling_vol_30d,
        monthly_returns,
        anomaly_df,
        paths
    )

    print("\n🎉 Pipeline completed successfully!")
    print("📁 Reports saved to:", paths["reports"])
    print("🖼️ Charts saved to:", paths["charts"])
    print("\nDone.\n")


# ------------------------------------------------------------
# Trigger pipeline
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
