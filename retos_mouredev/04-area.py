class IPolygon:
    def area():
        pass
    def printArea():
        pass

class Triangle(IPolygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) / 2

    def printArea(self):
        print("El área del triángulo es", self.area())

class Rectangle(IPolygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def printArea(self):
        print("El área del rectángulo es", self.area())

class Square(IPolygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def printArea(self):
        print("El área del cuadrado es", self.area())

def area(polygon:IPolygon):
    polygon.printArea()
    
area(Triangle(10, 5))
area(Rectangle(5, 7))
area(Square(4))
