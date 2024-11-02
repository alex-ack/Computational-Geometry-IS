class Triangle:
    def __init__(self, p1, p2, p3):
        """Initialize triangle with three points as tuples (x,y)"""
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    
    def get_barycentric_coordinates(self, point):
        """
        Calculate barycentric coordinates (λ1, λ2, λ3) for given point
        Returns tuple of three weights that sum to 1
        """
        x, y = point
        x1, y1 = self.p1
        x2, y2 = self.p2
        x3, y3 = self.p3
        
        # Calculate denominator for barycentric formula
        denominator = ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3))
        
        # Calculate first weight (λ1)
        lambda1 = ((y2 - y3)*(x - x3) + (x3 - x2)*(y - y3)) / denominator
        
        # Calculate second weight (λ2)
        lambda2 = ((y3 - y1)*(x - x3) + (x1 - x3)*(y - y3)) / denominator
        
        # Calculate third weight (λ3)
        lambda3 = 1 - lambda1 - lambda2
        
        return (lambda1, lambda2, lambda3)
    
    def contains_point(self, point):
        """
        Check if point lies inside triangle using barycentric coordinates
        Returns True if point is inside or on the triangle, False otherwise
        """
        lambda1, lambda2, lambda3 = self.get_barycentric_coordinates(point)
        
        # Point is inside or on triangle if all weights are between 0 and 1
        return (0 <= lambda1 <= 1) and (0 <= lambda2 <= 1) and (0 <= lambda3 <= 1)
    
    def get_circumcenter(self):
        """
        Calculate the circumcenter of the triangle
        Returns tuple (x, y) of circumcenter coordinates
        """
        x1, y1 = self.p1
        x2, y2 = self.p2
        x3, y3 = self.p3
        
        # Calculate perpendicular bisector components
        D = 2 * (x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))
        
        # Calculate circumcenter coordinates
        Ux = ((x1*x1 + y1*y1)*(y2 - y3) + (x2*x2 + y2*y2)*(y3 - y1) + (x3*x3 + y3*y3)*(y1 - y2)) / D
        Uy = ((x1*x1 + y1*y1)*(x3 - x2) + (x2*x2 + y2*y2)*(x1 - x3) + (x3*x3 + y3*y3)*(x2 - x1)) / D
        
        return (Ux, Uy)