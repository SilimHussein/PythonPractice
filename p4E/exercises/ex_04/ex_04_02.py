#calling a function before defining it- error
repeat_lyrics()
#defining a function
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

#calling a function
#print_lyrics()
#using a function inside another function
def repeat_lyrics():
    print_lyrics()
    print_lyrics()


