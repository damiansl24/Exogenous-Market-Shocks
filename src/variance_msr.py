import pandas as pd

def covariance(mkt_data: pd.Series, time_window: int) -> pd.Series: 
    '''
    Calculating the covariance of two indices, given a certain time window.

    Parameters:
    market_data: a dataframe containing market information from the yfinance
    library for both markets / indices being measured.
    time_window: the time window for covariance measure (will be optimized). The
    window will be used to find the price means, and pct change will come from
    that. To be clear, this is a rolling window.

    Returns:
    A series of covariance over time. 
    '''

    # Measuring covariance only between two indices.
    tickers = mkt_data.columns.values.tolist()
    if len(tickers) != 2:
        return "Error: Provide only 2 indices for comparison"
    
    covariance: None | list = []
    # Computing the rolling time window for covariance. 
    for i in range(mkt_data.shape[0]):
        if i < time_window:
            covariance.append(None)
            continue
        
        window = mkt_data.iloc[i - time_window: i]
        means = window.mean()
        t1 = tickers[0]
        t2 = tickers[1]
        
        # covariance computation
        cov = ((window[t1] - means[t1]) * (window[t2] - means[t2])).sum() / (time_window - 1)
        covariance.append(cov)
    
    return pd.Series(covariance, index = mkt_data.index)

def variance(mkt: pd.DataFrame, tick: str) -> float:
    '''
    this is a helper function for the following beta function.
    given price data for the market, which in the beta function
    will automatically be shortened to within the specified time
    window, return the variance of the market.

    the dataframe should include a calculated typical price column.

    Parameters:
    mkt: a dataframe of price data for the market, shortened to
    specified time frame in the beta function.

    Returns:
    a float value for variance
    '''
    # var = (sum(real - mean) ** 2) / N
    mean: float = mkt["typ",tick].mean() # establishing mean

    var = ((mkt["typ", tick] - mean) ** 2).sum() / (mkt.shape[0] - 1)

    return var
