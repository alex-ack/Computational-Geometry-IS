from basics.point import Point
from basics.line import Line
from typing import Union

def line_intersection(line1: Line, line2: Line) -> Union[tuple[float, float], None]:
    """
    Determine the intersection point of two lines, if it exists.
    Returns a tuple with the intersection point coordinates, or None if the lines are parallel.
    """
    x1, y1 = line1.point1.x, line1.point1.y
    x2, y2 = line1.point2.x, line1.point2.y
    x3, y3 = line2.point1.x, line2.point1.y
    x4, y4 = line2.point2.x, line2.point2.y

    # Calculate the denominator
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

    # If denominator is zero, lines are parallel
    if den == 0:
        return None

    # Calculate the intersection point
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
    x = x1 + t * (x2 - x1)
    y = y1 + t * (y2 - y1)

    return (x, y)

def do_lines_intersect(line1: Line, line2: Line) -> bool:
    """
    Determine if two line segments intersect using the CCW method.
    """
    def ccw(A: Point, B: Point, C: Point) -> bool:
        return (C.y - A.y) * (B.x - A.x) > (B.y - A.y) * (C.x - A.x)

    A, B = line1.point1, line1.point2
    C, D = line2.point1, line2.point2

    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)

def line_segment_intersection(line1: Line, line2: Line) -> Union[Point, None]:
    """
    Determine the intersection point of two line segments, if it exists.
    Returns the intersection point, or None if the segments don't intersect.
    Handles edge cases for degenerate segments.
    """
    # Precompute bounding boxes to reduce unnecessary calculations.
    if not (min(line1.point1.x, line1.point2.x) <= max(line2.point1.x, line2.point2.x) and
            min(line1.point1.y, line1.point2.y) <= max(line2.point1.y, line2.point2.y)):
        return None

    intersection = line_intersection(line1, line2)
    if intersection is None:
        return None

    # Check if the intersection point is within both segments
    def is_on_segment(point: Point, line: Line) -> bool:
        return (min(line.point1.x, line.point2.x) <= point.x <= max(line.point1.x, line.point2.x) and
                min(line.point1.y, line.point2.y) <= point.y <= max(line.point1.y, line.point2.y))

    if is_on_segment(Point(intersection[0], intersection[1]), line1) and        is_on_segment(Point(intersection[0], intersection[1]), line2):
        return Point(intersection[0], intersection[1])

    return None

# Error Handling for Edge Cases
def handle_degenerate_cases(line: Line) -> bool:
    """
    Handle cases where the line segment is degenerate (i.e., a point or zero length).
    """
    return line.point1 == line.point2

def line_intersection_with_handling(line1: Line, line2: Line) -> Union[Point, None]:
    """
    Wrapper that includes error handling for degenerate line segments (i.e., points).
    """
    if handle_degenerate_cases(line1) or handle_degenerate_cases(line2):
        print("One of the line segments is degenerate (a point).")
        return None

    return line_segment_intersection(line1, line2)