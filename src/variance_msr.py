import pandas as pd
import src.Exceptions

def covariance(mkt_data: pd.Series, time_window: int) -> pd.Series: 
    '''
    Calculates the rolling covariance of two indices, within a certain time 
    window. The function is input agnostic (can process typical price, log 
    returns, and simple returns). 

    Parameters:
    market_data: a dataframe containing market information from the yfinance
    library for both markets / indices being measured.
    time_window: the rolling time window for covariance measure (will be optimized).

    Returns:
    A series of covariance over time. 
    '''

    # Measuring covariance only between two indices.
    tickers = mkt_data.columns.values.tolist()
    if len(tickers) != 2:
        raise src.Exceptions.MustHaveTwoIndices("Covariance must only measure two indices")
    
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
    
    return pd.DataFrame(covariance, index = prices.index, name = "Covariance").dropna()

def variance(mkt: pd.DataFrame, window: int) -> pd.Series | pd.DataFrame:
    '''
    Calculates rolling variance of an index according to a rolling time window. 

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

    variance: pd.DataFrame = pd.DataFrame(index = mkt.index, columns = tickers)
    
    for t in tickers:
        var_list_t: list = []
        for i in range(mkt.shape[0]):
            if i < window:
                var_list_t.append(None)
                continue
        
            period = mkt[t].iloc[i - window: i]
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
