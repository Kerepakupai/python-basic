# filter_object = filter(predicate, iterable)
# predicate: Function return True or False

a = [1, 2, 3, 4, 5]

filter_obj = filter(lambda x: x % 2 == 0, a)
print(type(filter_obj))

print(list(filter_obj))


# map_object = map(method, iterable_object, ...)
# Note: When iterables with different sizes are passed to the map() method, 
# then the map function is applied to the elements until one of them is exhausted.

b = [i**2 for i in range(1, 6) if i % 3 == 0]
print(b)

squares = map(lambda x, y: x**2-y, a, b)
print(list(squares))


# from functools import reduce
# reduce_object = reduce(function, iterable)
from functools import reduce

all_multiplied = reduce(lambda a, b: a * b, a)
print(all_multiplied)
