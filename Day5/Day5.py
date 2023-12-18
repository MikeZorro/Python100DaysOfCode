studentList = [78, 65,89, 86, 91, 84, 80]
highestScore = studentList[0]
for score in studentList:
    if score > highestScore :
        highestScore = score
max = max(studentList)
print(f"Highest score in the class is: {max}")
print(f"Highest score in loop in the class is: {highestScore}")