import numpy as np
import matplotlib.pyplot as plt

# Class for representing a Line (y = mx + b)
class Line:
    def __init__(self, m, b):
        self.m = m  # slope
        self.b = b  # intercept
    
    def evaluate(self, x):
        """Returns y-value for a given x using y = mx + b."""
        return self.m * x + self.b

# Function to generate random lines with random slopes and intercepts
def generate_random_lines(num_lines=5):
    slopes = np.random.uniform(-2, 2, num_lines)
    intercepts = np.random.uniform(-10, 10, num_lines)
    return [Line(m, b) for m, b in zip(slopes, intercepts)]

# Function to plot the lines on a graph
def plot_arrangement(lines, points=None):
    """Plots all the generated lines on the same graph and optional points."""
    x_values = np.linspace(-10, 10, 400)
    
    # Plotting each line
    for line in lines:
        y_values = line.evaluate(x_values)
        plt.plot(x_values, y_values, label=f'y = {line.m:.2f}x + {line.b:.2f}')
    
    # Optionally plot points if provided
    if points:
        plt.scatter([p.x for p in points], [p.y for p in points], color='red', zorder=5)
    
    plt.xlim([-10, 10])
    plt.ylim([-10, 10])
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.title('Arrangement of Lines')
    plt.legend()
    plt.grid(True)
    plt.show()

# Class for representing Points and converting them to their dual Line
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def dual(self):
        """Returns the dual of a point, which is a Line."""
        return Line(self.x, self.y)

# Function to generate random points
def generate_random_points(num_points=5):
    x_coords = np.random.uniform(-10, 10, num_points)
    y_coords = np.random.uniform(-10, 10, num_points)
    return [Point(x, y) for x, y in zip(x_coords, y_coords)]

# Function to plot the dual of points as lines
def plot_duality(points):
    lines = [point.dual() for point in points]
    plot_arrangement(lines, points)