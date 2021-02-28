# Set items are enclosed in curly brackets
# Set is unordered (no indexing)
# Set is mutable, can contain only immutable items
# Set elements are unique
# Elements can contain only immutable items


"""
Sets can be used for mathematical set operations such as union, intersection, difference 
and symmetric difference.

https://en.wikipedia.org/wiki/Set_(mathematics)
"""

'''
Python set Attributes
'''

# print(dir(set))

'''
Creating Python sets
'''
# # integers
# set = {1, 2, 3}
# # mixed data types
# set = {3.2, "Hi", (1, 2, 3)}
# # Distinguish set and dictionary while creating an empty set


# set = {} #this is not a set intead it's a dictionary.
# set = set()
# set = {1,2,3}
# print(type(set))
# print(set)

''' 
modifying a set in Python
''' 

# set_example = {'Hello', 'World'}
# # set_example[0] # will get traceback as set is not support indexing.
# # set_example.add(['Country']) # we can add items inti set but it must be imuutable.
# set_example.add('Region')
# set_example.update([1,2,3])
# # using update() method
# # add multiple elements
# set_example.update([1, 2, 3], {4, 5, 6}, (7, 8,))
# print(set_example)

# print(help(set))
# print(help(set.update))

'''
Removing elements from a set
'''
# set_example = {1,2,3,4}
# # using two method
# # discard doesn't bother if we try something out of range while remove does.
# # set_example.discard(1)
# # set_example.discard(10)

# # set_example.remove(1)
# # set_example.remove(10)

# # also we can use .pop() but it deosn't support indexing so it always will pop a random element .
# # set_example.pop()
# # set_example.pop(2)
# # print(help(set.pop))

# print(set_example)


'''
Set union operations
'''

# a = {1,2,3,6,7}
# b = {4,5,6,7,8,9}

# # using | operator
# # using union() function

# print(a | b)
# print(a.union(b))

'''
Set intersection operations
'''


# a = {1,2,3,6,7}
# b = {4,5,6,7,8,9}
# # using & operator
# # usning intersection operator

# print(a & b)
# print(a.intersection(b))

'''
Set difference operations
'''

# a = {1,2,3,4,6,7,9}
# b = {2,5,6,7,8,9}

# # using - operator
# # using difference() function

# print(a - b)
# print(b - a)

# print(a.difference(b))
# print(b.difference(a))


'''
Set symmetric difference
'''

# a = {1,2,3,4,6,7,9}
# b = {2,5,6,7,8,9}

# # using ^ operator
# # using symmetric_difference method

# print(a^b)
# print(a.symmetric_difference(b))

'''
Set methods
'''

# add() - Adds an element to the set
# clear() - Removes all the elements from the set
# copy() - Returns a copy of the set
# difference() - Returns a set containing the difference between sets
# difference_update() - Removes the items in this set that are also in another
# discard() - Remove the specified item
# intersection() - Returns a set, that is the intersection of two other sets
# intersection_update() - Removes items in a set that are not present in other
# isdisjoint() - Returns whether two sets have a intersection or not
# issubset() - Returns whether another set contains this set or not
# issuperset() - Returns whether this set contains another set or not
# pop() - Removes an element from the set
# remove() - Removes the specified element
# symmetric_difference() - Returns a set with the symmetric differences
# symmetric_difference_update() - inserts the symmetric differences
# union() - Return a set containing the union of sets
# update() - Update the set with the union of this set and others
