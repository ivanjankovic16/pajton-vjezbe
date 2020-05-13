class className:
	def createName(self, name):
		self.name=name
	def displayName(self):
		return self.name
	def saying(self):
		print('hello %s' % self.name)

#print(className)

first=className()
second=className()

first.createName('bucky')
second.createName('tony')

print(first.displayName())
first.saying()

print(first.name)