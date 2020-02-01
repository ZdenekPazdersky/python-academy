#2DO##########
# our task is to create a script called check_start.py that will:
#
# ask the user for the secret password
# if the password given, starts with any of the lowercase 'a','e','f','q','z', print to the terminal 'Welcome!'
# otherwise print 'The input does not match'
##############

pwd=input('Please enter the password:')
pwd_required = ('a', 'e', 'f', 'q', 'z')

if pwd:
    if pwd[0] in pwd_required:
        print('Welcome')
    else:
        print('Input doesn\'t match')
   # print('checking pwd...')
else:
    print('No input provided')
