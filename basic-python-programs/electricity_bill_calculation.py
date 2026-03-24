#Calculate the electricity bill according to following conditions-
    #First 100 units - No charge
    #Next 100 units - 5 Rs. per unit
    #After 200 units - 10 Rs. per unit

a=int(input("Enter the number of units consumed : "))
b=0
c=(a-100)*5
d=500+(a-200)*10
#First 100 units = No Charge (a<=100)
if a<=100:
    print("Payable Amount = ",b,"(First 100 units are free)")
#Next 100 units = 5 Rs. per unit (100<a<=200)
if a>100 and a<=200:
    print("Payable Amount = ",c,"(5 Rs. per unit and First 100 units are free)")
#After 200 units = 10 Rs. per unit (a>200)
if a>200:
    print("Payable Amount = ",d,"(10 Rs. per unit and First 100 units are free)")
