import yfinance as yf
import pandas as pd
import numpy as np
import src.Exceptions

def typical_price(price: pd.Series) -> list:
    '''
    Calculates typical price of an index on a certain day. 

    Parameters: 
    price: A DataFrame object with ticker price data

    Returns: 
    Series of typical prices for the tickers.
    '''
    
    tickers: list(str) = price.index.get_level_values(1).unique().tolist()
    
    typ_prices: list(float) = []

    for t in tickers:
        tp = (price["Close", t] + price["High", t] + price["Low", t]) / 3
        typ_prices.append(tp)

    return typ_prices

def load_stock_data(ticker: list[str], start_date:str, end_date:str) -> pd.DataFrame:
    """
    Load stock data for a given ticker and date range.

    Parameters:
    ticker (str): The stock ticker symbol (e.g., 'AAPL').
    start_date (str): The start date in 'YYYY-MM-DD' format.
    end_date (str): The end date in 'YYYY-MM-DD' format.

    Returns:
    pd.Series: a series, containing typical price of the stock over time.
    Only returns pd.DataFrame when loading price data for multiple indices 
    at once.
    """

    stock_data = yf.download(ticker, start=start_date, end=end_date)

    if stock_data.isna().any().any():
        raise src.Exceptions.InvalidDataNaN("This dataset is incomplete. There
                                            are NaN values in this dataset."
    if (stock_data <= 0).any().any():
        raise src.Exceptions.InvalidDataZN("This dataset has errors. There are
                                            Zero and Negative values.")
    
    tickers: list = stock_data.columns.get_level_values(1).unique().tolist()

    for t in tickers:
        stock_data["typ", t] = stock_data.apply(lambda row: typical_price(row)[tickers.index(t)], axis = 1)

    return stock_data["typ"]


def log_returns(mkt_data: pd.DataFrame) -> pd.DataFrame:
    '''
    Calculates log returns for a market dataframe to normalize changes. 

    Parameters:
    mkt_data: a dataframe containing typical price for a ticker, with 
    information from the yfinance library. 

    Returns:
    A dataframe indexed by date and containing daily log returns
    '''

    columns: list[str] = mkt_data.columns.values.tolist()

    mkt_ret: pd.DataFrame = pd.DataFrame(data=[None] * mkt_data.shape[0], 
                                         index = mkt_data.index, 
                                         columns = columns)
    
    for i in range(1, mkt_data.shape[0]):
        for column in columns:
            ticker: pd.DataFrame = mkt_data[column]
            tick_ret = float(np.log(ticker.iloc[i]/ticker.iloc[i-1]))
            mkt_ret.iloc[i, mkt_ret.columns.get_loc(column)] = tick_ret

    return mkt_ret

def returns(mkt_data: pd.DataFrame) -> pd.DataFrame:
    '''
    Calculates returns for a market dataframe. 
    Simple returns only.

    Parameters: 
    mkt_data: a dataframe containing typical price for a ticker, with 
    information from the yfinance library. 

    Returns:
    a dataframe indexed by date and containing simple daily returns.
    '''
    columns: list[str] = mkt_data.columns.values.tolist()

    mkt_ret: pd.DataFrame = pd.DataFrame(data=[None] * mkt_data.shape[0], 
                                         index = mkt_data.index, 
                                         columns = columns)
    
    for i in range(1, mkt_data.shape[0]):
        for column in columns:
            ticker: pd.DataFrame = mkt_data[column]
            
            # the function is exactly the same, but different calculation. 
            tick_ret = (ticker.iloc[i] - ticker.iloc[i - 1]) / ticker.iloc[i - 1]
            mkt_ret.iloc[i, mkt_ret.columns.get_loc(column)] = tick_ret

    return mkt_ret

