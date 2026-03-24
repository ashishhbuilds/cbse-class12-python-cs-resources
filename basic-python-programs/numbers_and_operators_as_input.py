# A program to take numbers and operator as input and perform calculation accordingly.

num1 = int(input('Enter first number : '))
num2 = int(input('Enter second number : '))
print("Choose Operation -")
print('''1 : Addition (+)
2 : Subtraction (-)
3 : Multiplication (*)
4 : Division (/)
5 : Floor Division (//)
6 : Modulus (%)
7 : Exponentiation (**)''')
opt = input('Enter operator : ')

if opt == '1':
    print(num1,'+',num2,'=',num1+num2)
elif opt == '2':
    print(num1,'-',num2,'=',num1-num2)
elif opt == '3':
    print(num1,'*',num2,'=',num1*num2)
elif opt == '4':
    try:
        print(num1,'/',num2,'=',num1/num2)
    except ZeroDivisionError:
        print("Error : Division by zero not allowed")
elif opt == '5':
    print(num1,'//',num2,'=',num1//num2)
elif opt == '6':
    print(num1,'%',num2,'=',num1%num2)
elif opt == '7':
    print(num1,'**',num2,'=',num1**num2)
else:
    print("Invalid Input! Try Again.")