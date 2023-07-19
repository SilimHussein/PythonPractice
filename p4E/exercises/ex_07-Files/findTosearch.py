#yet another way to search for lines that dont have @uct.ac.za
#this method uses the find function
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip
    #contracted form of if statement where continue is on the same line as if
    if line.find('@uct.ac.za') == -1: continue
    print(line)