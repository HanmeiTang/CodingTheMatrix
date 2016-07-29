# Python comprehension problems
# Problem 1.7.1
def my_filter(L, num): return [x for x in L if x % num != 0]

# Problem 1.7.2
def my_lists(L): return [[x for x in range(i)] for i in L]

# Problem 1.7.3
def my_function_composition(f, g): return {k:g[v] for (k,v) in f.items() if k in f and v in g}

# Problem 1.7.4
def mySum(L): return sum(L)

# Problem 1.7.5
def myProduct(L):
    product = 1
    for l in L:
        product *= l
    return product

# Problem 1.7.6
def myMin(L): return min(L)

# Problem 1.7.7
def myConcat(L):
    conc = ""
    for s in L:
        conc += s
    return conc

# Problem 1.7.8
def myUnion(L):
    union = set()
    for s in L:
        union.update(s)
    return union

