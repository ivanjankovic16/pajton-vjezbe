# Get first and last element of a list 
# a = [5, 10, 15, 20, 25]

#######################
# 1. Using list index

#a = [5, 10, 15, 20, 25]

#b = [a[0], a[-1]]
#print(str(b))

#######################
# 2. Using list slicing

#a = [5, 10, 15, 20, 25]

#b = a[::len(a)-1]
#print(str(b))

#######################
# 3. Using list comprehension

#a = [5, 10, 15, 20, 25]

#b = [a[i] for i in (0, -1)]
#print(b)

#######################
# 4. Using functions

a = [5, 10, 15, 20, 25]

# def first_and_last_element():
# 	b = [a[i] for i in (0, -1)]
# 	print(b)
# first_and_last_element() 

#######################
# NJIHOVO RJEŠENJE

def list_ends(a):
    print([a[0], a[len(a)-1]])
list_ends(a)
