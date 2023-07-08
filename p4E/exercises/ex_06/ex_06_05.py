str = 'X-DSPAM-Confidence:0.8475'
startpos = str.find(':')
print(startpos)
endpos = str.find("5",startpos)
print(endpos)
dspam = str[startpos+1:endpos+1]
fdspam = float(dspam)
print(fdspam)
print(type(fdspam))