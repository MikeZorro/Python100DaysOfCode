print("Welcome to the Tresure Island! Your mission is to find a tresure!")
question1 = input("You are at the crossroads, would you like to turn left or right? Type R or L")
if question1 == "L":
    print("You have been hit by a bus!")
else:
    question2 = input("There is a river. Do you swim across or wait? Type S or W")
    if question2 == "S":
        print("You have been eaten by a shark!")
    else:
        question3 = input("There are three doors. Pick Red, Blue or Yellow")
        if question3 == "Red" or  "Blue" :
                print("Game over. You have been slain!")
        else:
                print("Congratulations, you found a tresure!")

