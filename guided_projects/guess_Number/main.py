import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    attempts = 0
    
    while guess != random_number and attempts < 5:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        attempts += 1

        if guess < random_number:
            print("Sorry, too low. Try again")
        elif guess > random_number:
            print("Sorry, too high. Try again")

        if guess == random_number:
            print(f"Yaay! you have guessed the number {random_number} correctly! Congratulations")

        if attempts == 5:
            print(f"Game over! The number was {random_number}.")
            break

guess(10)


