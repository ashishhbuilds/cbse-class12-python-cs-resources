# A program to print a table in two column first is mile and second is kilometer.

a=int(input("Enter starting : "))
b=int(input("Enter ending : "))
c=b+1
for i in range (a,c):
    print(i,"miles","=",i*1.6,"km")
