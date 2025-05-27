"""
src/iv_solver.py

Uses Newton's Method to estimate implied volatility given a market price.
"""

from src.bs_model import bs_call_price, bs_vega

def implied_vol_newton(C_market, S, K, T, r,
                       initial_guess=0.2, tol=1e-6, max_iter=100):
    """
    Estimate implied volatility using Newton-Raphson root-finding.

    Parameters:
        C_market (float): Observed market price of the call option
        S (float): Spot price of the underlying asset
        K (float): Strike price
        T (float): Time to maturity (in years)
        r (float): Risk-free rate
        initial_guess (float): Starting estimate for volatility
        tol (float): Convergence tolerance
        max_iter (int): Max number of iterations allowed

    Returns:
        float: Estimated implied volatility

    Raises:
        ValueError: If method fails to converge
    """
    sigma = initial_guess
    for i in range(max_iter):
        price = bs_call_price(S, K, T, r, sigma)
        vega = bs_vega(S, K, T, r, sigma)

        if vega == 0:
            raise ValueError("Zero vega — Newton's method fails.")

        diff = price - C_market
        if abs(diff) < tol:
            return sigma

        sigma -= diff / vega

    raise ValueError("Newton’s method did not converge within the max iterations.")
