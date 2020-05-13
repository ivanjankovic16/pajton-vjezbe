import string
import random
import logging

# SLIJEDI GENERATOR LOZINKE

# Stvaranje i konfiguracija loggera (ZAMIJENITI 'Junky' sa vlastitim User name-om!!!)
LOG_FORMAT = '%(levelname)s %(asctime)s - %(message)s'
logging.basicConfig(filename = 'C:/Users/Junky/Desktop/logiranjeproba.log', level = logging.DEBUG, format = LOG_FORMAT, filemode = 'w')
logger = logging.getLogger()

# # Dodavanje slova i brojeva u listu za password. Zasad sam odabrao brojeve 6 i 2.
slova = random.sample(string.ascii_letters, k=userInput1)
brojevi = random.sample(string.digits, k=userInput2)
logger.debug('# Dodavanje slova i brojeva u listu za password')

# Priprema liste za password
list1 = [slova + brojevi] 
logger.debug('# Priprema liste za password')

# Generiranje nasumičnog passworda
password = random.choices(list1)

'''Spajanje elemenata u listi'''
for i in password:
	print(''.join(i))

# Upisivanje passworda u logger
logger.info(''.join(i))

# Upisivanje passworda u tekstualni dokument(ZAMIJENITI 'Junky' sa vlastitim User name-om!!!)'
with open('C:/Users/Junky/Desktop/probalozinka.txt', 'w') as f:
	f.write(str(''.join(i)))
	f.close()
logger.debug('# Upisivanje passworda u tekstualni dokument')

# Opcionalno - Prevencija preranog zatvaranja fajla za otvaranje u cmd-u
input('Press<enter>') 