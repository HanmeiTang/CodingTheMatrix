# Quiz 2.4.2
def translation(v): return [v[0]+1, v[1]+2]
translation([4,4])  # [5, 6]
translation([-4,-4])  # [-3, -2]

# Quiz 2.4.4
def addn(X, Y): return [x+y for x,y in zip(X,Y)]

# Quiz 2.5.3
def scalar_vector_mult(alpha, v): return [i*alpha for i in v]

# Exercise 2.6.1
w = [3, 4]
translation_vector = [2, 3]

# Exercise 2.6.2
line = [[1+5/i, 4-1/i] for i in range(100)]

# Task 2.6.9
def segment(pt1, pt2):
    [x1, y1] = pt1
    [x2, y2] = pt2
    n = 100
    segs = [[((1-a/n)*x1+(a/n)*x2), ((1-a/n)*y1+(a/n)*y2)] for a in range(100)]
    return segs
plot(segment([3.5,3], [0.5,1]))

# Quiz 2.7.2 - 2.7.5
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
    uv = Vec(u.D, {d:u.f[d]+v.f[d] for d in u.f})
    return uv

def neg(v):
    return Vec(v.D, {d:-v.f[d] for d in v.f})
