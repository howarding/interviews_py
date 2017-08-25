# v1.0 (8/25/2017)

class Calculator:
    def __init__(self, token_list):
        '''
        :param list token_list:
        '''
        self.stack = []
        self.tokens = []
        for string in token_list:
            if string not in Factory.dict:
                self.tokens.append(Operand(string))
            else:
                self.tokens.append(Factory.dict[string]())

    def run(self):
        for token in self.tokens:
            token.process(self.stack)
        return self.stack.pop()



class Token:
    pass


class Operand(Token):
    def __init__(self, val):
        self.val = int(val)

    def process(self, tokens):
        tokens.append(self.val)


class Operator(Token):
    pass

class Add(Operator):
    def process(self, stack):
        b, a = stack.pop(), stack.pop()
        stack.append(a + b)

class Subtract(Operator):
    def process(self, stack):
        b, a = stack.pop(), stack.pop()
        stack.append(a - b)

class Multiply(Operator):
    def process(self, stack):
        b, a = stack.pop(), stack.pop()
        stack.append(a * b)

class Divide(Operator):
    def process(self, stack):
        b, a = stack.pop(), stack.pop()
        stack.append(a / b)


class Factory:
    dict = {
        '+': Add,
        '-': Subtract,
        '*': Multiply,
        '/': Divide
    }


# input = "1 2 + 4 * 4 2 - +"
# input = "1 4 + 3 7 + * 5 /"
# input = "10 2 +"
input = "10 2 /"
token_list = input.split()
cal = Calculator(token_list)
print cal.run()