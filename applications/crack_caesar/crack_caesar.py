# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

with open("ciphertext.txt") as f:
    text = f.read()

#create a hash table of frequencies
freq = {}
for char in text:
    #if the characters does not equal any of the characters to ignore
    if char != "." and char != "\n" and char != "1" and char != ")" and char != "(\n)" and char != "\"" and char != "(" and char != ";" and char != "-" and char != "," and char != "'" and char != " " and char != "—" and char != ":"  and char != "!"and char != "?":
        #if the frequency of the character is none, just set value equal to 1
        if freq.get(char) == None:
            freq[char] = 1
        #else if there is no frequency in character, then add that character into the frequency dictionary     
        else:
            freq[char] += 1

#now calculate the actual character frequency that is looped through the list
for character in list(freq):
    freq[character] = freq[character] / len(text)

#sort by frequency of key/character
def get_freq(key):
    return freq[key]

#sort the frequency, setting reverse to True
sorted_freq = sorted(freq, key = get_freq, reverse = True)

letters = ["E", "T", "A", "O", "H", "N", "R", "I", "S", "D", "L", "W", "U", "G", "F", "B", "M", "Y", "C", "P", "K", "V", "Q", "J", "X", "Z"]

#create an empty cypher dictionary to hold the decoded letters
cypher = {}


#sort through the letters and check for frequency
for l in range(26):    #range of the letters array
    cypher[sorted_freq[l]] = letters[l]


#final decoded text file
final = ""
for char in text:
    #if there's no character in the cypher dictionary then add it to the final string/new modified file
    if cypher.get(char) == None:
        final += char
    #else if there is already a character in the cypher dictionary(already decoded letters) then add it to the final    
    else:
        final += cypher[char]

print(final)





#import from collections library the Counter function- allows for elements to be stored as dictionary keys and their counts stored as dictionary values. Allows for cunting of hashable objects 
# from collections import Counter

# letters = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U','G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

# #need to import ciphertext.txt file
# with open("ciphertext.txt") as f:
#     text = f.read()

# c = Counter(filter(str.isalnum, text))

          #assign key and value in zip format starting from index of 0, and search for the most common letters in frequency  
          # zip function returns an iterator of tuples based on the iterable objects.

# map = {k:v for (k, v) in zip ([i[0] for i in c.most_common()], letters)}

# output =""

# for character in text:
#     output_character = character
#     if character in map.keys():           #keys method displays a list of leys
#         output_character = map[character]
#     output +=output_character

# print(output)