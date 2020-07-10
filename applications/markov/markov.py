import random

#going to try regex
import re


# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

updated_words = []

words = re.split('|\n|\r|\t', words)
ignore = [ "\"", ':', ';', "?", ",", ".", "!", "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&"]

#for word in words
for w in words:
    #remove the ignore characters
    for char in ignore:
        w = w.replace(char, "") #replace the ignore character with an empty string
    w = w.lower()   #lowercase the word

    if w !="":      
        #if word is not an empty string add that to the updated_words array
        updated_words.append(w)


# TODO: analyze which words can follow other words
# Your code here

#create lookup dictionary/hash table

lookup ={}

#loop through length of updated_words array stopping at the last element
for i in range(len(updated_words) -1):
    current = updated_words[i]

    if lookup.get(current) == None:
        #if in the updated_words there there is none then return empty array
        lookup[current] =[]
    #else if there a value is the updated_words array add that into the lookup, have the new word follow after the first word in the [i +1]
    lookup[current].append(updated_words[i +1])    


# TODO: construct 5 random sentences
# Your code here

for x in range(5):
    print(f"random sentence {x}:")

    sentence = ""
