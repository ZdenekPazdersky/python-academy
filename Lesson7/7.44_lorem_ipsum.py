# #####2DO
# In some situations we need to generate test text as when for example, we need to populate our website with some dummy text before the real content is available. To do this, it is better to have some automatic generator of this so called lorem impsum text. Our task is to create a function that will generate poems from lists of words.
#
# Create a dictionary words, that will contain keys articles, determiners, subjects, verbs and adverbs and relevant values:
#
# articles ("the", "a", "an"),
# determiners ("another", "this", "every", "many")
# subjects ("cat", "dog", "man", "woman"),
# verbs ("sang", "ran", "jumped"), and
# adverbs ("loudly", "quietly", "well", "badly")
# The function lorem_poetry should take input of how many rows should the text have.
#
# The words should be chosen randomly from the above dictionary, but the order in which the words are added together should be somehow meaningful - your program should again choose randomly one of the following orders:
#
# article, subject, verb, adverb
# determiner, subject, verb
# determiner, subject, verb, adverb
# The function should return a string of lorem ipsum sentences, devided by new line (\n) Example of running the program using the above functionality (number 5 as input for the number of the rows):
# ########
import random
words = {
    'articles': ('the', 'a', 'an'),
    'determiners': ('another', 'this', 'every', 'many'),
    'subjects': ('cat', 'dog', 'man', 'woman'),
    'verbs': ('sang', 'ran', 'jumped'),
    'adverbs': ('loudly', 'quietly', 'well', 'badly')
    }
orders = [['articles', 'subjects', 'verbs', 'adverbs'],
         ['determiners', 'subjects', 'verbs'],
         ['determiners', 'subjects', 'verbs', 'adverbs']]
print(words)
# print(words.keys())

def lorem_poetry(number_sentences: int):
    sentences = []
    for index in range(number_sentences): #vytvari jednotlive vety
        order = random.choice(orders) #vyber nahodneho listu s vyberem klicu
        # print(order)
        sentence = []
        for j in order: #vytvari jednotliva slova ve vete
            sentence.append(random.choice(words[j])) #pridava nahodna slova do listu dane vety
            #print(sentence)
        sentences.append(' '.join(sentence)) #spoji list z vety a pridava vety v dalsich cyklech
        #print(sentences)
    result = '\n'.join(sentences)   #vypise jednotlive vety, ktere mam v listu a oddeli novym radkem
    print(result)
    return result

lorem_poetry(5)