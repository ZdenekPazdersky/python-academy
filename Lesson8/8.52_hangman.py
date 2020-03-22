# # ####2DO
# # The goal of this exercise is to implement the hangman game. The game is played by 2 players, in this case by the computer and the human. The computer selects a secret word and the human tries to guess it by suggesting letters or numbers, within a certain number of guesses.
# #
# # The word to guess is represented by a row of dashes, representing each letter of the word.
# #
# # Each time the human player suggests a letter that is not present in the guessed word, the counter of incorrect guesses is increased by one.
# #
# # Computer wins and the game ends if the number of incorrect guesses reaches specified amount. The human wins if the whole word is guessed before reaching the limit of incorrect guesses.
# #
# # You shall decide what the limit of incorrect guesses should be.
# #
# # Example of running the program:
# ~/PythonBeginner/Lesson5 $ python hangman.py
# I am thinking of a word. What word is it?:
# _ _ _ _ _ _ _
# Guess a letter (9 guesses available): 'C'
# No, the letter 'C' is not in my word
# _ _ _ _ _ _ _
# Guess a letter (8 guesses available): 'B'
# No, the letter 'B' is not in my word
# _ _ _ _ _ _ _
# Guess a letter (7 guesses available): 'H'
# Yes, there is 1 letter 'H'
# H _ _ _ _ _ _
# Guess a letter (7 guesses available): 'a'
# Yes, there are 2 letters 'a'
# H a _ _ _ a _
# # #######

def main(seq):
    import random
    print('I am thinking of a word. What word is it?')
    word_to_find = random.choice(seq)
    guess_cnt = len(word_to_find) + 1
    human_word = ['_'] * len(word_to_find)
    while True:
        letter = input_letter(human_word, guess_cnt)
        human_word = check_letter(letter, word_to_find, human_word)
        guess_cnt -= 1
        if '_' not in human_word:   #has to be checked first, just in the case the last attempt will be succ
            print('Congratulation, you have won the game! Found: ', word_to_find)
            break
        if not guess_cnt: #number of attempts is gone
            print('You have lost. The searched word was:', word_to_find)
            break
def check_letter(character, word_to_find, human_word):
    count_found = 0
    for index, value in enumerate(word_to_find):
        if character == value: #character found, counter increased and letter added to the list
            count_found += 1
            human_word[index] = value

    if count_found: #how many time character was found
        print('Yes, ', count_found, character, 'found.')
    else:
        print('No, letter ', character, 'not found.')
    return human_word   #input and output to be run more times


def input_letter(human_word, guess_cnt): #print the name of already found letters and return input prompt for next character
    print(' '.join(human_word))
    letter = input('Guess a letter (' + str(guess_cnt) + ' guesses available):')
    return letter

test = ['Zdenek', 'Lucie', 'Engeto']
main(test)

