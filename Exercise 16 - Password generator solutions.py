# Exercise 16 - Password generator solutions

# Write a password generator in Python. Be creative with how you generate 
# passwords - strong passwords have a mix of lowercase letters, uppercase 
# letters, numbers, and symbols. The passwords should be random, generating 
# a new password every time the user asks for a new password. Include your 
# run-time code in a main method.

#Njihovo rješenje

import string
import random

def pw_gen(size = input, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))

print(pw_gen(int(input('How many characters in your password?'))))

input('Press<enter>')

