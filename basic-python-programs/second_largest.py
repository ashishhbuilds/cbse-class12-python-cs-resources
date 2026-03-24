#  A program to accept three numbers from user and display the second largest number.

a = float(input("Enter 1st number : "))
b = float(input("Enter 2nd number : "))
c = float(input("Enter 3rd number : "))

while True:
    if (a>b and a<c)or(a<b and a>c):
        print(a,'is second largest')
    elif (b>c and b<a)or(b<c and b>a):
        print(b,'is second largest')
    else:
        print(c,'is second largest')
    print()
    a = float(input("Enter 1st number : "))
    b = float(input("Enter 2nd number : "))
    c = float(input("Enter 3rd number : "))
