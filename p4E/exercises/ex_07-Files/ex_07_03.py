#to extract floating point in text we use regular expressions, we need
#to import re module to use regular expressions.
import re
fname = input('Enter file name :')
count = 0
tot = 0
try:
    fhandle = open(fname)
except:
    if fname == 'na na boo boo':
        print('NA NA BOO BOO TO YOU - You have been punk\'d!')
        exit()
    else:
        print('no file with the name', fname)
        exit()

for line in fhandle:
    line = line.rstrip()
    #searching for lines starting with..
    if line.startswith('X-DSPAM-Confidence:'):
        
        #using regular expressions to extract floating point numbers.
        floating_numbers = re.findall(r'\d+\.\d+', line)
        for number in floating_numbers:
            count = count + 1
            fnumber = float(number)
            tot += fnumber
            #print(fnumber)
#print('there are',count, 'ocurance of floating point numbers')
#print('Total:', tot)
print('Average spam confidence:',tot/count)