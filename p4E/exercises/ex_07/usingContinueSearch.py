#this is another way of searching through a file using continue to 
#ignore line that we dont want and print line that we want
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip
    #skip uniteresting lines
    if not line.startswith('From:'):
        continue
    #process our interesting lines
    print(line)