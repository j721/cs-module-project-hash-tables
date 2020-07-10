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

#similar to word_count


# Your code here

ignore = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']

def histogram():

    #counts dictionary for updated string
    counts ={}

    #need to open the filename "robin.txt"
    with open ("robin.txt") as f:
        words = f.read()
        split_words = words.split()     #split the string file into a list of words
    
    for word in split_words:
        #new histogram to be generated starts off with an empty string
        histo = ""

        for character in word:
            if character not in ignore:
                histo += character
        word = histo.lower() #lowercase the new_word string

        #update the counts dictionary with the updated word
        if word in counts:
            counts[word] += 1
        #else if there is no word, just an empty string break/stop running the method
        elif word == "" or word == " ":
            break
        #else if there is already a word in counts have that value set to 1 
        else:
            counts[word] = 1
    


    #create a list of items that returns a key-value tuple pair in the counts dictionary
    items = list(counts.items())     
    #sort using anonymous function starting from negative range to start from largest to smallest number of duplicates. determining the order of the list
    items.sort(key = lambda e: (-e[1], e[0]))
    #convert list of items (key-value pair) into a dictionary and add into counts
    counts = (dict(items))
    #loop through the counts list and check for the string and value(number of duplicates) 
    for (string, value) in counts.items():
        #max method returns the largest item in an iterable
        #returns the string with the longest length (number of duplicates)
                                  #key function iterables are passed on comparison of length performed on return value      
        max_len = len(max(string, key=len))
        print(f'{string} {" " * max_len} {"#" * value}')
        #print our string that is being looped that is our word, then printing out the max length the one from highest number of duplicates to lowest, then going to print value which is hashes
print(histogram())


"""
Hint
-----------
Items: .items() method on a dictionary might be useful.
    -items() method returns a view object that displays a list of a given dictionary's (key, value) tuple pair.

Sorting: it's possible for .sort() to sort on multiple keys at once.

Sorting: negatives might help where reverse won't.

Printing: you can print a variable field width in an f-string with nested braces, like so {x:{y}}
"""