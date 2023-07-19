str = 'X-DSPAM-Confidence:0.8475'
#we are looking for our starting position which is :
startpos = str.find(':')
print(startpos)
#we look for the first 5 after the starting position (startpos), which is our ending position(endpos)
endpos = str.find("5",startpos)
print(endpos)
dspam = str[startpos+1:endpos+1]
fdspam = float(dspam)
print(fdspam)
print(type(fdspam))