# A program to calculate bill according to following criteria -
    # First 10 km : 11 Rs/km
    # Next 90 km : 10 Rs/km
    # After that : 9 Rs/km

d = int(input("Enter the distance travelled : "))
a = d*11
b = (d-10)*10 + 110
c = (d-100)*9 + 1010

if d <= 10:
    print("Total cost =",a,'Rs')
elif d > 10 and d <=100:
    print("Total cost =",b,'Rs')
elif d > 100:
    print("Total cost =",c,'Rs')
