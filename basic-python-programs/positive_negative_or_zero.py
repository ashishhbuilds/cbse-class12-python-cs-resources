# A program to get a number and print whether it is positive, negative or zero.

while True:
    x=int(input("Enter a number : "))
    if x>0:
        print("The number you entered is positive")
    elif x<0:
        print("The number you entered is negative")
    elif x==0:
        print("The number you entered is zero")
