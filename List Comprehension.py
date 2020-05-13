squares = []
for i in range(1, 101):
	squares.append(i**2)
print(squares)


squares2 = [i**2 for i in range(1, 101)]
print(squares2)


remainders5 = [x**2 % 5 for x in range(1, 101)]
print(remainders5)

remainders11 = [x**2 % 11 for x in range(1, 101)]
print(remainders11)


movies = ['Star Wars', 'Ghandi', 'Gattaca', 'Casablanca', 'Ghostbusters', 'Shawshank Redemption', 'Toy Story' ]
gmovies = []
for title in movies:
	if title.startswith('G'):
		gmovies.append(title)
print(gmovies)

gmovies = [title for title in movies if title.startswith('G')]
print(gmovies)


movies = [('Citizen Kane', 1941), ('Spirited Away', 2001), ('Gattaca', 1997)]
pre2k = [title for (title, year) in movies if year < 2000]
print(pre2k)


v = [2, -3, 1]
print(4*v)

w = [4*x for x in v]
print(w)


A = [1, 3, 5, 7]
B = [2, 4, 6, 8]
cartesian_product = [(a, b) for a in A for b in B]
print(cartesian_product)