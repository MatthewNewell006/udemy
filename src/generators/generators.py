"""

Generator functions allow us to write a function that can send back a value and then later resume to pick up where it left off.

This type of function is a generator in Python, allowing us to generate a sequence of values over time.

The main difference in syntax will be the use of a yield statement.

When a generator function is compiled they become an object that supports an iteration protocol.

That means when they are called in your code they don't actually return a value and then exit.

Generator functions will automatically suspend and resume their execution and state around the last point of value generation.

The advantage is that instead of having to compute an entire series of values up front, the generator computes one value waits until the next value is called for.

For example, the range() function doesn't produce a list in memory for all the values from start to stop.

Instead, it just keeps track of the last number and step size. To provide a flow of numbers.

If a user did need the list, they have to transform the generator to a list with list(range(0, 10))

"""

def create_cubes(n):
    result = []
    
    for x in range(n):
        result.append(x**3)
    return result

print(create_cubes(10))


for x in create_cubes(10):
    print(x)

print('\n') #============================================================================================================

# Using yield will create a generator function and not create a list with stored values.
# It will simply "yield" the desired values thus becoming more energy efficient.

def create_cubes(n):
    
    for x in range(n):
        yield x**3

for x in create_cubes(10):
    print(x)

print(list(create_cubes(10)))

print('\n') #============================================================================================================

def gen_fibonacci(n):
    
    a, b = 0, 1
    
    for i in range(n):
        yield a
        a, b = b, a + b

print(list(gen_fibonacci(11)))

for num in gen_fibonacci(11):
    print(num)

print('\n') #============================================================================================================

# This approach is less memory efficient because it stores values in a list

def gen_fibonacci(n):
    a, b = 0, 1
    output = []
    
    for i in range(n):
        output.append(a)
        a, b = b, a + b
    
    return output

print(gen_fibonacci(11))

print('\n') #============================================================================================================

def simple_gen():
    
    for x in range(3):
        yield x

for number in simple_gen():
    print(number)

print('\n')

g = simple_gen()

print(next(g))
print(next(g))
print(next(g))

print('\n') #============================================================================================================

s = 'hello'

for letter in s:
    print(letter)

print('\n') #============================================================================================================

s_iter = iter(s)

print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))

print('\n') #============================================================================================================

print('\n') #============================================================================================================

print('\n') #============================================================================================================