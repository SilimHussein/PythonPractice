#user input
score = input("Enter a score :")
try:
    fscore = float(score)
except:
    print("please enter a number")
    quit()
if fscore >= 0.0 and fscore <= 1.0:
    if fscore >= 0.9:
        print("A")
    elif fscore >= 0.8:
        print("B")
    elif fscore >= 0.7:
        print("C")
    elif fscore >= 0.6:
        print("D")
    elif fscore < 0.6:
        print("E")
else:
    print("out of range")