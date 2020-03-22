# ###2Do
# our task is to implement a function 'luhn', that will perform credit card number validation based on so called Luhn test. The Luhn test is used by some credit card companies to distinguish valid credit card numbers from what could be a random selection of digits. The function should return a boolean value depending on test result. Your function should be able to except a numeric string as an argument.
#
# Validation by Luhn test
# Reverse the order of the digits in the number,
# take the first, third and every other odd digit in the reversed digits and sum them to form the partial sum s1,
# take the second, fourth and every other even digit in the reversed digits and:
# a. multiply each digit by two,
# b. if the result of digit multiplication is greater than nine (more than 1 digit number) then sum the digits to form the partial sums for each even digit multiplication,
# c. and sum the partial sums of the even digits to form s2,
# if s1 + s2 ends in zero then the original number is in the form of a valid credit card number as verified by the Luhn test.
# The output of the program should be True (valid card number) or False (invalid card number).
#
# Example
# Complicated, huh? Let's try to take a trial number 49927398716:
#
# Step	Description	Results
# 1.	Reverse the digits	61789372994
# 2.	Sum the odd digits	6 + 7 + 9 + 7 + 9 + 4 = 42 = s1
# 3.	The even digits	1, 8, 3, 2, 9
# 3a.	Each even digit x 2	2, 16, 6, 4, 18
# 3b.	Sum the digits of each multiplication	2, 7, 6, 4, 9
# 3c.	Sum the the partial sums	2 + 7 + 6 + 4 + 9 = 28 = s2
# 4.	The sum s1+s2 ends with digit 0	s1 + s2 = 70
# Output	The function returns value	True
# ######

def my_Luhn_test(seq):
    global s1
    global s2
    a = 0

    def my_reversed(seq):
        result = []
        for index in seq:
            result.insert(0, int(index)) #inserting to the first index in integer format (reversed order)
        return result #list of numbers

    result = my_reversed(seq)
    for index, value in enumerate(result):
        if index % 2: # choosing even according index
            a = value * 2
            if a > 9: #2 digit number after multiplication
                a -= 9
            s2 += a #partial sum
        else: #choosing odd according index
            s1 += value
    if (s1 + s2) % 10 == 0: #multiplicable by 10, i.e. ending with 0
        return True
    else:
        return False


s1 = 0
s2 = 0
card_no = '49927398716'
print('Result of the Luhn test >> ', card_no, '>> ',my_Luhn_test(card_no))
print(s1, s2)


