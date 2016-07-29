# Python comprehension problems
# Problem 0.8.1
def increments(L): return [x+1 for x in L]

# Problem 0.8.2
def cubes(L): return [x**3.0 for x in L]

# Problem 0.8.3
def tuple_sum(A, B): return [(x1+x2, y1+y2) for ((x1, y1), (x2, y2)) in zip(A, B)]

# Problem 0.8.4
def inv_dict(d): return {v:k for k,v in d.items()}

# Problem 0.8.5
def row(p, n): return [p+i for i in range(n)]
comprehension = [row(i, 20) for i in range(1, 16)]
comprehension = [[i+j for j in range(20)] for i in range(1, 16)]

# Function inverse
# Problem 0.8.6
Solution: Yes, this function is invertible, because it is both onto and one-to-one.
One possible change:
U         V
1 ------> A
      ^
2 ----|   B
3 ------> C
4 ------> D

# Problem 0.8.7
No, it is not invertible.
U         V   
1 ------> A
2 ------> B   
3 ------> C
4 ------> D

# Functional composition
# Problem 0.8.8 
domain: (-∞, 0]; co-domain: [0, +∞)
domain: [0, +∞); co-domain: [0, +∞)

domain: [0, +∞); co-domain: [0, +∞)

# Problem 0.8.9
Yes.

# Probablity
# Problem 0.8.10
Pr(get an even number) = 0.5 + 0.1*2 = 0.7
Pr(get an odd number) = 0.3

# Problem 0.8.11
Pr(getting 1) = Pr(1, 4, 7) = 0.2 + 0.1 + 0.1 = 0.4
Pr(getting 2) = Pr(2, 5) = 0.2 + 0.1 = 0.3
Pr(getting 0) = 0.3

