# A program to find the youngest people among four people.

name1 = input('Name of first person : ')
age1 = int(input("Age : "))
print()
name2 = input('Name of second person : ')
age2 = int(input("Age : "))
print()
name3 = input('Name of third person : ')
age3 = int(input("Age : "))
print()
name4 = input('Name of fourth person : ')
age4 = int(input("Age : "))
print()
if age1<age2 and age1<age3 and age1<age4:
    print(name1,'is youngest')
elif age2<age1 and age2<age3 and age2<age4:
    print(name2,'is youngest')
elif age3<age1 and age3<age2 and age3<age4:
    print(name3,'is youngest')
else:
    print(name4,'is youngest')
