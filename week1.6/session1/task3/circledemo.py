# Week 1.6, Session 1: Task 3
from shapes import Shape
from shapes import Circle
from point import Point
p = Point(0.0,0.0)
c = Circle(2.5,p,"red")

print(c)
print(f"{c.perimeter():.3f}")
print(f"{c.area():.3f}")
p.set_x(1.6)
p.set_y(3.2)
c.set_position(p)
print(c)
c.set_colour("green")
print(c)
# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)
