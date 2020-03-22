# ###2DO
# # When two or more words are composed of the same characters, but in a different order, they are called anagrams. An anagram is direct word switch or word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once.
# #
# # For example the word 'eat' has the following anagrams in english:
# #
# # ate
# # tea
# # There is also a page, that generates anagrams.
# #
# # The goal in this assignment is to create a function all_anagrams that takes a list of 2 or more strings as input and returns boolean value telling us, whether all the strings inside the list are anagrams or not.
# #
# # Example of function in use:
# # >>> all_anagrams(['ship', 'hips'])
# # True
# # >>> all_anagrams(['ship', 'hips', 'name'])
# # False
# # >>> all_anagrams(['ship'])
# # True
# # >>> all_anagrams([])
# # False
# # ######


def all_anagrams(seq):
    LEN = len(seq[0])
    for index in range(1, len(seq)):
        compare_string = seq[0]
        if len(seq[index]) != LEN:
            print('Incorrect length')
            return False
        for i in range(0, LEN):
            if not seq[index][i] in compare_string:
                print('Letter doesn\'t match')
                return False
    return True


test = all_anagrams(['ship', 'hips', 'hhip'])
print(test)

