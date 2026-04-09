year = int (input("Enter the year "))
if (year % 400 == 0 or year % 4 == 0 ):
    print("this is a leap year ")
else:
    print("this is not a leap year ")    