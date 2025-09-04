# step4_compare_strategies.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load sample data
df = pd.read_csv("sampled_debris_parameters.csv")

# Load optimal u from file
with open("optimal_control.txt", "r") as f:
    lines = f.readlines()
    optimized_u = float(lines[0].split(":")[1].strip())

# Define loss function
def compute_loss(u, mass, omega, conductivity):
    capture_risk = (omega**2) * (1 - u) * 100
    mass_penalty = (mass / 100) * (1 - u)
    misalignment = np.abs(0.8 - conductivity) * 10
    return capture_risk + mass_penalty + misalignment

# Compute losses for both strategies
fixed_u = 0.8
loss_fixed = []
loss_optimized = []

for _, row in df.iterrows():
    loss_fixed.append(compute_loss(fixed_u, row['Mass (kg)'], row['Angular Velocity (rad/s)'], row['Conductivity (S/m)']))
    loss_optimized.append(compute_loss(optimized_u, row['Mass (kg)'], row['Angular Velocity (rad/s)'], row['Conductivity (S/m)']))

# Prepare dataframe for plotting
plot_df = pd.DataFrame({
    'Loss': loss_fixed + loss_optimized,
    'Strategy': ['Fixed (u = 0.8)'] * len(loss_fixed) + [f'Optimized (u = {optimized_u:.2f})'] * len(loss_optimized)
})

# Create boxplot
sns.set(style="whitegrid", font_scale=1.2)
plt.figure(figsize=(8, 5))
sns.boxplot(data=plot_df, x="Strategy", y="Loss", palette=["gray", "purple"])
plt.title("Loss Comparison: Fixed vs Optimized Control")
plt.ylabel("Loss")
plt.xlabel("Control Strategy")
plt.tight_layout()
plt.savefig("loss_comparison_boxplot.png", dpi=300)
plt.show()

print("✅ Comparison plot saved as 'loss_comparison_boxplot.png'")
