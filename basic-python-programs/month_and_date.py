# A program to accept a number from 1 to 12 and display the month name and days in that month.
m=int(input('Enter a number from 1 to 12 : '))
if m==1:
    print('You entered January having 31 days')
elif m==2:
    print('You entered February having 28 or 29 days')
elif m==3:
    print('You entered March having 31 days')
elif m==4:
    print('You entered April having 30 days')
elif m==5:
    print('You entered May having 31 days')
elif m==6:
    print('You entered June having 30 days')
elif m==7:
    print('You entered July having 31 days')
elif m==8:
    print('You entered August having 31 days')
elif m==9:
    print('You entered September having 30 days')
elif m==10:
    print('You entered October having 31 days')
elif m==11:
    print('You entered November having 30 days')
elif m==12:
    print('You entered December having 31 days')
else:
    print('❎ Wrong input, please enter a number from 1 to 12')
