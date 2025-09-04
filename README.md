# Robust Optimization for Harpoon-Based Space Debris Removal 🚀🛰️

This project develops a **robust optimization framework** for harpoon-based active debris removal (ADR) systems operating under uncertainty.  
By modeling debris parameters as probabilistic distributions and applying **Monte Carlo simulation + Differential Evolution (DE)**, the project demonstrates how optimization can significantly reduce mission risk compared to fixed-control strategies.

---

## 📌 Project Overview
- **Goal:** Identify a robust control input for harpoon-based ADR that minimizes expected mission loss under uncertain debris properties.  
- **Key Debris Parameters:**  
  - Mass (10–150 kg)  
  - Spin rate (Normal distribution, mean = 0.5 rad/s)  
  - Conductivity (0.1–1.5 S/m)  
- **Mission Loss Function:** Combines capture failure risk, mass penalty, and misalignment.  
- **Approach:**  
  - Monte Carlo simulations to evaluate performance under uncertainty  
  - Differential Evolution (population-based optimizer) to minimize expected loss  
  - Sensitivity analysis to identify most influential parameters  

---

## 🛠️ Methods
1. **Probabilistic Modeling** – Debris mass, spin rate, and conductivity modeled as random variables.  
2. **Monte Carlo Simulation** – Sampled debris parameters to estimate mission performance.  
3. **Differential Evolution** – Used to find optimal control input with minimum expected loss.  
4. **Sensitivity Analysis** – Partial correlation coefficients (PCCs) measured parameter influence.  

---

## 📊 Results
- **Optimizer Performance:**  
  - Expected mission loss dropped rapidly from ~3.9 to ~3.0 within first 4 iterations.  
  - Converged efficiently with minimal additional iterations.  
- **Comparison to Fixed Strategy:**  
  - Fixed control input → median loss ≈ 8 (high variability & risk).  
  - Optimized input → median loss ≈ 3 (lower, more consistent outcomes).  
- **Sensitivity Analysis:**  
  - Spin rate (angular velocity) had the greatest effect on mission outcomes.  
  - Conductivity had moderate influence.  
  - Mass had minimal effect within tested range.  

---

## 🔍 Key Insights
- Robust optimization significantly improves reliability of ADR missions.  
- Accounting for debris **spin rate** is critical to mission success.  
- Monte Carlo + Differential Evolution provides an efficient framework for decision-making under uncertainty.  

---


---

## 🚀 How to Run
1. Clone the repo:  
   ```bash
   git clone https://github.com/Funmi-adeeye/harpoon-space-debris-optimizer.git
   cd harpoon-space-debris-optimizer

