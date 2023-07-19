#user input
sh = input("Enter hours:")
sr = input("Enter rate:")
fh = float(sh)
fr = float(sr)
#overtime
if fh > 40:
    reg = fh * fr
    otp = (fh - 40) * (fr * 0.5)
    #rint(reg, otp)
    #print("overtime")
    gp = reg + otp
    print ("gross pay :", gp)
else:
#regular time
    #print("regular time")
    gp = fh * fr
    print("gross pay", gp)
