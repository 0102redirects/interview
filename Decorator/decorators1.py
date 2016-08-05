#!/usr/bin/env python
# coding=utf-8


import functools

"""
通过一个<带参数>装饰器修改一个函数的返回值！
"""


def decorate(func):  # func是被装饰的函数！
    @functools.wraps(func)  # wrapper.__name__ = func.__name__ 
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        val = func()
        print 'value before changing :  %s' % val
        val["a"] = 1
        print 'value after change :  %s ' % val
        return val
    return wrapper


@decorate
def test():
    return {'a': 0}
test()
print test.__name__


# print decorate(test)(111)

