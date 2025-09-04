# step3_optimize_control.py (Fixed)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import differential_evolution

# Load the sampled debris data
df = pd.read_csv("sampled_debris_parameters.csv")

# Define the loss function
def compute_loss(u, mass, omega, conductivity):
    capture_risk = (omega**2) * (1 - u) * 100
    mass_penalty = (mass / 100) * (1 - u)
    misalignment = np.abs(0.8 - conductivity) * 10
    return capture_risk + mass_penalty + misalignment

# Objective function over all samples
def objective(u_array):
    u = u_array[0]
    losses = [
        compute_loss(u, row['Mass (kg)'], row['Angular Velocity (rad/s)'], row['Conductivity (S/m)'])
        for _, row in df.iterrows()
    ]
    return np.mean(losses)

# Hook function to track convergence
convergence_log = []
def callback_fn(xk, convergence=None):
    loss = objective([xk[0]])
    convergence_log.append(loss)

# Run Differential Evolution
result = differential_evolution(
    objective,
    bounds=[(0.0, 1.0)],
    strategy='best1bin',
    seed=42,
    callback=callback_fn,
    disp=True
)

# Extract result
optimal_u = result.x[0]
min_loss = result.fun
print(f"\n✅ Optimal u = {optimal_u:.4f} with expected loss = {min_loss:.4f}")

# Save to file
with open("optimal_control.txt", "w") as f:
    f.write(f"Optimal u: {optimal_u:.6f}\nExpected Loss: {min_loss:.6f}")

# Plot convergence manually from callback log
plt.figure(figsize=(8, 5))
plt.plot(convergence_log, marker='o', linestyle='-', color='darkblue')
plt.xlabel('Iteration')
plt.ylabel('Expected Loss')
plt.title('Optimizer Convergence (Differential Evolution)')
plt.grid(True)
plt.tight_layout()
plt.savefig("optimizer_convergence.png", dpi=300)
plt.show()
