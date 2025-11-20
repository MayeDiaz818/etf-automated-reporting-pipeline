import pandas as pd
import numpy as np


def max_drawdown(series):
    """
    Computes maximum drawdown for a return series.
    Drawdown = (cumulative - peak) / peak
    """
    cumulative = (1 + series).cumprod()
    peak = cumulative.cummax()
    drawdown = (cumulative - peak) / peak
    return drawdown.min()


def calculate_kpis(close_df, daily_returns):
    """
    Computes all core KPIs:
    - cumulative returns
    - daily volatility
    - annualized volatility
    - maximum drawdown
    - rolling 30-day volatility
    - KPI summary table
    """

    # --------------------------------------------------------
    # 1. Cumulative Returns
    # --------------------------------------------------------
    cumulative_returns = (1 + daily_returns).cumprod() - 1

    # --------------------------------------------------------
    # 2. Volatility
    # --------------------------------------------------------
    daily_vol = daily_returns.std()
    annual_vol = daily_vol * np.sqrt(252)

    # --------------------------------------------------------
    # 3. Maximum Drawdown
    # --------------------------------------------------------
    drawdowns = daily_returns.apply(max_drawdown)

    # --------------------------------------------------------
    # 4. Rolling 30-Day Annualized Volatility
    # --------------------------------------------------------
    rolling_vol_30d = daily_returns.rolling(30).std() * np.sqrt(252)

    # --------------------------------------------------------
    # 5. YTD Return
    # --------------------------------------------------------
    current_year = pd.Timestamp.today().year
    ytd_mask = daily_returns.index >= f"{current_year}-01-01"

    ytd_returns = (1 + daily_returns[ytd_mask]).prod() - 1

    # --------------------------------------------------------
    # 6. Build KPI Summary DataFrame
    # --------------------------------------------------------
    kpi_summary = pd.DataFrame({
        "Annualized Volatility": annual_vol,
        "Maximum Drawdown": drawdowns,
        "YTD Return": ytd_returns
    })

    kpi_summary.index.name = "ETF"

    print("✔ KPIs calculated successfully.")
    
    return kpi_summary, cumulative_returns, rolling_vol_30d
