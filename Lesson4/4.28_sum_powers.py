###2Do
# Write a Python script that will ask the user to enter a number from which it will compute the result. The result should be the sum of numbers less than or equal to the input number, each raised to power of its value. Then the script should print the result to the terminal.
#
# For example:
#
# if the user enters number 5, the program should compute the sum as: 1**1 + 2**2 + 3**3 + 4**4 + 5**5.
# if the user enters 6, then it should be: 1**1 + 2**2 + 3**3 + 4**4 + 5**5 + 6**6
# ...and so on.
######
number = int(input('Enter finite number for calculation:'))
i = 1
result = 0
while i <= number:
    result = result + i ** i
    i += 1
    # #Engeto solution
    # while nummber:
    #     # 1.
    #     result = result + number ** number
    #     # 2.
    #     number = number - 1
    # #End of Engeto solution
print('Result is:', result)