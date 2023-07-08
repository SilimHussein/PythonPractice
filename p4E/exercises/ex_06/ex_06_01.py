fruit = 'banana'
index = len(fruit)
#gives the range of traversal, from 0 - the entire length of the string
while index > 0:
    letter = fruit[index-1]
    print(letter)
    index = index - 1