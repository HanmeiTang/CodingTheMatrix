# Lab: Python - modules and control structures - and inverse index

# Task 0.6.1: Import the math module using the command
import math
help(math)
math.pow(3, 0.5) # 1.7320508075688772
math.pow(3, 2)  # 9.0

math.sqrt(-1)
math.pow(-1, 0.5)
ValueError: math domain error
# To solve this

# Solution1
import numpy as np
np.sqrt(-1+0j) # 1j

# Solution2
import cmath
cmath.sqrt(-1) # 1j

math.cos(math.pi) # -1.0
math.log(math.e) # 1.0

# Task 0.6.2: The module random defines a procedure randint(a,b) that returns an integer chosen uniformly at random from among {a, a + 1,...,b}. Import this procedure using the command
# >>> from random import randint

# Try calling randint a few times. Then write a one-line procedure movie review(name) that takes as argument a string naming a movie, and returns a string review selected uniformly at random from among two or more alternatives (Suggestions: “See it!”, “A gem!”, “Ideological claptrap!”)
help(randint)
def review(name): return ["See it!", "A gem!", "Ideological claptrap!"][randint(0,2)]

# Task 0.6.3: In Tasks 0.5.30 and 0.5.31 of Lab 0.5, you wrote procedures dict2list(dct, keylist) and list2dict(L, keylist). Download the file dictutil.py from the resource page for Coding the Matrix. Edit the file, replacing each occurence of pass with the appropriate statement. Import this module, and test the procedures. We might have occasion to use this module in the future.

