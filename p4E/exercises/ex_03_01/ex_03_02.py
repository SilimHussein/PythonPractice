"""
this snippet of code calculates gross pay but also uses 
try and except to handle user tracebacks
"""
#user input
hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
#overtime
    if h > 40:
        reg = h * r
        otp = (h - 40) * (r * 0.5)
        xp = reg + otp
        print(xp)
#normal pay
    else:
        xp = h * r
        print(xp)
except:
    print("Please enter a number")