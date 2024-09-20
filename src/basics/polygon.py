from basics.point import Point
from basics.line import Line

class Polygon:
    def __init__(self, vertices: list[Point]):
        """A polygon is defined by a list of vertices (points)."""
        if len(vertices) < 3:
            raise ValueError("A polygon must have at least 3 vertices.")
        self.vertices = vertices

    def perimeter(self):
        """Calculate the perimeter of the polygon."""
        perimeter = 0
        for i in range(len(self.vertices)):
            j = (i + 1) % len(self.vertices)  # Wrap around for the last vertex
            perimeter += Line(self.vertices[i], self.vertices[j]).length()
        return perimeter

    def area(self):
        """Calculate the area of the polygon using the Shoelace theorem."""
        n = len(self.vertices)
        area = 0
        for i in range(n):
            j = (i + 1) % n
            area += self.vertices[i].x * self.vertices[j].y
            area -= self.vertices[j].x * self.vertices[i].y
        return abs(area) / 2

    def __repr__(self):
        return f"Polygon({', '.join([str(v) for v in self.vertices])})"