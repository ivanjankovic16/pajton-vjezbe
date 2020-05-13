# Exercise 15 - Reverse word order

# Write a program (using functions!) that asks the user for a long string 
# containing multiple words. Print back to the user the same string, except 
# with the words in backwards order. For example, say I type the string:

#  My name is Michele

# Then I would see the string:

#  Michele is name My

# shown back to me.

def reverse_sentence():
	
	string = input('Write a sentence: ')

	def reverse(x):
		x = x[::-1]
		print(x)		
	reverse(string)
reverse_sentence()

while True:		
	answer = input('Dou you want to reverse again? (yes/exit): ')		
	if answer == 'yes':
		reverse_sentence()
	elif answer == 'exit':
		break	
	else:
		print('Enter: yes or exit')
		#input('Press<enter>')
		continue

##########################################
# Njihovo rješenje

# sentence = input('Write a sentence: ')

# def reverseWord(w):
#   print(' '.join(w.split()[::-1]))
# reverseWord(sentence)
# input('Press<enter>')
# morao sam ga doraditi