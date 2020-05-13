nums = [1,2,3,4,5,6,7,8,9,10]

##my_list =[]
##for letter in 'abcd':
##    for num in range(4):
##        my_list.append((letter, num))

#my_list = [(letter, num) for letter in 'abcd' for num in range(4)]

#my_list = [n*n for n in nums]

#my_list = filter(lambda n: n%2 == 0, nums)

##names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
##heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
##
##my_dict = {}
##for name, hero in zip(names, heros):
##    my_dict[name] = hero
##print(my_dict)

##my_dict = {name: hero for name, hero in zip (names, heros) if name != 'Peter'}
##print(my_dict)

#
##my_set = set()
##for n in nums:
##    my_set.add(n)
##print(my_set)

# Generator Expressions
# I want to yield 'n*n' for each 'n' in nums
##def gen_func(nums):
##    for n in nums:
##        yield n*n
##
##my_gen = gen_func(nums)

my_gen = (n*n for n in nums)

for i in my_gen:
    print(i)

