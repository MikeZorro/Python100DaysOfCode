import random


names = input("Put a list of the names!").split(", ")
limit = len(names)
random = random.randint(0, limit)
print(names[random])
