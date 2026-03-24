# A program to accept age, sex('M','F') and number of days and display the wages accordingly.
    # Age : >= 18 and < 30
        # M = 700/day
        # F = 750/day
    # Age : >= 30 and <=40
        # M = 800/day
        # F = 850/day
# If age does not fall in any range then display : "Enter appropriate age".

age = int(input("Enter your age : "))
gender = input("Enter your gender"+' (M/F)'+': ')
days = int(input("Total number of working days : "))
if age >= 18 and age < 30:
    if gender == 'M':
        print(days*700,'Rs')
    elif gender == 'F':
        print(days*750,'Rs')
elif age >= 30 and age <= 40:
    if gender == 'M':
        print(days*800,'Rs')
    elif gender == 'F':
        print(days*850,'Rs')
else:
    print('Enter appropriate age')
