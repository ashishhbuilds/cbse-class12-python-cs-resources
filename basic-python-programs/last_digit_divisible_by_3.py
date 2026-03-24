# A program to check whether the last digit of a number is divisible by 3 or not.
n = int(input('Enter a number :'))
a = n%10
if a%3 == 0:
    print('✅ Last digit of the number you entered is divisible by 3')
else:
    print('❎ Last digit of the number you entered is not divisible by 3')
