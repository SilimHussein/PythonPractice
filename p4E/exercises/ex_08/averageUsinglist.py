#creating empty list
numlist = list()
while(True):
    inp = input('Enter a Number:')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)

average = sum(numlist)/len(numlist)
print('Average:', average)
