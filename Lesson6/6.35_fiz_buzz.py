# ####2DO
# Write a program that prints the integers from 1 to 100 (inclusive).
#
# But:
#
# for multiples of three, print Fizz (instead of the number)
# for multiples of five, print Buzz (instead of the number)
# for multiples of both three and five, print FizzBuzz (instead of the number)
# Example of running the program for numbers between 10 to 20:
# #######
STOP = int(input('Please enter  STOP number between 10 .. 100:'))
START = 10

for index in range(START, STOP+1):
    if index % 3 == 0 and index % 5 ==0: #Engeto index % 15 == 0
        print('FizzBuzz')
    elif index % 3 == 0:
        print('Fizz')
    elif index % 5 == 0:
        print('Buzz')
    else:
        print(index)
