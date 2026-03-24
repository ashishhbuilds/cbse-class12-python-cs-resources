while True:
    L=[]
    def push(L,a):
        L.append(a)
        print(a,"pushed")
    def pop1(L):
        ele=L.pop()
        print(ele,'popped')
    print("Enter 1 to push and 2 to pop")
    ch=int(input("Enter the choise "))
    if(ch==1):
        a=int(input("Enter the ele "))
        push(L,a)
    elif(ch==2):
        if(len(L)==0):
            print("Stack empty")
        else:
            pop1(L)
    else:
        print("Enter the correct choice")
