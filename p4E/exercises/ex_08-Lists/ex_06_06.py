#re writting a code that prompts users for numbers and prints out max and min
numlist = list()
while(True):
    inp = input('Enter a number:')
    if inp == 'done': break
    finp = float(inp)
    numlist.append(finp)

largest = max(numlist)
print('Largest number is:', largest)
smallest = min(numlist)
print('Smallest numbers is:', smallest)