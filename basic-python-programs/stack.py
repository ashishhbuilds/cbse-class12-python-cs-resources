def push(L,element):
    L.append(element)
def Pop(L):
    L.pop()
def display(L):
    for i in L:
        print(i)
L = []
while True:
    print("Enter 1 to push")
    print("Enter 2 to push")
    print("Enter 3 to display")
    choise = int(input("Enter your choise : "))
    if choise == 1:
        element = input("Enter element to push : ")
        push(L,element)
        print(element,"is pushed")
        print()
    elif choise == 2:
        length = len(L)
        if length == 0:
            print("Stack is empty")
            print()
        else:
            pop_element = L[length-1]
            Pop(L)
            print(pop_element,"is popped")
            print()
    elif choise == 3:
        display(L)
        print()
