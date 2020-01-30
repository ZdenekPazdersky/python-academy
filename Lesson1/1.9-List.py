###########2do
# Again, use results from previous task. Add following:

# print names on index from 2 to 5 introducing it with a string: 'In interval from 2 to 5 is:',
# print every third element of the employees list introducing it with a string: 'Every third member is:',
# print which index contains the string 'Jacob' in the `employees' list introducing it with a string: ' Jacob is on the index: ',
# print the number of times the name 'Agnes' appears in the list `employees per string: 'Number of Agnes names in the sheet:'.
##############
# Results from the previous task
candidates = ['Agnes', 'Agnes', 'Agnes']
employees = ['Francis', 'Bruno', 'Ann', 'Jacob', 'Claire', 'Agnes', 'Agnes', 'Agnes']


# Interval 2-5
print('IN interval from 2to5 is: ' + str(employees[2:5+1]))

# Each 3rd
print('Every 3rd member is: ' +str(employees[::3]))
print('test for new version')


# Save index
Jacob_index=employees.index('Jacob')

# Jacob index
print('Jacob si on the index: ' + str(Jacob_index))


# Number of name Agnes
Agnes_cnt=employees.count('Agnes')
#print('Number of Agnes names in the sheet: ' + str(employees.count('Agnes')))
print('Number of Agnes names in the sheet: ' + str(Agnes_cnt))