from point import Point
from line import Line

class Polygon:
    def __init__(self, vertices: list[Point]):
        """A polygon is defined by a list of vertices (points)."""
        if len(vertices) < 3:
            raise ValueError("A polygon must have at least 3 vertices.")
        self.vertices = vertices
        self.n = len(vertices)
        self.sides = [Line(vertices[i], vertices[(i+1) % self.n]) for i in range(self.n)]

    def perimeter(self):
        """Calculate the perimeter of the polygon."""
        return sum(side.length() for side in self.sides)

    def area(self):
        """Calculate the area of the polygon using the Shoelace theorem."""
        area = 0
        for i in range(self.n):
            j = (i + 1) % self.n
            area += self.vertices[i].x * self.vertices[j].y
            area -= self.vertices[j].x * self.vertices[i].y
        return abs(area) / 2

    def orientation(self):
        """Determine the orientation of the polygon (clockwise or counterclockwise)."""
        area = 0
        for i in range(self.n):
            j = (i + 1) % self.n
            area += (self.vertices[j].x - self.vertices[i].x) * (self.vertices[j].y + self.vertices[i].y)
        
        if area > 0:
            return "Counterclockwise"
        elif area < 0:
            return "Clockwise"
        else:
            return "Collinear (degenerate polygon)"

    def contains_point(self, point: Point):
        """You can check if a point is inside the polygon using the ray casting algorithm"""
        inside = False
        for i in range(self.n):
            j = (i + 1) % self.n
            if ((self.vertices[i].y > point.y) != (self.vertices[j].y > point.y)) and \
               (point.x < (self.vertices[j].x - self.vertices[i].x) * (point.y - self.vertices[i].y) / 
               (self.vertices[j].y - self.vertices[i].y) + self.vertices[i].x):
                inside = not inside
        return inside

    def intersects_line(self, line: Line):
        """Check if a line intersects with the polygon."""
        for side in self.sides:
            if self._line_intersects(side, line):
                return True
        return False

    @staticmethod
    def _line_intersects(line1: Line, line2: Line):
        """Helper function to check if two lines intersect"""
        def ccw(A, B, C):
            return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)
        
        A, B = line1.point1, line1.point2
        C, D = line2.point1, line2.point2
        return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

    def __repr__(self):
        return f"Polygon({', '.join([str(v) for v in self.vertices])})"