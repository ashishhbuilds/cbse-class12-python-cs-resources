# A program to find the largest number out of three numbers.

a = float(input("Enter 1st number : "))
b = float(input("Enter 2nd number : "))
c = float(input("Enter 3rd number : "))

while True:
    if a>b and a>c:
        print(a,'is largest')
    elif b>a and b>c:
        print(b,'is largest')
    elif c>a and c>b:
        print(c,'is largest')
    print()
    a = float(input("Enter 1st number : "))
    b = float(input("Enter 2nd number : "))
    c = float(input("Enter 3rd number : "))
