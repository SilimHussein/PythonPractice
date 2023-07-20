#reading through a file
fname = input('Enter file name:')
#error checking for wrong name input.
try:
    fhand = open(fname)
except:
    print('cannot open file:',fname)
    exit()

counts = dict()
#parsing a line
for line in fhand:
    line = line.rstrip()
    #checking if line starts with from
    if not line.startswith('From '): continue
    #spliting the string into words and storing in a list
    words = line.split()
    #getting the second index of the list = email
    email = words[1].split()
    #storing the email in a dictionary
    for sender in email:
        counts[sender] = counts.get(sender,0) + 1

#print(counts)

#finding the most common email sender.
largest = -1
theEmail = None
for k,v in counts.items():
    #print(k,v)
    if v > largest:
        largest = v
        theEmail = k
    
print(theEmail,largest)