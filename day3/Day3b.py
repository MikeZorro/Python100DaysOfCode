
def isLeapYear (year):
    if year % 4 == 0 :
        if year % 100 == 0 & year % 400 != 0:
                print("This is NOT a leap year!")
                return False
        else:
            print("This is a leap year!")
            return True
    else :
        print("This is NOT a leap year!")
        return False
    
isLeapYear(int(input("What year would you like to check?")))