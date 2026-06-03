import pandas as pd
import src.variance_msr
import src.Exceptions

def beta(market_data: pd.DataFrame, time_window: int, ticker: str) -> pd.Series:
    '''
    given price data for the market and a specific asset, return
    a list of beta over time. 

    Parameters:
    market_data: dataframe from yfinance of market index, and asset index
    ticker: a string, denoting which ticker is supposed to be the market.

    Returns:
    Series of beta measures over time.
    '''
    # beta = cov(Ri, Rm) / var(Rm)

    try:
        cov = src.variance_msr.covariance(market_data, time_window)
    except src.Exceptions.MustHaveTwoIndices:
        print("not a valid dataframe for covariance and volatility measure!")
        return None

    var = src.variance_msr.variance(market_data, time_window)
    
    beta_series = pd.Series(cov / var[ticker], index = cov.index, name = "beta")

    return beta_series

def volatility(market_data: pd.DataFrame, time_window: int) -> pd.Series | pd.DataFrame:
    '''
    Calculates rolling volatility of an asset or index. This is simply the standard 
    deviation calculation.

    Parameters:
    market_data: dataframe containing typical price data for some asset or index

    Returns:
    Series or Dataframe with volatility of the asset.
    '''
    stdev: None | list[None | float] = []

    # need to calculate the rolling mean as well as rolling standard deviation: 
    # Find the baseline mean then use LIFO to adjust it. 
    # First n rows, standard deviation is measured by change 
    
    return NotImplementedError
