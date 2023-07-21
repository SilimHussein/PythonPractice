fname = input('Enter file name:')
try:
    fhand = open(fname)
except:
    print('Cannot open file:',fname)
    exit()

counts = dict()

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    #our email list
    email_list = words[1].split()
    #defining an empty list to store domain names.
    domain_list = []
    
    #looping through each email address in the email_list
    for email in email_list:
        #finding the position of "@" symbol in the email address.
        at_index = email.index("@")

        #slicing domain name from email address and append it to the domain_list
        domain_name = email[at_index + 1:]
        domain_list.append(domain_name)
        #print(domain_list)
        for domain in domain_list:
            counts[domain] = counts.get(domain, 0) + 1
    
print(counts)