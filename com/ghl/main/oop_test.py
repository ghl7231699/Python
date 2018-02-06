# -*- coding: UTF-8 -*-
# python面向对象
class Employee:
    """所有员工的基类"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print 'Total Employee %d' % self.empCount

    def displayEmployee(self):
        print 'Name:', self.name, 'Salary:', self.salary

    def displaySelf(self):
        print self
        print self.__class__

    def prt(self):
        print 'hello Python!!'


e1 = Employee('LiLi', 10000.0)
e2 = Employee('LeLe', 19000.0)
e1.age = 28
# https://stackoverflow.com/questions/31063384/when-i-assign-a-list-to-variable-why-pycharm-give-me-a-prompt-that-is-this-list
employees = list([])
employees.append(e1)
employees.append(e2)
for e in employees:
    e.displayEmployee()
    e.displaySelf()
    e.displayCount()
    b = hasattr(e, 'age')
    if b:
        print '年龄为', getattr(e, 'age')
    else:
        print '没有含有age这个属性'
    e.prt()
print 'Total Employee %d\n' % Employee.empCount
print 'Employee.__doc__:', Employee.__doc__
print 'Employee.__name__:', Employee.__name__
print 'Employee.__module__:', Employee.__module__
print 'Employee.__bases__:', Employee.__bases__
print 'Employee.__dict__:', Employee.__dict__


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        classname = self.__class__.__name__
        print classname, '销毁'


p1 = Point()
p2 = p1
p3 = p1
# 打印对象的id
print id(p1), id(p2), id(p3)
del p1
del p2
del p3
