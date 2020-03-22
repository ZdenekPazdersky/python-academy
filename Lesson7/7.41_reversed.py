####2DO
# Your task is to create a function that will imitate the built-in function reversed(). It will take any sequence as an input and will return a list of items from the original sequence in reversed order.
#
# Example of using the function:
#
# >>> reversed(range(10))
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# >>> reversed(['New', 'Years', 'Eve'])
# ['Eve', 'Years', 'New']
# >>> reversed('Hello World')
# ['d', 'l', 'r', 'o', 'W', ' ', 'o', 'l', 'l', 'e', 'H']
#######

def my_reversed(seq):
    rev_seq = []
    for index in range(0, len(seq)):
        rev_seq.append(seq[len(seq) - 1 - index])
    return rev_seq


test = ['Eve', 'Years', 'New']
print(test, type(test))
print(my_reversed(test))
print(my_reversed(range(10)))
print(my_reversed('Hello world'))


# Engeto solution
def my_reversed(sequence):
    return list(sequence[::-1])


def my_reversed(sequence):
    result = []
    for item in sequence:
        result.insert(0, item)
    return result
################
