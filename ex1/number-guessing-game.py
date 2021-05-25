import random

def guessing_game():
    answer = random.randint(0, 100)

    running = True
    number_of_guesses = 0

    while running:
        try:
            guess = int(input(f"What's your guess?: "))

            number_of_guesses += 1
            if (guess > answer):
                print("Too high. Guess again.")
            elif (guess < answer):
                print("Too low. Guess again.")
            else:
                print(f"Just right, the number was {answer}!")
                print(f"The number of guesses is {number_of_guesses}")
                running = False
            
        except ValueError:
            print("Sorry that's not a number. Try again.")

guessing_game()