

import math

class Circle:
    def __init__(self,radius=1):
        self.radius= radius

    def getPerimeter(self):
        return 2* self.radius *math.pi

    def getArea(self):
        return self.radius * self.radius * math.pi
    
    def setRadius(self,radius):
        self.radius=radius



c1 = Circle()          # Creates a circle with default radius 1

print(c1.getArea())

c2=Circle(20)
print(c2.getPerimeter())


c1.setRadius(5)
print(c1.r)