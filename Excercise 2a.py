print('Enter a number.')
number = input()
if int(number) % 4 == 0:
    print('This number can be divided by 4.')
elif int(number) % 2 == 0:
    print('This is an even number.')
else: 
    print('This is an odd number.')
