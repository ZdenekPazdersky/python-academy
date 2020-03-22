# ###2DO
# Write a Python program which prompts and accepts a string of comma-separated numbers from a user and generates a list of those individual numeric strings converted into numbers.
#
# The program should print the resulting list to the terminal.
#
# Also take care of possible spaces that could be located at the beginning or the end of the string. In case you do not know, how to get rid of blank spaces at the beginning or end of a string, we will remind you the .split() method.
# ######
string_1 = input('Enter comma separeted numbers between '', followed by pressing ENTER:')
#print(string_1)
string_1 = string_1.split(',')  #split into list
print(string_1)
result = []
for index in string_1:
   index = int(index.strip())  #removed spaces and changed to integer
   result.append(index)
print(result)