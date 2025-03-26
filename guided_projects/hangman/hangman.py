import random 
from words import words
import string

def get_valid_word(words):
    word = random.choice(words).upper()
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    # getting user input
    while len(word_letters) > 0:
        # letters used
        print("You have used these letters: ", " ".join(sorted(used_letters)))

        # what current word is (i.e W-RD)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        
        elif user_letter in used_letters:
            print("You have already used that character. Please try again. ")

        else:
            print("Invalid character. Please try again.")
        
    print(f"Congratulations! you have guessed the word : {word} correctly!")
    
    #gets here when len(word_letters) == 0

hangman()