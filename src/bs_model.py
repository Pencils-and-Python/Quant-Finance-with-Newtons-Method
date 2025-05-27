"""
src/bs_model.py

Black-Scholes pricing and vega (Greek) implementation for European call options.
"""

import numpy as np
from scipy.stats import norm

def bs_call_price(S, K, T, r, sigma):
    """
    Compute the Black-Scholes price of a European call option.

    Parameters:
        S (float): Spot price of the underlying asset
        K (float): Strike price
        T (float): Time to maturity (in years)
        r (float): Risk-free interest rate
        sigma (float): Volatility of the underlying asset

    Returns:
        float: Call option price
    """
    if sigma <= 0 or T <= 0:
        return max(0.0, S - K * np.exp(-r * T))  # Edge case for zero vol or zero time

    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return call_price


def bs_vega(S, K, T, r, sigma):
    """
    Compute the vega of a European call option (sensitivity to volatility).

    Parameters:
        S (float): Spot price
        K (float): Strike price
        T (float): Time to maturity (in years)
        r (float): Risk-free interest rate
        sigma (float): Volatility

    Returns:
        float: Vega (∂Price/∂Sigma)
    """
    if sigma <= 0 or T <= 0:
        return 0.0  # No sensitivity if option is at expiry or no movement

    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    vega = S * norm.pdf(d1) * np.sqrt(T)
    return vega
