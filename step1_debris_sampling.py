# step1_debris_sampling.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set styling for plots
sns.set(style="whitegrid", font_scale=1.2)

# Fix random seed for reproducibility
np.random.seed(42)

# Number of samples
NUM_SAMPLES = 100

# Sample uncertain parameters
mass_samples = np.random.uniform(10, 150, NUM_SAMPLES)  # in kg
omega_samples = np.random.normal(0.5, 0.22, NUM_SAMPLES)  # in rad/s
conductivity_samples = np.random.uniform(0.1, 1.5, NUM_SAMPLES)  # in S/m

# Combine into a DataFrame
df = pd.DataFrame({
    'Mass (kg)': mass_samples,
    'Angular Velocity (rad/s)': omega_samples,
    'Conductivity (S/m)': conductivity_samples
})

# Save first 10 rows as CSV for use in table later
df.head(10).to_csv("sampled_debris_parameters.csv", index=False)

# Create and save histogram plots
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

sns.histplot(mass_samples, kde=True, ax=axes[0], color='skyblue', edgecolor='black')
axes[0].set_title('Sampled Debris Mass Distribution')
axes[0].set_xlabel('Mass (kg)')

sns.histplot(omega_samples, kde=True, ax=axes[1], color='lightgreen', edgecolor='black')
axes[1].set_title('Sampled Angular Velocity Distribution')
axes[1].set_xlabel('Angular Velocity (rad/s)')

sns.histplot(conductivity_samples, kde=True, ax=axes[2], color='salmon', edgecolor='black')
axes[2].set_title('Sampled Conductivity Distribution')
axes[2].set_xlabel('Conductivity (S/m)')

plt.tight_layout()
plt.savefig("sampled_distributions.png", dpi=300)
plt.show()

print("✅ Generated CSV and saved 'sampled_distributions.png' + 'sampled_debris_parameters.csv'")
