# ####2Do
# Write a Python program that will count how many vowels and consonants are in a given string. The program should count the number of consonants and vowels inside the sentence: 'A speech sound that is produced by comparatively open configuration of the vocal tract.'
#
# The program should print the resulting counts in format 'No. consonants: <cons_count> | No. vowels: <vowel_count>'
#
# cons_count should be the number specifying the number of consonants in the sentence
# vowel_count should be the number specifying the number of vowels in the sentence
# Example of running the program:
#
# ~/PythonBeginner/Lesson3 $ python count_vow_cons.py
# No. consonants: 43 | No. vowels: 30
# To solve this task you will need the following knowledge:
#
# Membership testing
# String Methods
# Dict Characteristics - Insert new value
# Nested Loops
# If you decide to generate the whole alphabet programmatically, you will probably want to
#
# use your knowledge of sets - Mutable Set Operations
# look up information about built-in function chr() resp. ord()
# #######

sentence = 'A speech sound that is produced by comparatively open configuration of the vocal tract.'
sentence = sentence.replace('.', '').split()
vowels = ['a', 'e', 'i', 'o', 'u']
vowels_count = 0

total_count = 0
vowels_list = []

for i in range(0, len(sentence)):
    total_count += len(sentence[i])
    for j in range(0, len(sentence[i])):
        if (sentence[i][j]) in vowels or sentence[i][j].lower() in vowels:
            vowels_list.append(sentence[i][j])
            vowels_count += 1
print('No. consonants: ', total_count - vowels_count, ' | ', 'No. vowels: ',vowels_count)
print(vowels_list, len(vowels_list))




