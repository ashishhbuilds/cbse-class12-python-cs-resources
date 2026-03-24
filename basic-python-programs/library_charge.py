# A program to accept the number of days and calculate the charge for library according to following criteria -
    # Till 5 days : 2 Rs/day
    # 6 to 10 days : 3 Rs/day
    # 11 to 15 days : 4 Rs/day
    # After 15 days : 5 Rs/day

d = int(input("Enter the number of days : "))
a = d*2
b = (d-5)*3 + 10
c = (d-10)*4 + 25
e = (d-15)*5 + 45

if d <= 5:
    print("Total cost =",a,'Rs')
elif d > 5 and d <=10:
    print("Total cost =",b,'Rs')
elif d > 10 and d <=15:
    print("Total cost =",c,'Rs')
elif d > 15:
    print("Total cost =",e,'Rs')
