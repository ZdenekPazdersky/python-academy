###########2Do
# Ask user for any string
# Determine, whether the string entered
# contains only numbers - digits - in that case the program should print to the terminal: 'Numeric'
# contains only letters - in that case the program should print to the terminal: 'Letters Only'
# otherwise print to terminal: 'Mixed'
##############
var_string=input('Enter any string:')

if not var_string:
    print('...No character entered')
elif var_string.isdecimal():
#elif var_string.isnumeric():
    print('...All are numberic')
elif var_string.isalpha():
    print('...All are letters')
else:
    print('...Mixed')