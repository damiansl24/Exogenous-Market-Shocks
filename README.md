# Exogenous-Market-Shocks

This is a working self-directed research project on Exogenous Shocks in the 
Market. This analysis uses rolling covariance between the S&P 500 and VIX to
identify periods where market behavior deviated from its normal relationship. 

The key finding is that covariance spikes align with known crisis periods 
(2008, 2020), but also reveal smaller disruptions in 2012, 2016, and late 2018
that warrant further economic investigation. 

Recently transitioning from colab to github.

# Working notes:
*Housekeeping*

Implement volatility

Implement log normalized variance

Implement "indicator timing"

*Data Exploration*

Calculate typical price and add to data frame immediately after downloading
Compare with GDP / CPI / FRED data. 

Some other tickers: Japan ^N225, India ^BSESN, UK ^FTSE, China 000001.SS or 
MCHI, futures. 

Implement Window Grid Search
