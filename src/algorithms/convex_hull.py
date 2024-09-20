from basics.point import Point

def polar_angle(p0, p1):
    """Returns the polar angle between p0 and p1."""
    return (p1.y - p0.y) / (p1.x - p0.x) if p1.x != p0.x else float('inf')

def distance(p0, p1):
    """Returns the squared distance between p0 and p1."""
    return (p1.x - p0.x) ** 2 + (p1.y - p0.y) ** 2

def graham_scan(points):
    """Computes the convex hull of a set of points using Graham's scan."""
    if len(points) < 3:
        return points  # Convex hull not possible for fewer than 3 points

    # Find the point with the lowest y-coordinate (if tie, lowest x-coordinate)
    start = min(points, key=lambda p: (p.y, p.x))

    # Sort points by polar angle with the start point
    sorted_points = sorted(points, key=lambda p: (polar_angle(start, p), distance(start, p)))

    # Initialize the convex hull with the first two points
    hull = [start, sorted_points[0]]

    for point in sorted_points[1:]:
        # Check if we turn clockwise or counterclockwise
        while len(hull) > 1 and cross_product(hull[-2], hull[-1], point) <= 0:
            hull.pop()  # Pop the last point if we turn clockwise
        hull.append(point)

    return hull

def cross_product(o, a, b):
    """Returns the cross product of vectors OA and OB (O = origin, A, B = points).
    A positive cross product means counterclockwise, negative means clockwise."""
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)