largest = None
print("Before:", largest)
for itervar in [34,23,45,9,14]:
    if largest is None or itervar > largest:
        largest = itervar
    print("loop:", itervar, largest)
print("Largest:", largest)