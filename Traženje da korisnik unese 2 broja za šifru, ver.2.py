import string
import random
import logging

def generate_password():
	try:
		LOG_FORMAT = '%(levelname)s %(asctime)s - %(message)s'
		logging.basicConfig(filename = 'C:/Users/Junky/Desktop/logiranjeproba.log', level = logging.DEBUG, format = LOG_FORMAT, filemode = 'w')
		logger = logging.getLogger()

		userInput1 = int(input('Enter how many letters in password (0 - 10): '))
		userInput2 = int(input('Enter how many numbers in password (0 - 10): '))

		slova = random.sample(string.ascii_letters, k=userInput1)
		brojevi = random.sample(string.digits, k=userInput2)
		logger.debug('# Dodavanje slova i brojeva u listu za password')
		
		list1 = slova + brojevi
		logger.debug('# Priprema liste za password')
		
		password = random.choices(list1)
		#print('dfg')
		#for i in password:
		print(''.join(list1))
		#print('dfg2')
		with open('C:/Users/Junky/Desktop/probalozinka.txt', 'w') as f:
			f.write(str(''.join(list1)))
			f.close()
		logger.debug('# Upisivanje passworda u tekstualni dokument')
		
		logger.info(''.join(list1))

	except:
		print('Advisable to enter a number only between 0 and 10.')

generate_password()

while True:
	answer = input('Do you want to generate another password? (yes/no): ')
	if answer == 'yes' or answer == 'Yes':
		generate_password()
	elif answer == 'no' or answer == 'No':
		break
	else:
		print('Enter yes or no')