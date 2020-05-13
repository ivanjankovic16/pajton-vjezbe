class Pizza:
	def __init__(self, ingredients):
		self.ingredients = ingredients

	def __repr__(self):
		return f'Pizza({self.ingredients})'

	@classmethod
	def margheritta(cls):
		return cls(['cheese', 'tomatoes'])

	@classmethod
	def prosciutto(cls):
		return cls(['chesse', 'tomatoes', 'ham', 'mushrooms'])

print(Pizza.margheritta())
print(Pizza.prosciutto())

# Pizza(['cheese', 'tomatoes'])

# Pizza (['chesse', 'tomatoes', 'ham'])

# Pizza (['chesse', 'tomatoes', 'ham', 'mushrooms'])