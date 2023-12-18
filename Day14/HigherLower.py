from art import logo
from art import vs
from game_data import data
import random


YOUR_SCORE = 0
WINING_STRIKE = True

importedData = data

def printEntry(choice, keyNumber):
    person = importedData[keyNumber]
    print("Compare " +choice + ": " +person["name"] +", " + person["description"] + ", from " + person["country"])

def compareFollowers(optionTaken, optionAgainst):
     return data[optionTaken]["follower_count"] > data[optionAgainst]["follower_count"]

def playRound(num1, num2):
    print(f"Your current score is: {YOUR_SCORE}")
    printEntry("A", num1)
    print(vs)
    printEntry("B", num2)
    
    choice = input("Who has more followers? Type 'A' or 'B': ")
    print("-----------\n")

    if choice == "A":
        playersChoice = num1
        otherChoice = num2
    elif choice == "B":
        playersChoice = num2
        otherChoice = num1
    else:
        choice = input("Try again, Who has more followers? Type 'A' or 'B': ")

    return playersChoice




print(logo)

firstCelebrity = random.randint(1, len(importedData))

while WINING_STRIKE:

    nextCelebrity =random.randint(1, len(importedData))

    if nextCelebrity == firstCelebrity:
        nextCelebrity = random.randint(1, len(importedData))

    playersChoice = playRound(firstCelebrity, nextCelebrity)

    if playersChoice == firstCelebrity:
        roundResult = compareFollowers(playersChoice, nextCelebrity)
    else:
        roundResult = compareFollowers(playersChoice, firstCelebrity)
        playersChoice == nextCelebrity

    if roundResult:
        YOUR_SCORE += 1
        firstCelebrity == playersChoice
    else:
        WINING_STRIKE == False   
        break


print(f"Your final score is {YOUR_SCORE}")