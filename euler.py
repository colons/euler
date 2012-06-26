#!/usr/bin/env python2

from answers import answers
from sys import argv


print answers

def test_all():
    pass

def test_one(problem):
    pass

try:
    problem = int(argv[-1])
except ValueError:
    task = test_all
else:
    test_one(problem)
