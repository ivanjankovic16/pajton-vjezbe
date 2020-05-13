a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#a2 = [x for x in a if x % 2 == 0]
#b2 = [i for i in b if i % 2 == 0]

#c = [x for x in a if x % 2 == 0] + [i for i in b if i % 2 == 0]

#my_list = print(sorted(list(set([x for x in a if x % 2 == 0] + [i for i in b if i % 2 == 0])))) #ovo je samo za izdvajanje parnih brojeva
#my_list = list(my_set)
#
my_list = print(sorted(list(set([x for x in a if x in b]))))
