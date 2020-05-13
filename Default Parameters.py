def name(first, last):
	print('%s %s' % (first, last))

name('bucky', 'roberts')
print(name)

def name(first='tom', last='smith'):
	print('%s %s' % (first, last))

print(name())

print(name('bucky', 'roberts'))

print(name('bucky'))

print(name(last='roberts'))