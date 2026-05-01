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

    prices = mkt_data.pct_change().dropna()
    
    covariance: None | list = []
    # Computing the rolling time window for covariance. 
    for i in range(mkt_data.shape[0]):
        if i < time_window:
            covariance.append(None)
            continue
        
        window = prices.iloc[i - time_window: i]
        means = window.mean()
        t1 = tickers[0]
        t2 = tickers[1]
        
        # covariance computation
        cov = ((window[t1] - means[t1]) * (window[t2] - means[t2])).sum() / (time_window - 1)
        covariance.append(cov)
    
    return pd.Series(covariance, index = mkt_data.index)

def variance(mkt: pd.DataFrame, window: int) -> pd.Series | pd.DataFrame:
    '''
    Calculates variance of an index according to a rolling time window. 

    Parameters:
    mkt: a dataframe of price data for the market

    Returns:
    A series or dataframe, showing log-normalized variance over time
    '''
    tickers = mkt.columns.values.tolist()

    variance: pd.DataFrame = pd.DataFrame(index = mkt.index, columns = tickers)

    prices = mkt.pct_change().dropna()
    
    for t in tickers:
        var_list_t: list = []
        for i in range(mkt.shape[0]):
            if i < window:
                var_list_t.append(None)
                continue
        
            period = prices[i - window: i]
            mean_t = period.mean()

            var = ((period - mean_t) ** 2).sum() / (window - 1)

            var_list_t.append(var)

        variance.isetitem(tickers.index(t), var_list_t)
    
    return variance

def variance_log(mkt: pd.DataFrame, window: int) -> pd.Series | pd.Dataframe:
    '''
    Calculates the variance of an index over time with a rolling time window,
    calculated using log returns to normalize real price data. 

    Parameters: 
    mkt: a dataframe of price data for the market.

    Returns: 
    a series or dataframe, showing log-normalized variance over time.
    '''

    return NotImplementedError 
