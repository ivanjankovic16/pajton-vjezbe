
def palindrome():
    print('Enter one word.')
    string = input()
    if string[:] == string[::-1]:
        print('This word is a palindrome.')
    else:
        print('This word is not a palindrome.')
    print('Do you want to enter another word?')
    user = input('') 
    while True:
        if user == 'Yes':
           palindrome()
        elif user == 'No':
            break
        else:
            print('Enter: Yes or No')

