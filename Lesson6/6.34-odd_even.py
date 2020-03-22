# ####2DO
# Write a Python program that will prompt user for a number and then will determine, whether the number is odd or even. You should use ternary operator to solve this task.
# #######
number = int(input('Please input a number:'))
result = 'ODD' if number % 2 else 'EVEN'
print(result)