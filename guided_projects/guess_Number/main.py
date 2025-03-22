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

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    attempts = 0

    while feedback != 'c' and attempts < 5:
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        attempts += 1

        feedback = input(f'Attempt {attempts}/5: Is {guess} too high (H), too low (L), or correct (C)?').lower()
        
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    if feedback == 'c':
        print(f"Yay! The computer has guessed your number, {guess}, correctly!")
    else:
        print(f"Game over, the computer could'nt guess the number within 5 attempts.")

computer_guess(10)


