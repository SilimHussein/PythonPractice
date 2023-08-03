import re
fname = input('Enter file name:')
try:
    fhand = open(fname)
except:
    print('cannot open file', fname)
    exit()

regExpression = input('Enter a regular expression:')
match_count = 0
for line in fhand:
    match = re.search(regExpression, line)
    if match != None:
        match_count += 1

print(fname,'had', match_count, 'lines that matched', regExpression)
