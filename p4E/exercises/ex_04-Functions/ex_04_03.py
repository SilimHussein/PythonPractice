#using a function inside another function
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

#defining the parent function after the child to see what happens
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

repeat_lyrics()