# Exercise 14 - List remove duplicates 

# Write a program (function!) that takes a list and returns a new list that 
# contains all the elements of the first list minus all the duplicates.

#Extras:

    # Write two different functions to do this - one using a loop and constructing 
    # a list, and another using sets.
    # Go back and do Exercise 5 using sets, and write the solution for that 
    # in a different function.

a = [1,1,2,2,3,3,4,4,5,5]

# Using sets
def no_duplicates():
	b = set(a)
	c = list(b)
	print(c)
no_duplicates()

# Using loop
def remove_dup(a):
   i = 0
   while i < len(a):
      j = i + 1
      while j < len(a):
         if a[i] == a[j]:
            del a[j]
         else:
            j += 1
      i += 1

s = ['cat','dog','cat','mouse','dog']
remove_dup(s)
print(s)

#####################################
# Njihovo rješenje 
# this one uses a for loop
def dedupe_v1(x):
  y = []
  for i in x:
    if i not in y:
      y.append(i)
  return y

#this one uses sets
def dedupe_v2(x):
    return list(set(x))

r = [1,2,3,4,3,2,1]
print(r)
print(dedupe_v1(r))
print(dedupe_v2(r))

####################################
# Exercise 5 using sets and function

# Take two lists, say for example these two:

  # e = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  # f = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# and write a program that returns a list that contains only the elements 
# that are common between the lists (without duplicates). Make sure your 
# program works on two lists of different sizes.

# Extras:
    # Randomly generate two lists to test this
    # Write this in one line of Python

import random
import string

e = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
f = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def common_elements(a, b):
	print([int(i) for i in(sorted(list(set(a + b))))])
common_elements(e, f)

# Randomly generated lists
lista1 = random.sample(range(1, 10), 5)
lista2 = random.sample(range(1, 15), 4)
# ili ovo dolje alternativno
#lista1 = random.sample(string.digits, k=10) 
#lista2 = random.sample(string.digits, k=15) 

common_elements(lista1, lista2)