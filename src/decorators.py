"""

Decorators allow you to tack on extra functionality to an already existing function.
They use the @ operator and are then placed on top of the original function

@some_decorator
def simple_func():
Do simple stuff
return something

"""

def func():
    return 1

print(func())

print(func)

print('\n') #============================================================================================================


def hello():
    return 'Hello!'

print(hello())
print(hello)

greet = hello
print(greet())

print('\n') #============================================================================================================


def hello(name = 'Jose'):
    print('The hello() function has been executed!')
    
    def greet():
        return '\t This is the greet() function inside hello!'
    
    def welcome():
        return '\t This is welcome() function inside hello!'
    
    print(greet())
    print(welcome())
    print('This is the end of the hello() function!')


hello()


print('\n') #============================================================================================================


def hello(name = 'Jose'):
    print('The hello() function has been executed!')
    
    def greet():
        return '\t This is the greet() function inside hello!'
    
    def welcome():
        return '\t This is welcome() function inside hello!'
    
    print("I'm going to return a function")
    
    if name == 'Jose':
        return greet
    else:
        return welcome

my_new_func = hello('Jose')

my_new_func

print(my_new_func())


print('\n') #============================================================================================================


def cool():
    
    def super_cool():
        return 'I am very cool'
    
    return super_cool

some_func = cool()

print(some_func())


print('\n') #============================================================================================================


def hello():
    return 'Hi Jose'

def other(some_def_func):
    print('Other code runs here!')
    print(some_def_func())


other(hello)


print('\n') #============================================================================================================


def new_decorator(original_function):
    
    def wrap_func():
        
        print('Some extra code, before the original function')
        
        original_function()
        
        print('Some extra code, after the original function')
    
    return wrap_func


def func_needs_decorator():
    print('I want to be decorated!!')

decorated_func = new_decorator(func_needs_decorator)

decorated_func()

print('\n') #============================================================================================================


def new_decorator(original_function):
    
    def wrap_func():
        
        print('Some extra code, before the original function')
        
        original_function()
        
        print('Some extra code, after the original function')
    
    return wrap_func

@new_decorator
def func_needs_decorator():
    print('I want to be decorated!!')

func_needs_decorator()


print('\n') #============================================================================================================


def decorator_test(decorator_func):
    def test():
        print('Testing the decorator')
        decorator_func()
    return test

@decorator_test
def testing():
     print(2 ** 2)

testing()