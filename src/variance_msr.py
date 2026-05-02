import pandas as pd
import src.Exceptions

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
        raise src.Exceptions.MustHaveTwoIndices("Covariance must only measure two indices")

    prices = mkt_data.pct_change().dropna()
    
    covariance: None | list = []
    # Computing the rolling time window for covariance. 
    for i in range(prices.shape[0]): # pct_change drops first row.
        if i < time_window:
            covariance.append(None)
            continue
        
        window = prices.iloc[i - time_window: i]
        means = window.mean()
        t1 = tickers[0]
        t2 = tickers[1]
        
        # covariance computation
        cov = ((window[t1] - means[t1]) * (window[t2] - means[t2])).sum() / (time_window - 1)
        covariance.append(float(cov))
    
    return pd.Series(covariance, index = prices.index, name = "Covariance").dropna()

def variance(mkt: pd.DataFrame, window: int) -> pd.Series | pd.DataFrame:
    '''
    Calculates variance of an index according to a rolling time window. 

    Parameters:
    mkt: a dataframe of price data for the market

    Returns:
    A series or dataframe, showing log-normalized variance over time
    '''
    if isinstance(mkt, pd.Series):
        df = mkt.to_frame()
    else:
        df = mkt

    tickers = df.columns.values.tolist()
    prices = df.pct_change().dropna()

    variance: pd.DataFrame = pd.DataFrame(index = prices.index, columns = tickers)
    
    for t in tickers:
        var_list_t: list = []
        for i in range(prices.shape[0]):
            if i < window:
                var_list_t.append(None)
                continue
        
            period = prices[t].iloc[i - window: i]
            mean_t = period.mean()

            var = float(((period - mean_t) ** 2).sum()) / (window - 1)

            var_list_t.append(var)


        variance.isetitem(tickers.index(t), var_list_t)
    
    return variance.dropna()

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
