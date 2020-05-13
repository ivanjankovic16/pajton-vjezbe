# Write a program that asks the user how many Fibonnaci numbers 
# to generate and then generates them. Take this opportunity to 
# think about how you can use functions. Make sure to ask the user 
# to enter the number of numbers in the sequence to generate.(Hint: 
# The Fibonnaci seqence is a sequence of numbers where the next number 
# in the sequence is the sum of the previous two numbers in the 
# sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def gen_fib():
	nnums = int(input("How many numbers in a Fibonacci sequence do you want? "))
	n1, n2 = 0, 1
	count = 0
	if nnums <= 0:
	   print("Please enter a positive integer")
	#elif nterms == 1:
	#   print("Fibonacci sequence upto",nnums,":")
	#   print(n1)
	else:
	   print("Fibonacci sequence:")
	   while count < nnums:
	       print(n1)
	       n3 = n1 + n2
	       # update values
	       n1 = n2
	       n2 = n3
	       count += 1 # is the same as count = count + 1. That keeps the index moving forward
gen_fib()

while True:
	answer = input('Do you want to generate another sequence? (yes/no): ')
	if answer == 'yes':
		gen_fib()
	elif answer == 'no':
		break
	else:
		print('Enter yes or no')
	
#input('Press<enter>')