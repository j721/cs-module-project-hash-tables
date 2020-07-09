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




# Your code here

ignore = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']

def histogram():
