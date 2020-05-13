import string
import random
import logging

def generate_password():
	LOG_FORMAT = '%(levelname)s %(asctime)s - %(message)s'
	logging.basicConfig(filename = 'C:/Users/Junky/Desktop/logiranjeproba.log', level = logging.DEBUG, format = LOG_FORMAT, filemode = 'w')
	logger = logging.getLogger()

	userInput1 = int(input('Enter how many letters in password: '))
	userInput2 = int(input('Enter how many numbers in password: '))

	slova = random.sample(string.ascii_letters, k=userInput1)
	brojevi = random.sample(string.digits, k=userInput2)
	logger.debug('# Dodavanje slova i brojeva u listu za password')
	
	list1 = [slova + brojevi]
	logger.debug('# Priprema liste za password')
	
	password = random.choices(list1)
	
	for i in password:
		print(''.join(i))
	
	with open('C:/Users/Junky/Desktop/probalozinka.txt', 'w') as f:
		f.write(str(''.join(i)))
		f.close()
	logger.debug('# Upisivanje passworda u tekstualni dokument')
	
	logger.info(''.join(i))

generate_password()

while True:
	answer = input('Do you want to generate another password?')
	if answer == 'yes':
		generate_password()
	elif answer == 'no':
		break
	else:
		print('Enter yes or no')