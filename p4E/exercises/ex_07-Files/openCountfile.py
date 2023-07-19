#this snipet creates a handle to open file mbox-short.txt and counts the 
#number of lines in the file.
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    count = count + 1

print('Line Count :', count)