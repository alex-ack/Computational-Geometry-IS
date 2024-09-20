class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_to(self, other):
        """Calculate the Euclidean distance between two points."""
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        """Check equality of two points based on their coordinates."""
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        """Less-than comparison for sorting points."""
        return (self.x, self.y) < (other.x, other.y)