import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

def generate_random_points(num_points=10, seed=None):
    """Generates a set of random points in 2D space."""
    if seed:
        np.random.seed(seed)
    return np.random.rand(num_points, 2)

def compute_voronoi(points):
    """Computes the Voronoi diagram from a set of points."""
    return Voronoi(points)

def plot_voronoi(vor):
    """Plots the Voronoi diagram."""
    voronoi_plot_2d(vor)
    plt.title("Voronoi Diagram")
    plt.show()

def main(num_points=10, seed=None):
    """Main function to generate, compute, and plot Voronoi diagram."""
    points = generate_random_points(num_points, seed)
    vor = compute_voronoi(points)
    plot_voronoi(vor)

if __name__ == "__main__":
    main()