from basics.point import Point

class Line:
    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2

    def length(self):
        """Calculate the length of the line segment."""
        return self.point1.distance_to(self.point2)

    def slope(self):
        """Calculate the slope of the line segment."""
        if self.point1.x == self.point2.x:
            return float('inf')  # Vertical line has an undefined slope
        return (self.point2.y - self.point1.y) / (self.point2.x - self.point1.x)

    def __repr__(self):
        return f"Line({self.point1}, {self.point2})"