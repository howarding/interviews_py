import random

class ShapeFactory:
    factories = {}
    @staticmethod
    def addFactory(id, shapeFactory):
        ShapeFactory.factories[id] = shapeFactory

    @staticmethod
    def createShape(id):
        if id not in ShapeFactory.factories:
            ShapeFactory.factories[id] = eval(id + '.Factory()')
        return ShapeFactory.factories[id].create()

class Shape(object):
    pass

class Circle(Shape):
    def draw(self):
        print 'Circle.draw'
    def erase(self):
        print 'Circle.erase'

    class Factory:
        def create(self): return Circle()


class Square(Shape):
    def draw(self):
        print 'Square.draw'
    def erase(self):
        print 'Square.erase'

    class Factory:
        def create(self): return Square()


def shapeNameGen(n):
    return (random.choice(Shape.__subclasses__()).__name__ for i in range(n))

n = 7
shapes = [ShapeFactory.createShape(id) for id in shapeNameGen(n)]
for shape in shapes:
    shape.draw()
    shape.erase()