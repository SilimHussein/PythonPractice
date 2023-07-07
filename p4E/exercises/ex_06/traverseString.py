fruit = 'banana'
#accessing characters of a string
letter = fruit[1]
print('letter at index 1:',letter)
#getting the length of a string using len()
length = len(fruit)
print("lenght of string :", length)
#traversing through a string with a loop
index = 0
while index < len(fruit):
    letter = fruit[index]
    print('loop', letter)
    index = index + 1
