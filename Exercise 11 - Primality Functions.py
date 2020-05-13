#userNumber = print(int(input('Enter a number: ')))


# def prime_num_or_not():
# 	if i > 1:
# 		for i in range(2, userNumber):
# 			if (userNumber & i) == 0:
# 				print(userNumber, 'is not a prime number')
# 				break
# 		else:
# 			print(userNumber, 'is a prime number')
# 	# if input number is less than
# 	# or equal to 1, it is not prime
# 	else:
# 		print(userNumber, 'is not a prime number')

# if userNumber > 1:
# 	for i in range(2, userNumber):
# 		if (userNumber % i) == 0:
# 			print(userNumber, 'is not a prime number')
		
# 	else:
# 		print(userNumber, 'is a prime number')
# # if input number is less than
# # or equal to 1, it is not prime
# else:
# 	print(userNumber, 'is not a prime number')

# input('Press<enter>')

##################################

# a = print(int(input('Enter a number: ')))

# def is_prime(a):
#     return all(a % i for i in xrange(2, a))

# a = print(int(input('Enter a number: ')))

########################################


# from math import sqrt; from itertools import count, islice

# n = print(int(input('Enter a number: ')))

# def is_prime(n):
#     return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

# input('Press<enter>')

###################################

# from math import sqrt
# from itertools import count, islice

# n = print(int(input('Enter a number: ')))

# def is_prime(n):
#     if n < 2:
#         return False

#     for number in islice(count(2), int(sqrt(n) - 1)):
#         if n % number == 0:
#             return False

#     return True

# is_prime(n)

# input('Press<enter>')

#########################################

# num = int(input('Insert a number: '))
# a = [x for x in range(2, num) if num % x == 0]

# def is_prime(n):
# 	if num > 1:
# 		if len(a) == 0:
# 			print('prime')
# 		else:
# 			print('NOT prime')
# 	else:
# 		print('NOT prime')
	
# is_prime(num)

# input('Press<enter>')

####################################

def prime():
    x = int(input('Your number:\n'))
    for i in range(2, round(x/2)+2):
        if x % i == 0:
            print('Your number is a composite number')
            break
        else:
            print('Your number is a prime number')
            break
prime()

input('Press<enter>')