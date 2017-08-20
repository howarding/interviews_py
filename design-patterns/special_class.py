class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    def __repr__(self):
        return self.__str__()
    # __repr__ = __str__

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda : 25
        # raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

    def __call__(self):
        print 'My name is %s.' % self.name



class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def next(self):     # for Python 2.7
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__



s = Student('Michael')
print s
print s.score
print s.age()
print s()

link = Chain('http://wanlab.poly.edu')
print link.status.user.timeline.list


# f = Fib()
# for a in f:
#     print a
# print f[0]
# print type([3:5])
# print f[3:20]