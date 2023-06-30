#user input
score = input("Enter a score :")
fscore = float(score)
if fscore >= 0.0 and fscore <= 0.1:
    print(fscore)
else:
    print("out of range")