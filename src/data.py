import yfinance as yf
import pandas as pd

def typical_price(price: pd.Series) -> list:
    '''
    Calculates typical price of an index on a certain day. 

    Parameters: 
    price: A DataFrame object with ticker price data

    Returns: 
    Series of typical prices for the tickers.
    '''
    
    tickers: list = price.index.get_level_values(1).unique().tolist()
    
    typical_prices: list(float) = []

    for t in tickers:
        tp = (price["Close", t] + price["High", t] + price["Low", t]) / 3
        typical_prices.append(tp)

    return typical_prices

def load_stock_data(ticker: str, start_date:str, end_date:str) -> pd.DataFrame:
    """
    Load stock data for a given ticker and date range.

    Parameters:
    ticker (str): The stock ticker symbol (e.g., 'AAPL').
    start_date (str): The start date in 'YYYY-MM-DD' format.
    end_date (str): The end date in 'YYYY-MM-DD' format.

    Returns:
    pd.Series: a series, containing typical price of the stock over time.
    Only returns pd.DataFrame when loading price data for multiple indices at once.
    """
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    
    tickers: list = stock_data.columns.get_level_values(1).unique().tolist()

    for t in tickers:
        stock_data["typ", t] = stock_data.apply(lambda row: typical_price(row)[tickers.index(t)], axis = 1)

    return stock_data["typ"]
