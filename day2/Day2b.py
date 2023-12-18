hight = input("How tall are you?\n")
weight = input("How much do you weight?\n")
BMI = int((float(weight) / (float(hight))**2))

print("your bmi is: " + str((BMI)))
if BMI < 18.5 :
    print("you are too skinny!")
elif 18.5 < BMI < 25:
    print("good BMI!")
elif  25 < BMI < 35:
    print ("Need to lose some weight!")
else :
    print("DAmn you are fat!")

