class Operator(object):
    pass


class Add(Operator):
    def operate(self, x, y):
        return x + y


class Subtract(Operator):
    def operate(self, x, y):
        return x - y


class Factory:
    dict = {
        '+': Add,
        '-': Subtract
    }
    operators = {}
    @staticmethod
    def get(arg):
        if arg not in Factory.dict:
            raise ValueError('Invalid Operator.')
        if arg not in Factory.operators:
            Factory.operators[arg] = Factory.dict[arg]()
        return Factory.operators[arg]

a, b = 7, 3
op = '+'
operator = Factory.get(op)
print operator.operate(a, b)

op = '-'
operator = Factory.get(op)
print operator.operate(a, b)
