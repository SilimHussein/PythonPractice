#this snippet searches through the file for lines starting wiht From
#and prints out the outcome
fhand = open('mbox.txt')
for line in fhand:
    #stripping away the \n character that result in spaces during print
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
        