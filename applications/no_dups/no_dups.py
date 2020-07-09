"""
Input: a string of words separated by spaces. Only the letters a-z are utilized.

Output: the string in the same order, but with subsequent duplicate words removed.--create an array to hold no_dup values

There must be no extra spaces at the end of your returned string. --meaning using the join method

The solution must be O(n).

split method- splits a string into a list
"""

def no_dups(s):
    # Your code here
    #use split method to return a list of strings
    string_array = s.split()

    #create array to hold no_duplicates
    no_duplicates = []

    #loop through each string from the new array    
    for i in string_array:
        #add the string into the no_duplicates array if not already there
        if i not in no_duplicates:
            no_duplicates.append(i)
    #use join method to have no extra spaces in the returned string being added into the no_duplicates array
    # joins two adjacent elements in iterable way 
    return ' '.join(no_duplicates)



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))