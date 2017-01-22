# Quiz 2.4.2
def translation(v): return [v[0] + 1, v[1] + 2]


translation([4, 4])  # [5, 6]
translation([-4, -4])  # [-3, -2]


# Quiz 2.4.4
def addn(X, Y): return [x + y for x, y in zip(X, Y)]


# Quiz 2.5.3
def scalar_vector_mult(alpha, v): return [i * alpha for i in v]


# Exercise 2.6.1
w = [3, 4]
translation_vector = [2, 3]

# Exercise 2.6.2
line = [[1 + 5 / i, 4 - 1 / i] for i in range(100)]


# Task 2.6.9
def segment(pt1, pt2):
    [x1, y1] = pt1
    [x2, y2] = pt2
    n = 100
    segs = [[((1 - a / n) * x1 + (a / n) * x2), ((1 - a / n) * y1 + (a / n) * y2)] for a in range(100)]
    return segs


plot(segment([3.5, 3], [0.5, 1]))

# Quiz 2.7.2 - 2.7.5
from image import *
from plotting import *


class Vec:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function
        pass


def setitem(v, d, val): v.f[d] = val


def getitem(v, d): return v.f[d] if d in v.f else 0


def scalar_mul(v, alpha):
    for d in v.f:
        val = getitem(v, d) * alpha
        setitem(v, d, val)
    return v


def add(u, v):
    uv = Vec(u.D, {d: u.f[d] + v.f[d] for d in u.f})
    return uv


def neg(v):
    return Vec(v.D, {d: -v.f[d] for d in v.f})


# Computational Problem 2.8.7
from itertools import combinations
import sys

sys.path.insert(0, "../chapter_1")
from GF2 import one


def get_solution(s, L):
    """
    Args:
        s (list): a vector over GF(2)
        L (list of list): collection of possible sub-vectors over GF(2)
    Returns:
        solution (list of list): combination solutions collection
    """
    result = [[]] * len(s)
    for i in range(len(s))[1:]:
        combs = combinations(L, i)
        result[i] = [comb for comb in combs if get_sum_for_multi(comb) == s]
    result = [r[0] for r in result if r != []][0]
    return result


def get_sum_for_multi(list_set):
    length = len(list_set[0])
    L_sum = [0] * length
    for pie in list_set:
        L_sum = [x + y for x, y in zip(L_sum, pie)]
    return L_sum


# This is a test:
x = get_solution([one, one, one], [[one, 0, one], [0, one, 0], [one, one, 0], [0, 0, 0]])
print(x)  # ([one, 0, one], [0, one, 0])

# Quiz 2.9.3
import numpy as np


def get_ave(L): return np.dot(L, [1 / len(L)] * len(L))


# Quiz 2.9.4
def list_dot(u, v): return sum([x * y for x, y in zip(u, v)])


# Question 2.9.18
# I donot know so far.

# Computational Problem 2.9.19
# Computing all solutions to a linear system over GF(2).
# I do not know how to get this.

# Question 2.9.20
# I do not know so far.

# Exercise 2.11.3
x1 = 17.8
x2 = 4.4
x3 = -1.2

# Exercise 2.11.4
from vecutil import zero_vec


def trianglular_solve_n(rowlist, b):
    D = rowlist[0].D
    n = len(D)
    assert D == set(range(n))
    x = zero_vec(D)
    for i in reversed(range(n)):
        x[i] = (b[i] - rowlist[i] * x) / rowlist[i][i]

    return x
