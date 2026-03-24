'"A program to accept the following from user and calculate the percentage of class attended.\
a) total number of working days.\
b) total number of days absent.\
Show that if percentage is less than 75%, not allowed in exam."'

a = int(input("Total number of working days : "))
b = int(input("Total number of days absent : "))
c = a-b
d = c/a*100
print(d,'% attendence')

if d<75:
    print("Not allowed to give exam")
else:
    print("Allowed to give exam")
