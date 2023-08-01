import re
fname = input('Enter file name :')
try:
    fhand = open(fname)
except:
    print('cannot open file:', fname)
    exit()

for line in fhand:
    line = line.rstrip()
    #print('debug')
    #x = re.findall('\S+@\S+', line)
    #fine tuning to remove characters at the beginning and end
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z0-9]', line)
    if len(x) > 0:
        print(x)