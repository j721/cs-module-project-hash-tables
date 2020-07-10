"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

import itertools

q = set(range(1, 10))              #range(x,y)
#q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here

sum_values = {}

for x in q:
    for y in q:
        #perform sum function for f(a) + f(b) = f(c) - f(d)
        val = f(x) + f(y)

        if val not in sum_values:
            sum_values[val] = []
        #else add the update the sum_values with the new computed values
        sum_values[val].append((x,y,True))

        val = f(x) - f(y)
        if val not in sum_values:
            sum_values[val] = []
        sum_values[val].append((x,y,False)) 

for x in list(sum_values):
    tuples = sum_values[x]

    if len(tuples) > 1:
        if tuples[0][2] ^ tuples[1][2]:
            print(f"{tuples[0][0:2]} and {tuples [1][0:2]}")

