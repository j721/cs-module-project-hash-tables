"""
Input: a string of words separated by spaces. Only the letters a-z are utilized.

Output: the string in the same order, but with subsequent duplicate words removed.--create an array to hold no_dup values

There must be no extra spaces at the end of your returned string. --meaning using the join method

The solution must be O(n).

split method- splits a string into a list
"""

def no_dups(s):
    # Your code here




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))