# A program that accepts two integers from the user and prints a message saying if the first number is divisible by second number or not.

a=int(input("Enter 1st number : "))
b=int(input("Enter 2nd number : "))
if a%b==0:
    print(a,"is divisible by",b)
else:
    print(a,"is not divisible by",b)
