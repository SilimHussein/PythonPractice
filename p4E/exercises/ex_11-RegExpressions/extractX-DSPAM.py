#search for lines that start with 'X' followed by a non
#whitespace characters and ':'
#followed by a space and any number.
#the number can include a decimal
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    """"
    if re.search('^X\S*: [0-9.]+', line):
        print(line)
    """

    #if we want to extract numbers only, we use findall and parenthesis
    x = re.findall('^X\S*: ([0-9.]+)', line)
    if len(x) > 0:
        print(x)