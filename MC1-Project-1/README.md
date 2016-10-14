# TASK

The primary goal of this assignment is to introduce you to this form of portfolio analysis. You will use pandas for reading in data, calculating various statistics and plotting a comparison graph.


Create a function called assess_portfolio() that takes as input a description of a portfolio and computes important statistics about it.

## Inputs

- A date range to select the historical data to use (specified by a start and end date). You should consider performance from close of the start date to close of the end date.
- Symbols for equities (e.g., GOOG, AAPL, GLD, XOM). Note: You should support any symbol in the data directory.
- Allocations to the equities at the beginning of the simulation (e.g., 0.2, 0.3, 0.4, 0.1), should sum to 1.0.
- Total starting value of the portfolio (e.g. $1,000,000)

### Function Input Parameters

- sd: A datetime object that represents the start date
- ed: A datetime object that represents the end date
- syms: A list of symbols that make up the portfolio (note that your code should support any symbol in the data directory)
- allocs: A list of allocations to the stocks, must sum to 1.0
- sv: Start value of the portfolio
- rfr: The risk free return per sample period for the entire date range (a single number, not an array).
- sf: Sampling frequency per year
- gen_plot: If True, create a plot named plot.png

## Outputs

- Cumulative return
- Average period return (if sampling frequency == 252 then this is average daily return)
- Standard deviation of daily returns
- Sharpe ratio of the overall portfolio, given daily risk free rate (usually 0), and yearly sampling frequency (usually 252, the no. of trading days in a year)
- Ending value of the portfolio

### Function Output returns

- cr: Cumulative return
- adr: Average period return (if sf == 252 this is daily return)
- sddr: Standard deviation of daily return
- sr: Sharpe ratio
- ev: End value of portfolio

Suggestions
 
- Read in adjusted closing prices for the 4 equities.
- Normalize the prices according to the first day. The first row for each stock should have a value of 1.0 at this point.
- Multiply each column by the allocation to the corresponding equity.
- Multiply these normalized allocations by starting value of overall portfolio, to get position values.
- Sum each row (i.e. all position values for each day). That is your daily portfolio value.
- Compute statistics from the total portfolio value.
