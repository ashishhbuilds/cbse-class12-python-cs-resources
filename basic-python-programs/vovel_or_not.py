# A program to check a character is vowel or not.

vovel = ['a','e','i','o','u','A','E','I','O','U']
A = input("Enter a character : ")
while True:
    if A in vovel:
        print('Vovel is entered')
    else:
        print('Not a vovel')
    print()
    A = input("Enter another character : ")
