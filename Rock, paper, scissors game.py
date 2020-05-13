while True:
    igrac_1 = input('Enter rock, paper, scissors.')
    igrac_2 = input('Enter rock, paper, scissors.')
                
    if igrac_1 == 'rock' and igrac_2 == 'rock':
        print('Nereseno.')
    elif igrac_1 == 'rock' and igrac_2 == 'paper':
        print('igrac_2 je pobedio.')
    elif igrac_1 =='rock' and igrac_2 == 'scissors':
        print('igrac_1 je pobedio.')
    elif igrac_1 =='paper' and igrac_2 == 'rock':
        print('igrac_1 je pobedio.')
    elif igrac_1 =='paper' and igrac_2 == 'paper':
        print('Nereseno.')
    elif igrac_1 =='paper' and igrac_2 == 'scissors':
        print('igrac_2 je pobedio.')
    elif igrac_1 =='scissors' and igrac_2 == 'rock':
        print('igrac_2 je pobedio.')
    elif igrac_1 =='scissors' and igrac_2 == 'paper':
        print('igrac_1 je pobedio.')
    elif igrac_1 =='scissors' and igrac_2 == 'scissors':
        print('Nereseno.')
    else:
        print('Enter rock, paper, scissors.')
    print('Do you want to play again?')
    igrac_1 = input('Yes or No')
    igrac_2 = input('Yes or No')
    if igrac_1 == 'Yes' and igrac_2 == 'Yes':
        continue
    if igrac_1 == 'No' or igrac_2 == 'No':
        break
    
 
