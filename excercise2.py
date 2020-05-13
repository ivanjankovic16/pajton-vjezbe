print('Tell me a number.')
number = input()
def parnoneparno(number):
    number1 = int(number)
    if number1 % 2 == 0: #Provjerava da li je ostatak 0
        print('Broj je paran.')
    else:
        print('Neparan.')

parnoneparno(number)
