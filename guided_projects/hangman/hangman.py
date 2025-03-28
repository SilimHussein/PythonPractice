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
    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print(f"you have {lives} left and you have used these letters: "," ".join(sorted(used_letters)))

        # what current word is (i.e W-RD)
        '''
        word_list = []  # Create an empty list
        for letter in word:  
            if letter in used_letters:  
                word_list.append(letter)  # Keep the letter if guessed
            else:
                word_list.append('-')  # Hide the letter if not guessed
    
        LIST COMPREHENSION
        [expression for item in collection if condition]
        Expression → What to do with each item.

        Collection → The list (or range) we're looping through.

        Condition (Optional) → A filter to pick only some items.

        '''
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters: # if the user input is in alphabet and has not been used
            used_letters.add(user_letter) # add it to used letters
            if user_letter in word_letters: # if user input is in the word_letters ( he guessed correctly)
                word_letters.remove(user_letter)# remove it from the word letters.
            
            else:
                lives -= 1
                print('Letter is not in the word')
        
        elif user_letter in used_letters: # if user input has already been tried 
            print("You have already used that character. Please try again. ")

        else:
            print("Invalid character. Please try again.") # if user input is anything other than alphabet
    
    if lives == 0: 
        print(f'You died. The word was {word}') 
    else: 
        print(f"Congratulations! you have guessed the word : {word} correctly!")
    
    #gets here when len(word_letters) == 0 and lives == 0

hangman()