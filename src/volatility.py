import pandas as pd
import variance

def beta(market_data: pd.DataFrame, time_window) -> pd.Series:
    '''
    given price data for the market and a specific asset, return
    a list of beta over time. For normalization purposes, the first ticker
    is the market ticker, and the second is the asset.

    Parameters:
    market_data: dataframe from yfinance of market index, and asset index

    Returns:
    Series of beta measures over time.
    '''
    # beta = cov(Ri, Rm) / var(Rm)
    tickers: list = market_data.columns.get_level_values(1).unique().tolist()

    beta: list = []
    for i in range(market_data.shape[0]):
        if i < time_window:
            beta.append(None)
            continue

        window = market_data.iloc[i - time_window: i]
        var: float = variance(window, tickers[0])

        means = window.mean()
        ind1_p = window["typ", tickers[0]].mean()
        ind2_p = window["typ", tickers[1]].mean()

        cov = ((window["typ", tickers[0]] - ind1_p) * (window["typ", tickers[1]] - ind2_p)).sum() / (time_window - 1)

        beta.append(cov / var)

    return pd.Series(beta, index = market_data.index)

def volatility(market_data: pd.DataFrame, time_window) -> pd.Series | pd.DataFrame:
    '''
    Calculates rolling volatility of an asset or index.

    Parameters:
    market_data: dataframe containing typical price data for some asset or index

    Returns:
    Series or Dataframe with volatility of the asset.
    '''
    return NotImplementedError
