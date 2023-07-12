#lists are declared like arrays in other languages, elements of 
#arrays/ lists are called items.
cheeses = ['Cheddar','Edam','Gouda']
numbers = [17, 123]
empty = []
print(cheeses, numbers, empty)
#lists are mutable unlike strings
print('item on index [1] is ',numbers[1])
numbers[1] = 5
print('After mutation numbers list looks like:', numbers)
#in operator in lists
'Edam' in cheeses
'Brie' in cheeses
#traversing athe elements of a list using for loop
for cheese in cheeses:
    print('we used for loop to traverse:',cheese)

#combining functions range and len, to write or updated elements of the list using indices
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
    print(numbers)
