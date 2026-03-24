# A program to accept marked price from user and display amount after discount according to given conditions.
    # Marked price > 10,000 : Discount = 20%
    # 7,000 < Marked price <= 10,000 : Discount = 15%
    # Marked price <= 7,000 : Discount = 10%

MP = int(input('Enter marked price : Rs.'))
while True:
    if MP > 10000:
        print("Discount = 20%")
        print("Payable amount =",MP-(20/100*MP),'Rs.')
    elif MP > 7000 and MP <= 10000:
        print("Discount = 15%")
        print("Payable amount =",MP-(15/100*MP),'Rs.')
    elif MP <= 7000:
        print("Discount = 10%")
        print("Payable amount =",MP-(10/100*MP),'Rs.')
    print()
    MP = int(input('Enter marked price : Rs.'))
