# Task 0.5.1: Use Python to find the number of minutes in a week.
iminutes_in_week = 7 * 24 * 60  # 10080

# Task 0.5.2: Use Python to find the remainder of 2304811 divided by 47 without using the modulo operator%. (Hint: Use//.)
reminder = 2304811 - (2304811 // 47) * 47 # 25

# Task 0.5.3: Enter a Boolean expression to test whether the sum of 673 and 909 is divisible by 3.
(673 % 3 == 0) is True # False
(909 % 3 == 0) is True # True

# Task 0.5.4: Assign the value -9 to x and 1/2 to y. Predict the value of the following expression, then enter it to check your prediction: 
# 2**(y+1/2) if x+10<0 else 2**(y-1/2)
x = -9; y = 1/2
2**(y+1/2) if x+10<0 else 2**(y-1/2) # 1.0

# Task 0.5.5: Write a comprehension over {1, 2, 3, 4, 5} whose value is the set consisting of the squares of the first five positive integers.
comprehension = {x**2 for x in {1,2,3,4,5}} # {1, 4, 9, 16, 25}

# Task 0.5.6: Write a comprehension over {0, 1, 2, 3, 4} whose value is the set consisting of the first five powers of two, starting with 20.
comprehension = {2**x for x in {0, 1,2,3,4}} # {1, 2, 4, 8, 16}

# Task 0.5.7: The value of the previous comprehension, {x*y for x in {1,2,3} for y in {2,3,4}} is a seven-element set. Replace {1,2,3} and {2,3,4} with two other three-element sets so that the value becomes a nine-element set.
double_comprehension = {x*y for x in {1,2,3} for y in {3,5,7}} # {3, 5, 6, 7, 9, 10, 14, 15, 21}

# Task 0.5.8: Replace {1,2,3} and {2,3,4} in the previous comprehension with two disjoint (i.e. non-overlapping) three-element sets so that the value becomes a five-element set.
double_comprehension = {x*y for x in {0,1,2} for y in {0,1,3}} # {0, 1, 2, 3, 6}

# Task 0.5.9: Assume that S and T are assigned sets. Without using the intersection operator &, write a comprehension over S whose value is the intersection of S and T. Hint: Use a membership test in a filter at the end of the comprehension. Try out your comprehension with S = {1,2,3,4} and T = {3,4,5,6}.
S = {1,2,3,4}; T = {3,4,5,6}
X = S & T
X = {x for x in S|T if (x in S) and (x in T)} # {3, 4}

# Task 0.5.10: Write an expression whose value is the average of the elements of the list [20, 10, 15, 75].
ave = sum ([20, 10, 15, 75]) / len([20, 10, 15, 75]) # 30.0

# Task 0.5.11: Write a double list comprehension over the lists ['A','B','C'] and [1,2,3] whose value is the list of all possible two-element lists [letter, number]. That is, the value is [['A', 1], ['A', 2], ['A', 3], ['B', 1], ['B', 2],['B', 3], ['C', 1], ['C', 2], ['C', 3]]
double_comprehension = [[x,y] for x in ['A', 'B', 'C'] for y in [1,2,3]]

# Task 0.5.12: Suppose LofL has been assigned a list whose elements are themselves lists of numbers. Write an expression that evaluates to the sum of all the numbers in all the lists. The expression has the form sum([sum(... and includes one comprehension. Test your expression after assigning [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]] to LofL. Note that your expression should work for a list of any length.
LofL = [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
summation = sum(sum(LofL, [])) # 16.1

# Task 0.5.13: Find out what happens if the length of the left-hand side list does not match the length of the right-hand side list.
[x,y,z] = [1,2,3,4]
ValueError: too many values to unpack (expected 3)

[x,y,z] = [1,2]
ValueError: not enough values to unpack (expected 3, got 2)

# Task 0.5.14: Suppose S is a set of integers, e.g. {−4, −2, 1, 2, 5, 0}. Write a triple comprehension whose value is a list of all three-element tuples (i, j, k) such that i, j, k are elements of S whose sum is zero.
tri_tuples = {(x,y,z) for x in S for y in S for z in S if x+y+z==0}

# Task 0.5.15: Modify the comprehension of the previous task so that the resulting list does not include (0, 0, 0). Hint: add a filter.
tri_tuples = {(x,y,z) for x in S for y in S for z in S if x+y+z==0 and (x,y,z)!=(0,0,0)}

# Task 0.5.16: Further modify the expression so that its value is not the list of all such tuples but is the first such tuple.
_tuples = {(x,y,z) for x in S for y in S for z in S if x+y+z==0 an    d (x,y,z)!=(0,0,0)}[0]

# Task 0.5.17: Find an example of a list L such that len(L) and len(list(set(L))) are different.
L = [1,1,1]

# Task 0.5.18: Write a comprehension over a range of the form range(n) such that the value of the comprehension is the set of odd numbers from 1 to 99.
comprehension = [x for x in range(1,100,2)]

# Task 0.5.19: Assign to L the list consisting of the first five letters ['A','B','C','D','E']. Next, use L in an expression whose value is [(0, ’A’), (1, ’B’), (2, ’C’), (3, ’D’), (4, ’E’)] Your expression should use a range and a zip, but should not use a comprehension.
letters = ['A','B','C','D','E']
ran = range(5)
comprehension = [(x,y) for x,y in zip(ran,letters)]

# Task 0.5.20: Starting from the lists [10, 25, 40] and [1, 15, 20], write a comprehension whose value is the three-element list in which the first element is the sum of 10 and 1, the second is the sum of 25 and 15, and the third is the sum of 40 and 20. Your expression should use zip but not list.
l1 = [10,25,40]; l2 = [1,15,20]
comprehension = [x+y for x,y in zip(l1,l2)]

# Task 0.5.21: Suppose dlist is a list of dictionaries and k is a key that appears in all the dictionaries in dlist. Write a comprehension that evaluates to the list whose i th element is the value corresponding to key k in the i th dictionary in dlist. Test your comprehension with some data. Here are some example data. dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}] k = 'James'
dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]
k = 'James'
comprehension = [x[k] for x in dlist]

# Task 0.5.22: Modify the comprehension in Task 0.5.21 to handle the case in which k might not appear in all the dictionaries. The comprehension evaluates to the list whose i th element is the value corresponding to key k in the i th dictionary in dlist if that dictionary contains that key, and 'NOT PRESENT' otherwise. Test your comprehension with k = 'Bilbo' and k = 'Frodo' and with the following list of dictionaries: dlist = [{'Bilbo':'Ian','Frodo':'Elijah'}, {'Bilbo':'Martin','Thorin':'Richard'}]
dlist = [{'Bilbo':'Ian','Frodo':'Elijah'}, {'Bilbo':'Martin','Thorin':'Richard'}]
k = 'Bilbo'
comprehension = [x[k] if k in x else 'NOT PRESENT' for x in dlist]

# Task 0.5.23: Using range, write a comprehension whose value is a dictionary. The keys should be the integers from 0 to 99 and the value corresponding to a key should be the square of the key.
dic = {k:k**2 for k in range(100)}

# Task 0.5.24: Assign some set to the variable D, e.g. D ={'red','white','blue'}. Now write a comprehension that evaluates to a dictionary that represents the identity function on D.
D = {'red', 'white', 'blue'}
dic = {k:k for k in D}

# Task 0.5.25: Using the variables base=10 and digits=set(range(base)), write a dictionary comprehension that maps each integer between zero and nine hundred ninety nine to the list of three digits that represents that integer in base 10. That is, the value should be {0: [0, 0, 0], 1: [0, 0, 1], 2: [0, 0, 2], 3: [0, 0, 3],..., 10: [0, 1, 0], 11: [0, 1, 1], 12: [0, 1, 2],..., 999: [9, 9, 9]} Your expression should work for any base. For example, if you instead assign 2 to base and assign {0,1} to digits, the value should be {0: [0, 0, 0], 1: [0, 0, 1], 2: [0, 1, 0], 3: [0, 1, 1], ..., 7: [1, 1, 1]}

