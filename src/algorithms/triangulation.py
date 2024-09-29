from basics.point import Point
from basics.polygon import Polygon
from basics.line import Line

class Triangle:
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.vertices = [p1, p2, p3]
    
    def __repr__(self):
        return f"Triangle({self.vertices[0]}, {self.vertices[1]}, {self.vertices[2]})"

def is_clockwise(p1: Point, p2: Point, p3: Point) -> bool:
    """Check if three points form a clockwise turn."""
    return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x) < 0

def is_counterclockwise(p1: Point, p2: Point, p3: Point) -> bool:
    """Check if three points form a counterclockwise turn."""
    return not is_clockwise(p1, p2, p3)

def is_point_in_triangle(p: Point, t: Triangle) -> bool:
    """Check if a point p is inside the triangle t."""
    p1, p2, p3 = t.vertices
    area = abs((p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)) / 2
    area1 = abs((p.x - p1.x) * (p2.y - p1.y) - (p.y - p1.y) * (p2.x - p1.x)) / 2
    area2 = abs((p.x - p2.x) * (p3.y - p2.y) - (p.y - p2.y) * (p3.x - p2.x)) / 2
    area3 = abs((p.x - p3.x) * (p1.y - p3.y) - (p.y - p3.y) * (p1.x - p3.x)) / 2
    return area == area1 + area2 + area3

def is_ear(polygon: Polygon, i: int) -> bool:
    """Check if the vertex at index i forms an ear in the polygon."""
    prev_index = (i - 1) % polygon.n
    next_index = (i + 1) % polygon.n
    
    p1 = polygon.vertices[prev_index]
    p2 = polygon.vertices[i]
    p3 = polygon.vertices[next_index]
    
    # Form the potential ear triangle
    ear = Triangle(p1, p2, p3)
    
    # Check if the triangle is counterclockwise
    if is_clockwise(p1, p2, p3):
        return False
    
    # Ensure no other vertex is inside this triangle
    for v in polygon.vertices:
        if v not in ear.vertices and is_point_in_triangle(v, ear):
            return False
    
    return True

def triangulate_polygon(polygon: Polygon) -> list[Triangle]:
    """Triangulate the polygon into a list of triangles."""
    vertices = polygon.vertices[:]
    triangles = []

    # Continue until only 3 vertices are left (one triangle)
    while len(vertices) > 3:
        ear_found = False

        # Iterate over all vertices to find an ear
        for i in range(len(vertices)):
            if is_ear(Polygon(vertices), i):
                prev_index = (i - 1) % len(vertices)
                next_index = (i + 1) % len(vertices)

                # Create the ear triangle
                ear_triangle = Triangle(vertices[prev_index], vertices[i], vertices[next_index])
                triangles.append(ear_triangle)

                # Remove the ear vertex from the polygon
                del vertices[i]
                ear_found = True
                break

        if not ear_found:
            raise ValueError("No ear found. Polygon may be malformed or not simple.")

    # The final remaining triangle
    triangles.append(Triangle(vertices[0], vertices[1], vertices[2]))

    return triangles

if __name__ == "__main__":
    # Example of a simple concave polygon
    p1 = Point(0, 0)
    p2 = Point(2, 0)
    p3 = Point(3, 1)
    p4 = Point(2, 2)
    p5 = Point(0, 2)
    p6 = Point(1, 1)  # This point makes the polygon concave
    
    concave_polygon = Polygon([p1, p2, p3, p4, p5, p6])

    try:
        triangles = triangulate_polygon(concave_polygon)
        print("Triangles formed from triangulation:")
        for triangle in triangles:
            print(triangle)
    except ValueError as e:
        print(e)