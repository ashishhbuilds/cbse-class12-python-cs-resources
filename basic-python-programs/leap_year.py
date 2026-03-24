# A program to check whether the entered year is a leap year or not.

year = int(input('Enter year : '))
while True:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(year,"is a leap year")
    else:
        print(year,"is not a leap year")
    print()
    year = int(input('Enter year : '))