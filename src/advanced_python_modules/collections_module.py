"""

Collections Module
The collections module is a built-in module that implements specialized container data
types providing alternatives to Python’s general purpose built-in containers.

We've already gone over the basics: dict, list, set, and tuple.

Now we'll learn about the alternatives that the collections module provides.

"""

# Counter

# Counter is a dict subclass which helps count hashable objects.
# Inside of it elements are stored as dictionary keys and the counts of the objects are stored as the value.

from collections import Counter

lst = [1,2,2,2,2,3,3,3,1,2,1,12,3,2,32,1,21,1,223,1]

print(Counter(lst))

print('\n') # ========================================================================================================

print(Counter('aabsbsbsbhshhbbsbs'))

print('\n') # ========================================================================================================

s = 'How many times does each word show up in this sentence word times each each word'

words = s.split()

print(Counter(words))

print('\n') # ========================================================================================================

# Methods with Counter()
c = Counter(words)

print(c.most_common(2))

print('\n') # ========================================================================================================

"""

Common patterns when using the Counter() object

sum(c.values())                 # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
c += Counter()                  # remove zero and negative counts

"""

print('\n') # ========================================================================================================

# defaultdict

# defaultdict is a dictionary-like object which provides all methods provided by a dictionary but takes a first argument
# (default_factory) as a default data type for the dictionary.

# Using defaultdict is faster than doing the same using dict.set_default method.

from collections import defaultdict

d = {}

# print(d['one'])

d = defaultdict(object)

print(d['one'])


for item in d:
    print(item)


d = defaultdict(lambda: 0)

print(d['one'])
print(d['wrong_key'])

print('\n') # ========================================================================================================

# namedtuple
# The standard tuple uses numerical indexes to access its members, for example:

t = (12,13,14)

print(t[0])

print('\n') # ========================================================================================================

"""

For simple use cases, this is usually enough.
On the other hand, remembering which index should be used for each value can lead to errors,
especially if the tuple has a lot of fields and is constructed far from where it is used. A namedtuple assigns names,
as well as the numerical index, to each member.

Each kind of namedtuple is represented by its own class,
created by using the namedtuple() factory function.
The arguments are the name of the new class and a string containing the names of the elements.

You can basically think of namedtuples as a very quick way of creating a new object/class type with some attribute fields.
For example:

"""

from collections import namedtuple

Dog = namedtuple('Dog',['age','breed','name'])

sam = Dog(age=2,breed='Lab',name='Sammy')

frank = Dog(age=2,breed='Shepard',name="Frankie")


print(sam)
print(sam.age)
print(sam.breed)
print(sam[0])