# =====================================
# Predator-Prey Simulation (Dynamic + Save Figure)
# Lotka-Volterra Model
# =====================================

import numpy as np
import matplotlib
matplotlib.use("Agg")  # Headless backend for Raspberry Pi
import matplotlib.pyplot as plt

# -------------------------------------
# 1. Simulation parameters
# -------------------------------------
T = 50         # total time
dt = 0.01      # time step
time = np.arange(0, T, dt)

# Initial populations
prey = np.zeros_like(time)
predator = np.zeros_like(time)
prey[0] = 10
predator[0] = 5

# Predator-Prey parameters
a = 1.0   # prey growth rate
b = 0.1   # predation rate
c = 0.1   # predator death rate
d = 0.01  # predator growth per eaten prey

# -------------------------------------
# 2. Simulation loop
# -------------------------------------
for t in range(1, len(time)):
    prey[t] = prey[t-1] + (a*prey[t-1] - b*prey[t-1]*predator[t-1])*dt
    predator[t] = predator[t-1] + (d*prey[t-1]*predator[t-1] - c*predator[t-1])*dt
    # Ensure populations remain non-negative
    prey[t] = max(prey[t], 0)
    predator[t] = max(predator[t], 0)

# -------------------------------------
# 3. Plot and save figure
# -------------------------------------
plt.figure(figsize=(10,5))
plt.plot(time, prey, label="Prey", color="green")
plt.plot(time, predator, label="Predator", color="red")
plt.fill_between(time, prey, predator, color="yellow", alpha=0.1)  # optional dynamic area
plt.xlabel("Time")
plt.ylabel("Population")
plt.title("Predator-Prey Simulation (Dynamic)")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save figure instead of showing
plt.savefig("predator_prey_simulation.png", dpi=150)
print("✅ Figure saved as predator_prey_simulation.png")
