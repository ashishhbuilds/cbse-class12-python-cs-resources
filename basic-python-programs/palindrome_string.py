# A program that reads a string and check whether it is palindrome string or not.
a=input("Enter a word : ")
b=list(a)
c=list(b)
c.reverse()
if b==c:
    print("Palindrome word is entered")
else:
    print("Not a Palindrome word")
