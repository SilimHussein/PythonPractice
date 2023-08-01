#search for lines that contain 'From'
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    #if re.search('From:',line):
        #print(line)
    #caret ^ character used to begining of a line
    #if re.search('^From:',line):
        #print(line)
    if re.search('^F..m:', line):
        print(line)