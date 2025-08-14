
import math
import turtle

class Circle:

    def __init__(self, radius=None, diameter=None):
        if diameter is not None:
            self.diameter = diameter
            self.radius = diameter / 2
        elif radius is not None:
            self.radius = radius
            self.diameter = 2 * radius
        else:
            raise ValueError("Specify radius or diameter")

    def area(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return f'circle`s radius is {self.radius} and diameter is {self.diameter}'

    def __add__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        else:
            new_circle = Circle(self.radius + other.radius)
            return new_circle

    def __gt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        else:
            return self.radius > other.radius

    def __lt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        else:
            return self.radius < other.radius

    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        else:
            return self.radius == other.radius


c1 = Circle(radius=30)
c2 = Circle(diameter=100)
print(c1)
print(c1.area())
print(c1 < c2, c1 > c2, c1 == c2)
c3 = c1 + c2
print(c3)

circles = [c1, c3, c2]
circles.sort()

s = turtle.getscreen()
t = turtle.Turtle()
for circle in circles:
    t.circle(circle.radius)