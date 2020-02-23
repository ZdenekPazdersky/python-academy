#####2Do
# ow, we will work once again with these two strings:
#
# string01 = 'Bratislava'
# string02 = 'Budapest'
#
# Write a script that will find and print only the elements using a suitable operator or method:
#
# Difference - which string01 and string02 do not share. In other words, the elements that are located in string01, string02, but not in both.
# All - which string01 and string02 share and which they do not share - all elements
# The output could look like this:
# ~/PythonBeginner/Lesson3 $ python different_all_chars.py
# Different characters: {'d', 'v', 'u', 'r', 'i', 'e', 'p', 'l'}
# All characters: {'d', 'v', 'e', 'B', 's', 'a', 'u', 't', 'r', 'i', 'p', 'l'}
########
string01 = 'Bratislava'
string02 = 'Budapest'
print('1st string: ', string01, ' 2nd string: ', string02)
#convert to set() first :-)
sym_dif = set(string01).symmetric_difference(set(string02))
union = set(string01).union(set(string02))
print('Not in both ones:', sym_dif)
print('Union:', union)