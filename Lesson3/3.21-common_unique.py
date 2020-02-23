####2Do
# Now let's practice what we've learned about sets.
#
# We will work with these two strings:
#
# string01 = 'Bratislava'
# string02 = 'Budapest'
#
# Write a script that will find and print only elements using a suitable operator or method:
#
# Common - which have string01 and string02 common.
# Unique - which characters are present in string01 but not in string02.
# The output could look like this:
# ~/PythonBeginner/Lesson3 $ python common_unique_chars.py
# Common characters: {'s', 'B', 't', 'a'}
# Unique characters: {'i', 'r', 'l', 'v'}
#######
string01 = 'Bratislava'
string02 = 'Budapest'
common = set(string01) & set(string02)
#unique = set(string01) - set(string02)
unique = set(string01).difference(set(string02))
print('Common characters:', common)
print(' Unique characters in 1vs2:', unique)
