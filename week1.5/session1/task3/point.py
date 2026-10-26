# Week 1.5, Session 1: Task 3
import math
class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, x_coordinate, y_coordinate):
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x_coordinate
        self.y = y_coordinate
    
    # Add distance() method here
    def distance(self):
        """
        Returns distance from this Point to origin.
        """
        return math.hypot(self.x, self.y)
    # Add distance_to() method here 
    def distance_to(self, point2):
        """
        Calculates distance between this point and another point

        parameters:
        self and another point object

        returns: 
        distance (int)
        """
        distx = point2.x - self.x
        disty = point2.y - self.y
        return math.hypot(distx,disty)
    # (This will need a parameter representing another point)



# Finally, add code here to demonstrate use of Point
p1 = Point(3,-4)
p2 = Point(2.0,9.5)
print(p1.distance_to(p2))