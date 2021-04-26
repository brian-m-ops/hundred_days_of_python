# Step 1

import random
word_list = ["aardvark", "baboon", "camel"]
guess = input(f'Please guess a letter').lower()


def chosen_word(word_list):
    word = random.choice(word_list)
    return word


# chosen_word(word_list)


def check_guess(chosen_word, guess):
    for letter in chosen_word(word_list):
        if letter == guess:
            print('YES')
        else:
            print('NO')



check_guess(chosen_word, guess)
