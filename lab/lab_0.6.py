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
Done!

# Task 0.6.5: Type the above for-loop into Python. You will see that, after you enter the first line, Python prints an ellipsis (...) to indicate that it is expecting an indented block of statements. Type a space or two before entering the next line. Python will again print the ellipsis. Type a space or two (same number of spaces as before) and enter the next line. Once again Python will print an ellipsis. Press enter, and Python should execute the loop.
Done!

# Task 0.6.6: Write a procedure makeInverseIndex(strlist) that, given a list of strings (documents), returns a dictionary that maps each word to the set consisting of the document numbers of documents in which that word appears. This dictionary is called an inverse index. (Hint: use enumerate.)
def makeInverseIndex(strlist):
    """
    Returns:
        A dictionary that maps each word to the set 
        consisting of the document numbers of documents 
        in which that word appears.
    """
    # Put content into a long string
    long_str = ""
    for doc in strlist:
        long_str += doc
    
    # Get all elements
    all_elements = {ele for ele in long_str.split()}
    map_dict = dict([(key, None) for key in all_elements])
    for k in map_dict:
        map_dict[k] = {index for index in range(len(strlist)) if k in strlist[index]}
    return map_dict

# This is test:
with open('stories_small.txt') as f:
    content = f.readlines()
r_index = makeInverseIndex(content)

# Task 0.6.7: Write a procedure or Search(inverseIndex, query) which takes an inverse index and a list of words query, and returns the set of document numbers specifying all documents that conain any of the words in query.
def orSearch(inverseIndex, query):
    result = set()
    for item in query:
        result.update(inverseIndex[item] if item in inverseIndex.keys() else {})
    return result

# This is test:
search_result = orSearch(r_index, ['with', 'is', 'haha'])

# Task 0.6.8: Write a procedure andSearch(inverseIndex, query) which takes an inverse index and a list of words query, and returns the set of document numbers specifying all documents that contain all of the words in query.
def andSearch(inverseIndex, query):
    
    for item in query:
        if item not in inverseIndex:
            return {}
        
    result = inverseIndex[query[0]]
    for item in query:
        temp = inverseIndex[item] if item in inverseIndex.keys() else {}
        result = result & temp
    return result

# This is test:
search_result = andSearch(r_index, ['with', 'is'])
