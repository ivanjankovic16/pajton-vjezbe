import random

def Guessing_Game_One():
	try:
		random_number = random.randint(1, 9)
		global guesses
		guesses = 0
		
		while True:
			userInput = int(input('Guess the number between 1 and 9: '))
					
			if userInput == random_number:
				print('Congratulations! You guessed correct!')
				guesses +=1
				print(f'You took {guesses} guesses!')
				break
			elif userInput < random_number:
				print('You guessed to low!')
			elif userInput > random_number:
				print('You guessed to high!') 
			elif userInput > 9:
				print('Error! You should enter a number between 1 and 9!')
			guesses +=1
	except:
			print('Error! You must enter a number between 1 and 9.')
			
			Guessing_Game_One()
Guessing_Game_One()

while True:
	answer = input('Dou you want to play again? (yes/exit): ')
	if answer == 'yes':
		Guessing_Game_One()
	elif answer != 'exit':
		print('Enter: yes or exit')
	elif answer == 'exit':
		print(f'You took {guesses} guesses!') 
		input('Press<enter>')
		break
	