# step5_sensitivity_analysis.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load your data
df = pd.read_csv("sampled_debris_parameters.csv")

# Compute mean values
mean_mass = df['Mass (kg)'].mean()
mean_omega = df['Angular Velocity (rad/s)'].mean()
mean_conductivity = df['Conductivity (S/m)'].mean()

# Define the loss function
def compute_loss(u, mass, omega, conductivity):
    capture_risk = (omega**2) * (1 - u) * 100
    mass_penalty = (mass / 100) * (1 - u)
    misalignment = np.abs(0.8 - conductivity) * 10
    return capture_risk + mass_penalty + misalignment

# Fixed control input (use optimized_u if you like)
u = 0.8

# Vary each parameter
mass_range = np.linspace(10, 150, 100)
omega_range = np.linspace(0, 1.2, 100)
conductivity_range = np.linspace(0.1, 1.5, 100)

# Compute losses
loss_vs_mass = [compute_loss(u, m, mean_omega, mean_conductivity) for m in mass_range]
loss_vs_omega = [compute_loss(u, mean_mass, o, mean_conductivity) for o in omega_range]
loss_vs_conductivity = [compute_loss(u, mean_mass, mean_omega, c) for c in conductivity_range]

# Plot sensitivity analysis
plt.figure(figsize=(10, 6))
plt.plot(mass_range, loss_vs_mass, label='Mass (kg)', color='blue')
plt.plot(omega_range, loss_vs_omega, label='Angular Velocity (rad/s)', color='green')
plt.plot(conductivity_range, loss_vs_conductivity, label='Conductivity (S/m)', color='red')
plt.xlabel('Parameter Value')
plt.ylabel('Loss')
plt.title('Sensitivity Analysis of Loss Function')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("sensitivity_analysis.png", dpi=300)
plt.show()

print("✅ Sensitivity analysis plot saved as 'sensitivity_analysis.png'")
