hrs = input('Enter Hours:')
rate = input('Enter rate:')
fhrs = float(hrs)
frate = float(rate)
#calculating overtime
if fhrs > 40:
    reg = fhrs * frate
    otp = (fhrs - 40) * (frate * 0.5)
    xp = reg + otp
    print (xp)
#calculating normal pay
else:
    xp = fhrs * frate
    print(xp)