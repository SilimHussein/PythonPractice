#this snippet uses a function to count the number of times a letter 
#appears in a word. user inputs are the words and letters to be counted
word = input("Enter word:")
letter = input('Enter search letter:')

def wordCount(neno, herufi):
    count = 0
    for herufi in neno:
        if herufi == letter:
            count = count + 1
    return count

times = wordCount(word, letter)
print(letter, 'appears ', times , 'times')
