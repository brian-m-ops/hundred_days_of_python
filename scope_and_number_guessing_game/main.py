from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

answer = random.randint(1, 100)
guesses = int()
game_end = False
player_guess = 0

if difficulty == 'easy':
    guesses = 10
elif difficulty == 'hard':
    guesses = 5

while game_end == False:
    player_guess = int(input("Make a guess: "))
    if guesses == 0:
        print("You've run out of guesses. The correct answer was {answer}")
        game_end == True
        break

    if player_guess == answer:
        print(f"You got it! The answer was {answer}")
        game_end == True
        break
    elif player_guess < answer:
        print("Too Low.\n Guess again.\n")
        print(f"You have {guesses} remaining.")
        guesses -= 1
    elif player_guess > answer:
        print("Too High.\n Guess again.\n")
        print(f"You have {guesses} remaining.")
        guesses -= 1
