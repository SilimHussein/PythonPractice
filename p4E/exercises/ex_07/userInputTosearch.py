fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('No file with the name', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
#trying out the str.format() and str.format_map()
#str.format()
message = 'There were {} Subject lines in {}'.format(count, fname)
print(message)

#print('There were', count, 'Subject lines in ', fname)