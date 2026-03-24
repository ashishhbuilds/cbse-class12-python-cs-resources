# A program to accept three sides of triangle and check whether triangle is possible or not.

print('       .')
print('      ...')
print('     .....')
print('    .......')
print('   .........')
print('  ...........')
print(' .............')
print('...............')
print()
print('Check possibility of triangle')
print()
a = float(input('Length of 1st side : '))
b = float(input('Length of 2nd side : '))
c = float(input('Length of 3rd side : '))

if (a+b)>c:
    print('Triangle is possible')
elif (b+c)>a:
    print('Triangle is possible')
elif (a+c)>b:
    print('Triangle is possible')
else:
    print('Triangle is not possible')
