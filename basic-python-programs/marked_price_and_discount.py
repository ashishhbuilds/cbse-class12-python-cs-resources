MP = int(input("Enter marked price : "))
a = MP-(20/100*MP)
b = MP-(15/100*MP)
c = MP-(10/100*MP)
while True:
    if MP > 10000:
        print("Discount = 20%")
        print("Payable amount =",a)
    elif MP >= 7000 and MP <= 10000:
        print("Discount = 15%")
        print("Payable amount =",b)
    elif MP < 7000:
        print("Discount = 10%")
        print("Payable amount =",c)
    print()
    MP = int(input("Enter marked price : "))
