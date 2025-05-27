# 🧠 Estimating Implied Volatility Using Newton’s Method

<!--
Keywords: implied volatility, newton’s method, black-scholes, quant finance, numerical methods, python, scipy, root finding, volatility modeling, financial engineering, computational finance
-->

This project explores the use of **Newton’s Method**, a classic root-finding algorithm, to estimate **implied volatility** from observed market prices using the **Black-Scholes** model.

The work bridges **numerical methods**, **financial modeling**, and **Python implementation**, and is part of my broader transition from civil engineering into quantitative finance.

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
