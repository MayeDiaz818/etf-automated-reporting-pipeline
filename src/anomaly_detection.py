import pandas as pd
import numpy as np
from scipy import stats


def detect_anomalies(daily_returns, threshold=3):
    """
    Detects anomalies using z-scores.
    Returns:
    - anomaly_df: full list of anomalies
    - summary_df: summarized metrics per ETF
    """

    # --------------------------------------------------------
    # 1. Compute z-scores for each ETF
    # --------------------------------------------------------
    z_scores = daily_returns.apply(
        lambda col: stats.zscore(col, nan_policy='omit')
    )

    # --------------------------------------------------------
    # 2. Build dataframe of anomalies
    # --------------------------------------------------------
    anomaly_records = []

    for etf in daily_returns.columns:
        # Mask where absolute z-score > threshold
        mask = z_scores[etf].abs() > threshold
        etf_anoms = daily_returns[etf][mask]

        # Record anomalies
        for date, value in etf_anoms.items():
            anomaly_records.append([date, etf, value])

    anomaly_df = pd.DataFrame(
        anomaly_records,
        columns=["date", "ticker", "daily_return"]
    ).sort_values("date").reset_index(drop=True)

    # --------------------------------------------------------
    # 3. Build anomaly summary by ETF
    # --------------------------------------------------------
    summary_records = []

    for etf in daily_returns.columns:
        etf_rows = anomaly_df[anomaly_df['ticker'] == etf]

        if etf_rows.empty:
            summary_records.append([etf, 0, None, None, None, None])
            continue

        total = etf_rows.shape[0]
        worst_drop = etf_rows['daily_return'].min()
        worst_drop_date = etf_rows.loc[
            etf_rows['daily_return'].idxmin(), 'date'
        ]

        biggest_jump = etf_rows['daily_return'].max()
        biggest_jump_date = etf_rows.loc[
            etf_rows['daily_return'].idxmax(), 'date'
        ]

        summary_records.append([
            etf,
            total,
            worst_drop,
            worst_drop_date,
            biggest_jump,
            biggest_jump_date
        ])

    summary_df = pd.DataFrame(
        summary_records,
        columns=[
            "ETF",
            "# Anomalies",
            "Worst Drawdown Return",
            "Date of Worst Drop",
            "Largest Positive Return",
            "Date of Largest Jump"
        ]
    )

    print(f"✔ Anomaly detection completed. Total anomalies: {len(anomaly_df)}")

    return anomaly_df, summary_df
