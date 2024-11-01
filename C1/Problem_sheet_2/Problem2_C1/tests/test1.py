from pygbm.gbm_simulator import GBMSimulator
import matplotlib.pyplot as plt

# Parameters for GBM
y0 = 1.0
mu = 0.05
sigma = 0.2
T = 1.0
N = 100

# Initialize simulator
simulator = GBMSimulator(sigma , mu , y0 )
# Simulate path
t_values , y_values = simulator.simulate_path (T, N)
# Plot the simulated path
plt.plot( t_values , y_values , label ="GBM Path ")
plt.xlabel(" Time ")
plt.ylabel("Y(t)")
plt.title(" Simulated Geometric Brownian Motion Path ")
plt.legend()
plt.show()