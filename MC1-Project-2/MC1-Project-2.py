"""MC1-Project-2: Optimize a portfolio."""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo
import datetime as dt
from util import get_data, plot_data

def normalize_data(df):
    """Normalize stock prices using the first row of the dataframe"""
    return df / df.ix[0,:]

def compute_daily_returns(df):
    """Compute and return the daily return values."""
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:] / df[:-1].values) - 1
    return daily_returns[1:]

def compute_portfolio_stats(prices, allocs=[0.1, 0.2, 0.3, 0.4], rfr = 0.0, sf=252.0):
    normed = prices / prices.ix[0]
    alloced = normed * allocs
    port_vals = alloced.sum(axis = 1)
    daily_rets = compute_daily_returns(port_vals)
    cr = port_vals[-1] / port_vals[0] - 1
    adr = daily_rets.mean()
    sddr = daily_rets.std()
    sr = (daily_rets - rfr).mean() / (daily_rets).std() * np.sqrt(sf)

    return port_vals, cr, adr, sddr, sr

# This is the function that will be tested by the autograder
# The student must update this code to properly implement the functionality
def optimize_portfolio(sd=dt.datetime(2008,1,1), ed=dt.datetime(2009,1,1), \
        syms=['GOOG','AAPL','GLD','XOM'], gen_plot=False):

        # Read in adjusted closing prices for given symbols, date range
        dates = pd.date_range(sd, ed)
        prices_all = get_data(syms, dates)  # automatically adds SPY
        prices = prices_all[syms]  # only portfolio symbols
        prices_SPY = prices_all['SPY']  # only SPY, for comparison later

        # find the allocations for the optimal portfolio
        # note that the values here ARE NOT meant to be correct for a test case
        num_stocks = len(syms)
        allocations = [1.0 / num_stocks] * num_stocks # initially evenly split
        bounds = [(0.0, 1.0)] * num_stocks
        constraints = {'type': 'eq', 'fun': lambda allocations: 1.0 - np.sum(allocations)}

        def negitive_sharpe_ratio(allocations):
            return -compute_portfolio_stats(prices, allocations)[4]

        minimum_allocations = spo.minimize(negitive_sharpe_ratio, allocations, method='SLSQP', options={'disp': True},
            constraints=constraints, bounds=bounds).x

        # cr, adr, sddr, sr = [0.25, 0.001, 0.0005, 2.1] # add code here to compute stats
        print "Getting stats"
        port_val, cr, adr, sddr, sr = compute_portfolio_stats(prices, minimum_allocations)
        print "Done Getting stats"

        # Compare daily portfolio value with SPY using a normalized plot
        if gen_plot:
            # add code to plot here
            df_temp = pd.concat([port_val / port_val.ix[0,:], prices_SPY / prices_SPY.ix[0,:]], keys=['Portfolio', 'SPY'], axis=1)
            plot_data(df_temp)
            pass

        return minimum_allocations, cr, adr, sddr, sr



def test_code():
    # This function WILL NOT be called by the auto grader
    # Do not assume that any variables defined here are available to your function/code
    # It is only here to help you set up and test your code

    # Define input parameters
    # Note that ALL of these values will be set to different values by
    # the autograder!

    start_date = dt.datetime(2010,1,1)
    end_date = dt.datetime(2010,12,31)
    symbols = ['GOOG', 'AAPL', 'GLD', 'XOM']

    # Assess the portfolio
    allocations, cr, adr, sddr, sr = optimize_portfolio(sd = start_date, ed = end_date,\
        syms = symbols, \
        gen_plot = True)

    # Print statistics
    print "Start Date:", start_date
    print "End Date:", end_date
    print "Symbols:", symbols
    print "Allocations:", allocations
    print "Sharpe Ratio:", sr
    print "Volatility (stdev of daily returns):", sddr
    print "Average Daily Return:", adr
    print "Cumulative Return:", cr

if __name__ == "__main__":
    # This code WILL NOT be called by the auto grader
    # Do not assume that it will be called
    test_code()
