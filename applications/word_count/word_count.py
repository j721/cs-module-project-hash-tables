"""
input- takes a single string
        -ignore certain characters 

output- returns a dictionary of words and their counts
        -keys all lowercased 
        -split the strings into words on any whitespace
       
If the input contains no ignored characters, return an empty dictionary.
"""


#create an array to ignore certain characters in the string
ignore = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']

def word_count(s):
    #counts dictionary for updated string
    counts = {}
    #loop through string/word that will be updated
    for word in s.split():
        #empty string to hold the updated word
        new_word = ""
        #check if word has characters excluding the ones in the ignore array. And add that to the new_word string
        for character in word:
            if character not in ignore:
                new_word += character
        word = new_word.lower() #lowercase the new_word string

        #update the counts dictionary with the updated word
        if word in counts:
            counts[word] += 1
        #else if there is no word, just an empty string break/stop running the method
        elif word == "" or word == " ":
            break
        #else if there is already a word in counts have that value set to 1 
        else:
            counts[word] = 1

    #if the string is empty then return an empty dictionary
    if s == "":
        return {}
    #else string is not empty, return the counts array with the updated words    
    else:
        return counts



# def word_count(s):
#     # Your code here
#     ignored = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']

#     #create a dictionary for word count to be returned
#     counts = {}

    
#     for word in s.split():
#         new_word = ""
#         for character in word:
#             if character not in ignored:
#                 new_word +=character

#         word = new_word.lower()
       
#         if word in counts:
#             counts[word] +=1
#         elif word == "" or word == " ":
#             break
#         else:
#             counts[word] = 1
        
#         if s == "":
#             return {}
#         else:
#             return counts



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))