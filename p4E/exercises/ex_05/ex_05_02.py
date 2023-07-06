#this takes input from user, prints max and min, checks for user errors
largest = None
smallest = None
while True:
    num = input('Please Enter a number:')
    if num == 'done':
        break
    try:
        inum = int(num)
    except:
        print('Invalid input')
        continue
    #print(inum)
    if largest is None or inum > largest:
        largest = inum
    if smallest is None or inum < smallest:
        smallest = inum
print('Maximum is', largest)
print('Minimum is', smallest)

