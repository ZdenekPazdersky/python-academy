# ####2DO
# Write a program that will work with three inputs:
#
# integer start
# integer stop
# integer divisor
# All of them should be provided by the user.
#
# The program should:
#
# generate a collection of integers in range between start (including) and stop (included in the collection)
# print a list of only those numbers in range start - stop, that are divisible by divisor
# If divisor is 0, the program should print to the terminal a string 'Cannot divide by zero' instead of the list of divisible numbers
#
# Example of running the program:
# #####
START = int(input('Enter start number:'))
STOP = int(input('Enter stop number:'))
DIVISOR = int(input('Enter divisor number:'))
numbers = []

for x in range(START, STOP+1):
    if DIVISOR == 0:
        print('Cannot devide by 0!')
        break
    elif x == 0:
        continue
    elif x % DIVISOR == 0:
        numbers.append(x)
print('Numbers in ', range(START, STOP), ' devisible by ', DIVISOR, ' = ', numbers)