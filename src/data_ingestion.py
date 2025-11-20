import yfinance as yf
import pandas as pd

def download_etf_data(etfs, start_date, end_date):
    """
    Downloads historical price data for a list of ETFs.
    Returns a DataFrame with multi-level columns: [Ticker → OHLCV].
    """

    try:
        data = yf.download(
            etfs,
            start=start_date,
            end=end_date,
            group_by='ticker',
            auto_adjust=False,
            progress=False
        )
        print("✔ Data successfully downloaded.")
        return data

    except Exception as e:
        print("❌ Error downloading ETF data:", e)
        return pd.DataFrame()
 
