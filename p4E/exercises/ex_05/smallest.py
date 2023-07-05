smallest = None
print("Before", smallest)
for itervar in [12,4,3,5,67,8]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print("loop" , itervar, smallest)
print("Smallest:", smallest)