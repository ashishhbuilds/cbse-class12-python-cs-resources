# A program that accepts two military time and display the difference between them.

a=input("Enter starting military time : ")
b=input("Enter ending military time : ")
c=a[:2]
d=a[2:4]
e=b[:2]
f=b[2:4]
g=int(c)
h=int(d)
i=int(e)
j=int(f)
print(i-g,'Hours',j-h,'Minutes')
