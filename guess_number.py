# user input a number between 1 and 100
# 3 chances at the most

intAnswer = 58
intChances = 3
intGuess = None

# Using for
for i in range(intChances):
    if i > 0:
        print("You have " + str(intChances-i) + " more chances.")
    try:
        intGuess = int(input("Please guess an integer between 1 and 100: "))
        if intAnswer == intGuess:
            print("You win!")
            break
        else:
            if intAnswer > intGuess:
                print("The answer is greater than " + str(intGuess) + ".")
            else: # elseif intAnswer < intGuess:
                print("The answer is less than " + str(intGuess) + ".")
    except ValueError:
        print("This is not an integer!")

print("You lose.")

"""
# Using while
while intGuess != intAnswer and intChances > 0:
    intChances -= 1
    try:
        intGuess = int(input("Please guess an integer between 1 and 100: "))
        if intAnswer > intGuess:
            strTip = "greater"
        elif intAnswer < intGuess:
            strTip = "less"
        print("The answer is " + strTip + " than " + str(intGuess) + ".")
        if intChances > 0:
            print("You have " + str(intChances) + " more chances.")
    except ValueError:
        print("This is not an integer!")

if intGuess == intAnswer:
    print("You win!")
else:
    print("You lose.")
"""