# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math


# Copy Point class definition here
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

# Add a definition for a Circle class here, giving it
class Circle:
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
    def __init__(self,radius,centre):
        """
        creates a circle, given radius and centre
        """
        self.r = radius
        self.c = centre
    def area(self):
        return(math.pi * self.r * self.r)
    def perimeter(self):
        return(math.pi*self.r*2)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle

# Don't add any testing code to this file!
