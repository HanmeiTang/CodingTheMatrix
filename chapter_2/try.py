# Exercise 2.11.4
from vec import *
from triangular import triangular_solve_n

v1 = Vec({0, 1, 2, 3}, {0: 1, 1: 0.5, 2: -2, 3: 4})
v2 = Vec({0, 1, 2, 3}, {0: 0, 1: 3, 2: 3, 3: 2})
v3 = Vec({0, 1, 2, 3}, {0: 0, 1: 0, 2: 1, 3: 5})
v4 = Vec({0, 1, 2, 3}, {0: 0, 1: 0, 2: 0, 3: 2})

v_list = [v1, v2, v3, v4]

# triangular_solve_n(rowlist=v_list, b=[-8, 3, -4, 6])

print(v1 + v2)
