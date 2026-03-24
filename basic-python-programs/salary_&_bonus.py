# A company decided to give bonus to employee according to following :-
    # Service more than 10 years : 10% Bonus
    # 6 <= Service <= 10 years : 8% Bonus
    # Less than 6 years : 5% Bonus
# Ask user their salary and year of service and print the net bonus.

while True:
    sal = int(input("Enter your salary : Rs."))
    yr = int(input("Enter time period of service"+" (in years)"+" : "))
    a = sal*(10/100)
    b = sal*(8/100)
    c = sal*(5/100)

    if yr > 10:
        print()
        print('Bonus = 10%')
        print('Bonus amount =',a,'Rs.')
        print('Total amount =',sal+a,'Rs.')
    elif yr >= 6 and yr <=10:
        print()
        print('Bonus = 8%')
        print('Bonus amount =',b,'Rs.')
        print('Total amount =',sal+b,'Rs.')
    elif yr < 6:
        print()
        print('Bonus = 5%')
        print('Bonus amount =',c,'Rs.')
        print('Total amount =',sal+c,'Rs')
    print()
