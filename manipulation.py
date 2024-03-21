#============  Pseudo code ===============
# This program asks the user for a sentence
# and stores to a variable.

# Then it finds the length of the string

# it finds the last char of the given sent
# and replaces every occurrence of that char with @

# Then it finds the last 3 chars of the sent and
# prints them backwards

# Finds the first 3 and last 2 char of the sent
# and combines them to one 5 char word

#============ Final code ==================

# ask user for input and save in to variable
str_manip = input("Enter a sentence: ")

# get the length of input sentence by using len()
# and wrap it all in print() to get an output
print(len(str_manip))

# find last char of the sentence and replace every occurrence
# of that character in string with it with @
last_letter = str_manip[-1]
char_replac_str = str_manip.replace(last_letter, "@")
print(char_replac_str)

# find the last 3 characters of the string and
#print those letter of the word backwards
last_3_char = str_manip[-3:]
print(last_3_char[::-1])

# get first 3 and last 2 char of sent
# then print out the concatenation of the 2 strings to create 5 char word
first_3_char = str_manip[:3]
last_2_char = str_manip[-2:]
print(first_3_char + last_2_char)