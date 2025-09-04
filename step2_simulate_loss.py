# step2_simulate_loss.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the sample data from Step 1
df = pd.read_csv("sampled_debris_parameters.csv")

# Assume a fixed control input (e.g., harpoon force)
u = 0.8  # Can range from 0 to 1

# Define a mock loss function L(u, ξ)
def compute_loss(u, mass, omega, conductivity):
    capture_risk = (omega**2) * (1 - u) * 100
    mass_penalty = (mass / 100) * (1 - u)
    misalignment = np.abs(0.8 - conductivity) * 10  # penalize mismatch with optimal conductivity
    return capture_risk + mass_penalty + misalignment

# Compute loss for each debris sample
losses = []
for i, row in df.iterrows():
    loss = compute_loss(u, row['Mass (kg)'], row['Angular Velocity (rad/s)'], row['Conductivity (S/m)'])
    losses.append(loss)

df['Loss'] = losses

# Save as new CSV
df.to_csv("loss_results_fixed_u.csv", index=False)

# Plot the loss distribution
plt.figure(figsize=(8, 5))
sns.histplot(losses, bins=15, kde=True, color='purple', edgecolor='black')
plt.title(f'Loss Distribution with Fixed Control Input (u = {u})')
plt.xlabel('Loss')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig("loss_distribution_fixed_u.png", dpi=300)
plt.show()

print("✅ Losses computed and saved as 'loss_results_fixed_u.csv' + 'loss_distribution_fixed_u.png'")
