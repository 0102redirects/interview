#!/usr/bin/env python
# coding=utf-8
def predicate_false(exception, detail='', data=None):
    def inner(predicate, *args, **kwargs):
        if (yield predicate(*args, **kwargs)):
            raise exception(detail=detail, data=data)
    return inner


class myExpection(object):

    def __init__(self, detail, data):
        print detail
        print data
        print "zl--------exe"


def test_is_true(prams_a,params_b):
    print "p_a", prams_a
    return True


def aaa():
    expec = myExpection(1, 2)
    print "begin___________________"
    fun = predicate_false(expec)(test_is_true,"pa","pb")
    fun.next()
    yield fun

    print "end___________________"


if __name__ == "__main__":
    a = aaa()
    a.next()
    # a.next()
    print "over"
