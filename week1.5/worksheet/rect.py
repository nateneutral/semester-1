# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        if not (isinstance(width, int) and isinstance(height,int)):
            raise TypeError("input are not valid integers")
        if not (width > 0 and height >0):
            raise ValueError("inputs are not valid measurements")
        # raising appropriate exceptions if necessary (see README.md)
        self.width = width
        self.height = height
    

    # Implement methods is_square(), area() & perimeter() here
    def is_square(self):
        if self.width == self.height:
            return(True)
        return(False)
    def area(self):
        A = self.width * self.height
        return(A)
    def perimeter(self):
        P = (self.width * 2) + (self.height * 2)
        return(P)
        
    # (See README.md for details of what they should do)
R = Rectangle(5,5)
print(R.is_square())
print(R.area())
print(R.perimeter())