import pandas as pd
import numpy as np
import os

def clean_data(df_raw, paths):
    """
    Cleans the downloaded ETF dataset and prepares:
    - clean close price table
    - daily returns
    - monthly returns
    """

    # Extract list of tickers from MultiIndex columns
    tickers = sorted({col[0] for col in df_raw.columns})

    # Build a clean Close prices DataFrame
    close_df = pd.DataFrame()

    for ticker in tickers:
        # Extract Close column for this ticker
        close_df[ticker] = df_raw[(ticker, "Close")]

    # Drop rows with missing values
    close_df = close_df.dropna()

    # Save cleaned data
    clean_path = os.path.join(paths["clean"], "etf_clean_close.csv")
    close_df.to_csv(clean_path)

    # Calculate daily returns
    daily_returns = close_df.pct_change().dropna()

    # Save daily returns
    daily_path = os.path.join(paths["clean"], "etf_daily_returns.csv")
    daily_returns.to_csv(daily_path)

    # Monthly returns using compounded formula
    monthly_returns = daily_returns.resample("ME").apply(lambda x: (1 + x).prod() - 1)

    # Save monthly data
    monthly_path = os.path.join(paths["clean"], "etf_monthly_returns.csv")
    monthly_returns.to_csv(monthly_path)

    print("✔ Data cleaned successfully.")

    return close_df, daily_returns, monthly_returns
