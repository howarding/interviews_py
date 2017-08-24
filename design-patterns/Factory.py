import random

# 1. A simple static factory method.
class Shape(object):
    @staticmethod
    def factory(type):
        '''
        :param str type
        :return:
        '''
        if type == 'Circle':
            return Circle()
        if type == 'Square':
            return Square()
        assert 0, 'Bad shape creation: ' + type


class Circle(Shape):
    def draw(self):
        print 'Circle.draw'
    def erase(self):
        print 'Circle.erase'


class Square(Shape):
    def draw(self):
        print 'Square.draw'
    def erase(self):
        print 'Square.erase'


def shapeNameGen(n):
    return (
        random.choice(Shape.__subclasses__()).__name__
        for i in range(n)
    )

# n = 7
# shapes = [Shape.factory(type) for type in shapeNameGen(n)]
# for shape in shapes:
#     shape.draw()
#     shape.erase()




# 2. Preventing direct creation
# Not recommended
class Shape1(object):
    types = []

def factory(type):
    '''
    :param str type:
    :return:
    '''
    class Circle(Shape1):
        def draw(self):
            print 'Circle.draw'

        def erase(self):
            print 'Circle.erase'

    class Square(Shape1):
        def draw(self):
            print 'Square.draw'

        def erase(self):
            print 'Square.erase'

    if type == 'Circle':
        return Circle()
    if type == 'Square':
        return Square()
    assert 0, 'Bad shape creation: ' + type

def shapeNameGen1(n):
    return (
        factory(random.choice(['Circle', 'Square']))
        for i in range(n)
    )

# n = 7
# for shape in shapeNameGen1(n):
#     shape.draw()
#     shape.erase()
