import os
import sys
# from types import MethodType


class Student(object):
    __slots__ = ('name', 'age')


def set_age(self, age):
    self.age = age


def set_score(self, score):
    self.score = score


class GradStudent(Student):
    pass


s = Student()
s.name = 'Michael'
print s.name
# try:
Student.set_score = set_score
# s.set_score(35)
# print s.score
# except AttributeError:
#     pass
g = GradStudent()
GradStudent.set_score = set_score
g.set_score(36)
print g.score