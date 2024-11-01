import argparse
import matplotlib.pyplot as plt
import numpy as np

# Assuming GBMSimulator is defined elsewhere as per your earlier code
from pygbm.gbm_simulator import GBMSimulator

def simulate(y0, mu, sigma, T, N, output):
    # Initialize the GBM simulator with the parameters
    simulator = GBMSimulator(mu=mu, sigma=sigma, y_0=y0)

    # Simulate the GBM path
    t_values, y_values = simulator.simulate_path(T, N)

    # Create a plot
    plt.plot(t_values, y_values, label="GBM Path")
    plt.xlabel("Time")
    plt.ylabel("Y(t)")
    plt.title("Simulated Geometric Brownian Motion Path")
    plt.legend()

    # Save the plot to the specified output file
    plt.savefig(output)
    plt.show()  # Close the plot to free up memory

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Simulate a Geometric Brownian Motion and output a plot.")
    subparsers = parser.add_subparsers(dest="command")

    simulate_parser = subparsers.add_parser("simulate", help="Simulate a Geometric Brownian Motion and output a plot.")
    simulate_parser.add_argument('--y0', type=float, required=True, help='Initial value (y0) at time t=0')
    simulate_parser.add_argument('--mu', type=float, required=True, help='Drift coefficient (mu)')
    simulate_parser.add_argument('--sigma', type=float, required=True, help='Diffusion coefficient (sigma)')
    simulate_parser.add_argument('--T', type=float, required=True, help='Total time (T)')
    simulate_parser.add_argument('--N', type=int, required=True, help='Number of steps (N)')
    simulate_parser.add_argument('--output', type=str, required=True, help='Output file name for the plot')

    # Parse the arguments
    args = parser.parse_args()

    # Call the simulation function with the parsed arguments
    simulate(args.y0, args.mu, args.sigma, args.T, args.N, args.output)

if __name__ == '__main__':
    main()