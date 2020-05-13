def example(a, b, c):
	return a+b*c
	
tuna=(5, 7, 3)
print(example(*tuna))

def example2(**this):
	print(this)

bacon={'mom':32, 'dad':34}
example2(**bacon) 

