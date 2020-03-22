# ########2DO
# Your task is to create 2 functions:
#
# Function that should imitate the built-in function all(). It should take as input any sequence data type and return True, if all items in the sequence have boolean value True, or the sequence is empty. Otherwise it should be return False.
#
# Example of using all():
#
# >>> all([43,45,87,21,23])
# True
# >>> all([])
# True
# >>> all([0,12,431,3])
# False
# Function that should imitate the built-in function any(). It should take as input any sequence data type and return True, if at least one item in the sequence have boolean value True. Otherwise it should be return False - also if the sequence is empty.
#
# Example of using any():
#
# >>> any([43,45,87,21,23])
# True
# >>> any([])
# False
# >>> any([0,12,431,3])
# True
# >>> any(['',[],(),0])
# False
# ###########
def my_all(sequence):
    for index in sequence:
        if bool(index) == False:
            return False
    return True

def my_any(sequence):
    for index in sequence:
        if bool(index):
            return True
    return False

#seq = [43,45,87,21,23]
#seq = [0,12,431,3]
seq = []

print(seq)
print('ALL: ',my_all(seq))
print('ANY: ',my_any(seq))