from .point import Point

class Line:
    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2
        self.vector = (point2.x - point1.x, point2.y - point1.y)

    def length(self):
        """Calculate the length of the line segment."""
        return self.point1.distance_to(self.point2)

    def slope(self):
        """Calculate the slope of the line segment."""
        if self.vector[0] == 0:
            return None  # Vertical line has an undefined slope
        return self.vector[1] / self.vector[0]

    def __repr__(self):
        return f"Line({self.point1}, {self.point2})"
