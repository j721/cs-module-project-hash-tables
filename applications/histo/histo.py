# Input
# This function takes a single filename string as an argument, e.g.

# robin.txt
# It should open the file, and work through it to produce the output.


# Output
# Print a histogram showing the word count for each word, one hash mark for every occurrence of the word.

# Output will be first ordered by the number of words, then by the word (alphabetically).

# The hash marks should be left justified two spaces after the longest word.

# Case should be ignored, and all output forced to lowercase.

# Split the strings into words on any whitespace.

# Ignore each of the following characters:

# " : ; , . - + = / \ | [ ] { } ( ) * ^ &

# If the input contains no ignored characters, print nothing.

"""
Hint
-----------
Items: .items() method on a dictionary might be useful.

Sorting: it's possible for .sort() to sort on multiple keys at once.

Sorting: negatives might help where reverse won't.

Printing: you can print a variable field width in an f-string with nested braces, like so {x:{y}}
"""
#similar to word_count


# Your code here

ignore = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']

def histogram():

    counts ={}

    #need to open the filename "robin.text"

    with open ("robin.text") as f:
        words = f.read()
        split_words = words.split()     #split the string file into a list of words
    
    for word in split_words:
        #new histogram to be generated starts off with an empty string
        histo = ""