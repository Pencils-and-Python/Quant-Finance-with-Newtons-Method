import streamlit as st
from src.iv_solver import implied_vol_newton

st.set_page_config(page_title="Implied Volatility Estimator", layout="centered")

st.title("📈 Implied Volatility Estimator")
st.markdown(
    "Estimate implied volatility using Newton’s Method and the Black-Scholes model. "
    "This tool solves for the volatility that aligns the theoretical price with the market price."
)

with st.form("iv_form"):
    S = st.number_input("Spot Price (S)", value=100.0, step=1.0)
    K = st.number_input("Strike Price (K)", value=105.0, step=1.0)
    T = st.number_input("Time to Maturity (T, in years)", value=1.0, step=0.1)
    r = st.number_input("Risk-Free Rate (r)", value=0.05, step=0.01)
    C_market = st.number_input("Market Price of Call Option", value=9.5, step=0.1)
    initial_guess = st.slider("Initial Volatility Guess", 0.01, 1.0, 0.2, step=0.01)
    submitted = st.form_submit_button("Estimate IV")

if submitted:
    try:
        iv = implied_vol_newton(C_market, S, K, T, r, initial_guess)
        st.success(f"Estimated Implied Volatility: **{iv:.4f}**")
    except Exception as e:
        st.error(f"Error: {e}")
