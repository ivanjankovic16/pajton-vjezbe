print('Enter a number.')
number = input()
if int(number) % 4 == 0:
    print('This number can be divided by 4.')
elif int(number) % 2 == 0:
    print('This is an even number.')
else: 
    print('This is an odd number.')

print('Enter a number.')
num = input()
print('Enter a second number.')
check = input()
if int(num) % int(check) == 0:
    print('They can divide evenly.')
else:
    print('They divide to odd number.')
