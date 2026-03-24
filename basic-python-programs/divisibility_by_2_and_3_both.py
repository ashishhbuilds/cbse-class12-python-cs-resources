# A program to check whether a number is divisible by 2 and 3 both.

a = int(input("Enter a number : "))
while True:
    if a%2==0 and a%3==0:
        print("Divisible by 2 and 3 both")
    elif a%2==0 or a%3==0:
        if a%2==0:
            print("Only divisible by 2")
        elif a%3==0:
            print("Only divisible by 3")
    else:
        print("Neither divisible by 2 nor by 3")
    print()
    a = int(input("Enter another number : "))
