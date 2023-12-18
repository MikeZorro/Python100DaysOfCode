import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

map = {
  1: rock,
  2: paper,
  3: scissors
 }

yourchoice = int(input("chose rock - 1, paper - 2 or scissors - 3!"))
computersChoice = (random.randint(1,3))
print(map[yourchoice])
print(map[computersChoice])

if computersChoice - yourchoice == 0:
    print("DRAW!")
elif yourchoice - computersChoice == -1:
    print("You LOSE!") 
elif yourchoice - computersChoice == 2:
    print("You LOSE!") 
else:
    print("You Win!")   
