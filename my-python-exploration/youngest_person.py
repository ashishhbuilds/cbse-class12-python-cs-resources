# A program to find the youngest people among four people.

age1 = int(input("Age of first person : "))
age2 = int(input("Age of second person : "))
age3 = int(input("Age of third person : "))
age4 = int(input("Age of fourth person : "))

L = [age1,age2,age3,age4]
L.sort()
print(L[0],'is youngest')
