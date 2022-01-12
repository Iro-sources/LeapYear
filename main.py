year = int(input("Which year do you want to check? "))
# This program checks wheter a year is a leap or not

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("is a leap year")
        else:
            print("not a leap year")
    else:
        print("is a leap year")                 
else: 
    print("not a leap")

