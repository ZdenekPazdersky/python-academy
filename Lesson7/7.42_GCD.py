# ####2DO
# CD is an acronym for Greatest Common Divisor. Your task is to create a function, that will calculate greatest common divisor of two integers.
#
# How to calculate GCD?:
#
# We can use modulo operator to repeatedly calculate the remainder of division among number A and B. If the remainder != 0, then A becomes B and B becomes the remainder in the next iteration. This is done until the remainder of division among A and B is 0.
#
# |  A  |  B  |  Remainder  | Division Result|
# --------------------------------------------
# | 12  |  8  |      4      |        1       |
# |  8  |  4  |      0      |        2       |
# The GCD for numbers 12 and 8 is 4, because after the division by 4, there is 0 remainder.
#
# Example of using gcd() function:
#
# >>> math.gcd(414,78)
# 6
# >>> math.gcd(414,49)
# 1
# #######

def my_gcd(a:int, b:int):
    reminder = 1
    while reminder:
        reminder = a % b
        if reminder:
            a = b
            b = reminder
    return b
seq = (18,84)
print('GCD from ', seq, ': ', my_gcd(84,18))

#ENGETO solution
def gcd(a,b):
    while b > 1:
        remainder = a % b
        if not remainder:
            break
        a,b = b,remainder
    return b
##########