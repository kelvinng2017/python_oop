"""
12_34.py Design a Geometric category. This category mainly sets the color to Green In addition, a Circle category is designed. In this category, getRadius() can get half meridian, setRadius() can set half meridian,getDiameter() 
can getDiameter, GetPerimeter () makes perimeter,getArea() makes area, and getColor makes color
"""


class Geometric():
    def __init__(self):
        self.color = "Green"


class Circle(Geometric):
    def __init__(self, radius):
        super().__init__()
        self.PI = 3.141598
        self.radius = radius

    def getRadius(self):
        return self.radius

    def setRadius(self, radius):
        self.radius = radius

    def getDiamater(self):
        return self.radius * 2

    def getPerimeter(self):
        return self.radius * 2 * self.PI

    def getArea(self):
        return self.PI * (self.radius ** 2)

    def getColor(self):
        return color


A = Circle(5)
print("circle color", A.color)
print("circle radius", A.getRadius())
print("circle diameter", A.getDiamater())
print("circle perimeter", A.getPerimeter())
print("circle area", A.getArea())
A.setRadius(10)
print("circle diameter", A.getDiamater())
