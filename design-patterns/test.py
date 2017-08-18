import os, sys

class Student(object):
    def __init__(self, name, score):
        '''
        :param str name:
        :param int score::
        '''
        self.__name = name
        self.__score = score

    def print_score(self):
        print("%s: %d" % (self.__name, self.__score))

    def get_grade(self):
        if self.__score>= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

def run_twice(animal):
    '''
    :param Animal animal:
    :return:
    '''
    animal.run()
    animal.run()


class Timer(object):
    def run(self):
        print('Start...')


if __name__ == "__main__":
    bart = Student('bart', 59)
    print bart
    bart.print_score()
    print bart.get_grade()
    print bart.get_name()
    # bart.set_score(-32)
    dog = Dog()
    cat = Cat()
    dog.run()
    cat.run()
    print isinstance(cat, Animal)
    run_twice(Animal())
    run_twice(Dog())
    run_twice(Cat())
    run_twice(Tortoise())
    run_twice(Timer())
    print type(dog)
    print dir(dog)