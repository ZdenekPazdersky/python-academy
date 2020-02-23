####2DO
# Write a Python program that will create "echo sentences". Each word in the sentence we will feed in, should be repeated n number of times. The number of repetitions and the sentence to be manipulated are inputs provided by the user.
#
# Example:
# If the supplied number of repetitions is 3 and the sentence: 'I do not want to work today'.
#
# Output:
# 'I I I do do do not not not want want want to to to work work work today today today'
#
# The resulting sentence cannot begin with space, unless the input sentence contained it.
#######
repeat = int(input('Enter Nr. of repetitions: '))
sentence = input('Enter your sentence:')
sentence = sentence.split()
#print(sentence)
result = ''
word = ''
while sentence:
    word = sentence.pop(0)
    word = word + ' '
    result = result + repeat*word
print(result)

#Engeto solution
# result = []    #operace budou nad listem, umozni pouzit metodu join a vlozit mezery
# while sentence:
#     word = [sentence.pop(0)]
#     word = word * repeat
#     result = result + word
# result = " ".join(result)
# print(result)
#END Engeto
