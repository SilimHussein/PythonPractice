#this snippet takes user input and prints them one after the other
#until the user types done, then it breaks from the loop
while True:
    line = input("> ")
    if line == "done":
        break
    print(line)
print("All done")