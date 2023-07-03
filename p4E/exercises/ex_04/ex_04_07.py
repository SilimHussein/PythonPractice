#user input
score = input("Enter Score:")
try:
    fscore = float(score)

except:
    print("Please enter a Number ")
    quit()


#defining a function to compute grade and return a string
def computegrade(score):
    if score >= 0.0 and score <= 1.0:
        if score >= 0.9:
            return ("A")
        elif score >= 0.8:
            return ("B")
        elif score >= 0.7:
            return ("C")
        elif score >= 0.6:
            return ("D")
        elif score < 0.6:
            return ("E")
    else:
        return ("score out of range")


#calling the function, assigning the return value to a variable and printing the contents of the variable
grade = computegrade(fscore)
print(grade)