# A program that calculates and prints the number of seconds in a year.

while True:
    year=int(input("Enter a year : "))
    if year%4==0:
        print(366*24*3600,"seconds")
    else:
        print(365*24*3600, "seconds")
