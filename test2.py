#!/usr/bin/env python
# coding=utf-8

d1 = {"a": "a", "b": "b1"}
print "d1 =  ", d1
d2 = {"b": "b2", "c": "c"}
print "d2 =  ", d2
d1.update(d2)
print "after d1.update(d2), d1 = ", d1
