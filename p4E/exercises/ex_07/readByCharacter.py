#this snippet reads the whole file mbox-short.txt into one string 
#using the method .read(), it reads the file character by character.
fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])