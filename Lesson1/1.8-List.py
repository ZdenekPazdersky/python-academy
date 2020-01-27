
####################
# Todo
# We continue to work with the list, with the code from the previous task. Write a script, that will:

# remove the 'Bruno' element from the candidates list,
# print the content of candidates introducing it with a string: 'Bruno removed from candidates:',
# repeat the name 'Agnes' 3 times inside the candidates list,
# print the content of the candidates list introducing it with a string: 'Repetition of Agnes in the candidate list:',
# join the list employees with the listcandidates into a new list which retains the name `employees',
# print the content of the new `employees' list introducing it with a string: 'Joined candidates and employees:',
# print the name on index 2 introducing it with a string: 'On index 2 is:',
# print the name on the last index introducing it with a string: 'On the <last_index> index is:'
# <last_index> * should be replaced with the latest index number from our newly joined employees list.
# An example of a running script that includes a previous task:
####################

# Results from previous task
candidates = ['Bruno', 'Agnes']
employees = ['Francis', 'Bruno', 'Ann', 'Jacob', 'Claire']



# Delete names from candidates
candidates.remove('Bruno')

# Print remaining candidates
print('Bruno removed from candidates:' + str(candidates))


# Repeat element
candidates.extend(['Agnes']*2)


# Print repeating element in list candidates
print('Repetion of Agnes in the candidate list:' + str(candidates))


# Join lists
employees=employees+candidates

# Print joined lists
print('Joined candidates and employees:' + str(employees))

# Index 2
print('On index 2 is: ' +str(employees[2]))


# Find out last index and assign it to variable
last_index = len(employees) - 1
#print('last_index=', last_index)


# Last index
print('On the ' + str(last_index) + ' index is: ' + employees[last_index])