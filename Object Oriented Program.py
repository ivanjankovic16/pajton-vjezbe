class exampleClass:
	eyes='blue'
	age=22
	def thisMethod(self):
		return 'hey this method worked'

print(exampleClass)

exampleObject=exampleClass()

print(exampleObject.eyes)
print(exampleObject.age)
print(exampleObject.thisMethod())
