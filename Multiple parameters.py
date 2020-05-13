def list(*food):
	print(food)

list('apples')

list('apples', 'peaches', 'beef')

def profile(name, *ages):
	print(name)
	print(ages)

profile('bucky', 42, 43, 76, 54, 98)