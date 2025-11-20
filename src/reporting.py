import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ================================================================
# UTILS
# ================================================================
def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


# ================================================================
# 1. SAVE KPI REPORT
# ================================================================
def save_kpi_report(kpi_summary, paths):
    report_path = os.path.join(paths["reports"], "KPI_Summary.xlsx")
    ensure_dir(paths["reports"])
    kpi_summary.to_excel(report_path)
    print(f"✔ KPI report saved: {report_path}")


# ================================================================
# 2. SAVE ANOMALY REPORT
# ================================================================
def save_anomaly_report(anomaly_summary, paths):
    report_path = os.path.join(paths["reports"], "Anomaly_Summary.xlsx")
    ensure_dir(paths["reports"])
    anomaly_summary.to_excel(report_path, index=False)
    print(f"✔ Anomaly summary saved: {report_path}")


# ================================================================
# 3. BUILD HEATMAP DATAFRAME
# ================================================================
def build_heatmap_table(monthly_returns, etf):
    s = monthly_returns[etf].copy()
    df = s.to_frame(name="return")
    df["Year"] = df.index.year
    df["Month"] = df.index.month
    heatmap_df = df.pivot(index="Year", columns="Month", values="return")
    return heatmap_df.sort_index(axis=1)


# ================================================================
# 4. SAVE ALL CHARTS
# ================================================================
def save_charts(close_df, daily_returns, drawdown_curves, rolling_vol_30d, monthly_returns, anomaly_df, paths):
    charts_path = paths["charts"]
    ensure_dir(charts_path)

    # ------------------------------------------------------------
    # 1. Cumulative Returns
    # ------------------------------------------------------------
    plt.figure(figsize=(12,6))
    for etf in daily_returns.columns:
        plt.plot((1 + daily_returns[etf]).cumprod() - 1, label=etf)
    plt.title("Cumulative Returns of ETFs")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Return")
    plt.legend()
    plt.grid(True, alpha=0.3)
    cum_file = os.path.join(charts_path, "cumulative_returns.png")
    plt.savefig(cum_file, dpi=300, bbox_inches="tight")
    plt.close()

    # ------------------------------------------------------------
    # 2. Rolling 30-Day Volatility
    # ------------------------------------------------------------
    plt.figure(figsize=(12,6))
    for etf in rolling_vol_30d.columns:
        plt.plot(rolling_vol_30d[etf], label=etf)
    plt.title("30-Day Rolling Annualized Volatility")
    plt.xlabel("Date")
    plt.ylabel("Annualized Volatility")
    plt.legend()
    plt.grid(True, alpha=0.3)
    vol_file = os.path.join(charts_path, "rolling_volatility_30d.png")
    plt.savefig(vol_file, dpi=300, bbox_inches="tight")
    plt.close()

    # ------------------------------------------------------------
    # 3. Drawdown Curves
    # ------------------------------------------------------------
    plt.figure(figsize=(12,6))
    for etf in drawdown_curves.columns:
        plt.plot(drawdown_curves[etf], label=etf)
    plt.title("Drawdown Curves")
    plt.xlabel("Date")
    plt.ylabel("Drawdown")
    plt.legend()
    plt.grid(True, alpha=0.3)
    dd_file = os.path.join(charts_path, "drawdown_curves.png")
    plt.savefig(dd_file, dpi=300, bbox_inches="tight")
    plt.close()

    # ------------------------------------------------------------
    # 4. Anomalies Overlay (Subplots)
    # ------------------------------------------------------------
    fig, axes = plt.subplots(4, 1, figsize=(14, 18), sharex=True)
    for i, etf in enumerate(daily_returns.columns):
        axes[i].plot(daily_returns[etf], color="steelblue", label=f"{etf} Returns")
        etf_anoms = anomaly_df[anomaly_df["ticker"] == etf]
        axes[i].scatter(etf_anoms["date"], etf_anoms["daily_return"], color="red", label="Anomaly", zorder=5)
        axes[i].set_title(f"Anomaly Overlay — {etf}")
        axes[i].grid(True, alpha=0.3)
        axes[i].legend()
    plt.tight_layout()
    anom_file = os.path.join(charts_path, "anomaly_overlay_subplots.png")
    plt.savefig(anom_file, dpi=300, bbox_inches="tight")
    plt.close()

    # ------------------------------------------------------------
    # 5. Monthly Returns Heatmaps
    # ------------------------------------------------------------
    fig, axes = plt.subplots(4, 1, figsize=(14, 18))
    for i, etf in enumerate(daily_returns.columns):
        heatmap_df = build_heatmap_table(monthly_returns, etf)
        sns.heatmap(
            heatmap_df, cmap="RdYlGn", center=0, annot=True, fmt=".2%", 
            cbar=True, linewidths=0.5, ax=axes[i]
        )
        axes[i].set_title(f"Monthly Returns Heatmap — {etf}")
    plt.tight_layout()
    heatmap_file = os.path.join(charts_path, "monthly_heatmaps.png")
    plt.savefig(heatmap_file, dpi=300, bbox_inches="tight")
    plt.close()

    print("✔ All charts saved successfully.")
