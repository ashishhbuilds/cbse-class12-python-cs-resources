# A program to check wheather the number is 3 digit or not.

number = int(input('Enter a number : '))
while True:
    if number >= 100 and number <= 999:
        print('3 digit number')
    else:
        print('Not a 3 digit number')
    print()
    number = int(input('Enter another number : '))
