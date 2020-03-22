####2DO
# Your task is to create 2 functions:
#
# Function my_min that imitate the built-in function min(). It should take as input any sequence data type and return item with the lowest value.
#
# Example of using my_min:
#
# >>> my_min([43,45,87,21,23])
# 21
# Function 'my_max' that should imitate the built-in function max(). It should take as input any sequence data type and return item with the highest value.
#
# Example of using max:
#
# >>> my_max([43,45,87,21,23])
# 87
#######

def my_min(sequence):
    mini = sequence[0]
    for index in sequence:
        if index < mini:
            mini = index
    return mini

def my_max(sequence):
    maxi = sequence[0]
    for index in sequence:
        if index > maxi:
            maxi = index
    return maxi

#seq = [43,45,87,21,23]
#seq = (43,55,101,200)
#seq = [1.1,0,9,5.5]
seq = ['a', 'r', 'e'
print(seq)
print('Minimum: ', my_min(seq))
print('Maximum: ', my_max(seq))
