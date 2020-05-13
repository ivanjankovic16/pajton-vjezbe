import random

def Guessing_Game_One():
	try:
		userInput = int(input('Guess the number between 1 and 9: '))
		random_number = random.randint(1, 9)
		
		if userInput == random_number:
			print('Congratulations! You guessed correct!')
		elif userInput < random_number:
			print(f'You guessed to low! The correct answer is {random_number}')
		elif userInput > random_number:
			print(f'You guessed to high! The correct answer is {random_number}') 
		elif userInput > 9:
			print('Error! You should enter a number between 1 and 9!')
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
		#print(f'You took {guesses} guesses!') 
		break