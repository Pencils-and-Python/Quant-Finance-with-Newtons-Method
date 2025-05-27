# 🧠 Estimating Implied Volatility Using Newton’s Method

<!--
Keywords: implied volatility, newton’s method, black-scholes, quant finance, numerical methods, python, scipy, root finding, volatility modeling, financial engineering, computational finance
-->

This project demonstrates how to use **Newton’s Method** to solve a **nonlinear root-finding problem** in a quantitative finance context. Specifically, it estimates the **implied volatility** of a European call option using the **Black-Scholes pricing model**.

Built in **Python**, this modular implementation uses **SciPy**, **NumPy**, and Streamlit to showcase both analytical depth and interactive tooling. This project is part of my transition from civil engineering to quantitative modeling, with a focus on **numerical optimization**, **financial modeling**, and **computational problem solving**.

---

## 📌 Problem Statement

Implied volatility (IV) is not directly observable in the market—it must be inferred from the market price of options. This estimation leads to a root-finding problem, which we solve using Newton’s Method.

---

## 🛠️ Technical Approach

- Define the objective function \( f(\sigma) = BS(\sigma) - P_{\text{market}} \)
- Implement Newton’s Method to solve \( f(\sigma) = 0 \)
- Use Python to structure the logic and visualize convergence
- Package the solution in a clean, professional report using **Quarto**

---

## 📂 Project Structure

quant_fin_newton_method/
├── env.yml
├── README.md
├── .gitignore
├── .quarto/                         # Optional Quarto site/project config
│
├── data/                            # Input files (OK to push public)
│   └── example_option_data.csv
│
├── figs/                            # Output plots (OK to commit)
│   └── convergence_plot.png
│
├── notebooks/                       # Jupyter scratchwork (public but informal)
│   └── bs_iv_exploration.ipynb
│
├── reports/                         # Source Quarto reports (write/edit here)
│   └── implied_volatility_report.qmd
│
├── docs/                            # 🔥 GitHub Pages Output Folder (public-facing)
│   └── implied_volatility_report.html
│
├── src/                             # Core logic, modularized
│   ├── __init__.py
│   ├── bs_model.py
│   ├── iv_solver.py
│   └── config.py
│
├── utils/                           # Supporting tools
│   ├── plotting.py
│   └── logger.py
│
└── planning/                        # Public blog outlines & drafts (safe to commit)
    ├── outline.md
    ├── overview.md
    └── project_plan.md

---
## Render the quatro report

quarto render reports/implied_volatility_report.qmd --output-dir docs/

---

## 🔑 Featured Skills & Concepts

- Numerical root-finding with Newton’s Method
- Black-Scholes option pricing model
- Implied volatility estimation
- Python scientific computing with SciPy/NumPy
- Modular code architecture for finance tools
- Streamlit UI for interactive financial modeling
- Multi-page technical documentation using Quarto

---

## 📦 Deliverables

- ✅ Python implementation of Newton’s Method
- ✅ Modular codebase (`src/`) for pricing and solving
- ✅ Professional report in Quarto (`.qmd`)
- ✅ Optional Streamlit app (in future)
- ✅ Medium blog post + LinkedIn showcase (in progress)

---

## 🔖 License

This project is public and educational. All code is free to use and modify with attribution.

--- 

> 📚 *This project is part of my transition into quantitative finance, using Python and numerical analysis to explore core concepts in a hands-on way.*
