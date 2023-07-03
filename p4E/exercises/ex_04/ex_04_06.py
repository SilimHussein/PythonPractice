#user input
hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)


def computepay(hours, rate):
    #return 42.37
    #overtime
    if hours > 40:
        reg = hours * rate
        otp = (hours - 40) * (rate * 0.5)
        pay = reg + otp
        return (pay)
    #normal pay
    else:
        pay = hours * rate
        return (pay)


gp = computepay(h, r)
print(gp)