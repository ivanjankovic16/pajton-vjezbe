# Ask the user to enter a name.

print('Enter a name.')
name = input()
if name == '':
    print('You didnt enter a name.')
try:
    name = int(name)
    print('Nije validno.')
except:
    print('Thank you.')
    

    
