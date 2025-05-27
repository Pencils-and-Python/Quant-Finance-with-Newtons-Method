# 🧠 Estimating Implied Volatility Using Newton’s Method

## 📌 Problem Statement

In options trading, **implied volatility (IV)** reflects the market’s expectations of an asset’s future volatility. It is not directly observable and must be *inferred* from market prices using models like Black-Scholes. This leads to a classic **root-finding problem**: given a market price, find the volatility that makes the Black-Scholes model return that price.

This project explores how **Newton’s Method**—a foundational numerical technique—is used to solve this problem in quantitative finance.

---

## 🛠️ High-Level Outline

1. **Background & Intuition**
   - Brief explanation of the Black-Scholes model
   - Definition and significance of implied volatility
   - Real-world use cases in finance and trading

2. **Mathematical Formulation**
   - Define the objective function:  
     \( f(\sigma) = BS(\sigma) - P_{\text{market}} \)
   - Goal: Solve for \( \sigma \) such that \( f(\sigma) = 0 \)

3. **Newton’s Method**
   - Update rule:  
     \( \sigma_{n+1} = \sigma_n - \frac{f(\sigma_n)}{f'(\sigma_n)} \)
   - Discuss convergence behavior and edge cases

4. **Python Implementation**
   - Step-by-step script using NumPy/SciPy
   - Manual and library-based solutions
   - Visualization of convergence and error

5. **Interpretation of Results**
   - Understanding the meaning of the estimated IV
   - Discussion on practical reliability

6. **Limitations & Next Steps**
   - Scenarios where Newton’s Method may fail
   - Other root-finding approaches (e.g., Brent’s, Secant)
   - Future extensions (e.g., implied volatility surfaces)

---

## 📦 Anticipated Deliverables

| Deliverable | Description |
|------------|-------------|
| **Python Script / Notebook** | Clean, well-commented code for IV estimation using Newton’s Method |
| **Streamlit App (Optional)** | Interactive front end to input option parameters and visualize iterations |
| **Quantro Report** | Professional write-up summarizing the mathematical approach, code, and insights |
| **Medium Blog Post** | Educational post covering the project for public audiences |
| **LinkedIn Summary Post** | Short showcase post highlighting results and skills gained |

---

> 🚧 This project is part of my ongoing transition into quantitative finance from a background in civil engineering. It serves as a practical application of numerical methods in financial modeling.
