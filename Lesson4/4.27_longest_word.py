#2Do####
#Write a program that will take a list of words as input and will print to the terminal the longest word and its length in one tuple.
########

words = ['Python', 'is', 'a', 'widely', 'used',
         'high-level', 'programming', 'language',
         'for', 'general-purpose', 'programming,',
         'created', 'by', 'Guido', 'van', 'Rossum',
         'and', 'first', 'released', 'in', '1991.']
word = ''
# while words:
#     if len(word) < len(words[0]):
#         word = (words.pop(0))
#     else: words.pop(0)
# word_tuple = (word, len(word))
# print(word_tuple)

# ###Engeto solution
max_word = ('',0)
while words:
    # 2.
    word = words.pop(0)
    # 3.
    if len(word) > max_word[1]:
        # 4.
        max_word = word, len(word)
# 5.
print(max_word)