import random

random_number = random.randint(1, 9)

def guessing_game():
	userInput = int(input('Guess the number between 1 and 9: '))
	#lista_pokusaja = []

	while True:
		if userInput == random_number:
			print('Congratulations! You guessed correct!') 
			#print(f'You took {broj_pokusaja} guesses!')
			break
		elif userInput < random_number:
			userInput = int(input('You guessed to low! Try again: '))
		elif userInput > random_number and userInput < 10:
			userInput = int(input('You guessed to high! Try again: '))
		elif userInput > 9:
			userInput = int(input('Error! You should enter a number between 1 and 9!: '))
		else:
			userInput = int(input('Error! You should enter a number between 1 and 9!: '))
			guessing_game()

		#lista_pokusaja.append(userInput)
		#broj_pokusaja = lista_pokusaja.count()

guessing_game()

def play_again():
	answer = print(input('Do you want to play again? (yes/no): '))
	
	while True:
		if answer == 'yes':
			random_number = random.randint(1, 9)
			guessing_game()
		elif answer != 'yes':
			print('Type: yes or no')
		elif answer == 'no':
			break 
play_again()

input('Press<enter>')