####2Do
# Your task is to create a script called dist.py. The program should ask for x and y coordinates for 2 points and calculate the distance between those 2 points. The output should be a float, therefore let's round the result to 2 decimal places.
#
# The distance should be straight line between the two points.
# The coordinates cannot be negative numbers.
# Example of running the script:
# /Users/PythonBeginner/Lesson1$ python dist.py
# Point A, X Coordinate: 234
# Point A, Y Coordinate: 34
# Point B, X Coordinate: 27
# Point B, Y Coordinate: 114
#
# The distance between the points A and B is 221.92
#######
import math

X1 = int(input('Enter X1 coordinates (only positive number: '))
Y1 = int(input('Enter Y2 coordinates (only positive number: '))
X2 = int(input('Enter X2 coordinates (only positive number: '))
Y2 = int(input('Enter Y2 coordinates (only positive number: '))

if X1 < 0 or X2 < 0 or Y1 < 0 or Y2 < 0:
    print('Values has to be positive!')
else:
    result = round(math.sqrt(abs(X1 - X2) ** 2 + abs(Y2 - Y1) ** 2), 2)
    print('Distance: ' + str(result))