# Problem_1

# Create a generator that generates the squares of numbers up to some number N

def gen_squares(n):
    
    for i in range(n):
        yield i ** 2

for num in gen_squares(10):
    print(num)

gen = gen_squares(10)

print(next(gen))
print(next(gen))
print(next(gen))

print('\n') #============================================================================================================

# Problem_2
# Create a generator that yields "n" random numbers between a low number and a high number (that are inputs).

from random import randint

def rand_num(low_num, high_num, n):
    
    for num in range(n):
        yield randint(low_num, high_num)

for num in rand_num(1, 10, 12):
    print(num)

print('\n') #============================================================================================================

# Problem_3
# Turn the string below into an iterator

s = 'hello'

s_iter = iter(s)

print(next(s_iter))
print(next(s_iter))
print(next(s_iter))

print('\n') #============================================================================================================

# Problem_4

# Explain a use case for a generator using a yield statement where you would not want to use a normal function with a return statement.

# Answer
# If the output has the potential of taking up a large amount of memory and you only intend to iterate through it,
# you would want to use a generator


print('\n') #============================================================================================================

# Extra Credit
# Can you explain what gencomp is in the code below?


my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)

# "gencomp" is a Generator Comprehension

# A generator comprehension is the lazy version of a list comprehension.

# It is just like a list comprehension except that it returns an iterator instead of the list ie an object with a next() method
# that will yield the next element.

# It will not create a list in memory

