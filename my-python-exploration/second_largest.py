#  A program to accept three numbers from user and display the second largest number.

a = float(input("Enter 1st number : "))
b = float(input("Enter 2nd number : "))
c = float(input("Enter 3rd number : "))
L = [a,b,c]
L.sort()
print(L[-2],'is the second largest number')
