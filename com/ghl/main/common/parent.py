# -*- coding: UTF-8 -*-
class parent:  # 定义父类
    parentAttr = 100

    def __init__(self):
        print '调用父类构造函数'

    def parentMethod(self):
        print '调用父类方法'

    def setAttr(self, attr):
        parent.parentAttr = attr

    def getAttr(self):
        print '父类属性', parent.parentAttr


class child(parent):
    _child_attr = 10  # 两个下划线开头则表示为类私有属性

    def __init__(self):
        print '调用子类构造方法'

    def childMethod(self):
        print '调用子类的方法'


c = child()
c.childMethod()
c.parentMethod()
c.setAttr(20)
c.getAttr()
