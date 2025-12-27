year=int(input("Enter the year"))
if (year % 4 == 0):
    if (year % 100 != 0) or (year % 400 == 0):
        print("The given year is leap year")
    else:
        print("Not a laep year")
else:
    print("Not a laep year")
    
 
