'''
A set is a collection of data types in Python, same as the list and tuple.
However, it is not an ordered collection of objects.

A set object contains one or more items, not necessarily of the same type,
which are separated by comma and enclosed in curly brackets {}.

The set is a Python implementation of the set in Mathematics.
A set object has suitable methods to perform mathematical set operations like union, intersection, difference, etc.
'''

# myset = {'DS', 'ML', 'DL', 'AI', 'NLP', 'CV', 'Python', 'Java', 'C#', 'C++', 'R'}

# 1 Access Items
#print(len(myset))



# 2 Check if Item Exists:
# print( 'DS' in myset)


# 3 loop through set:

# for  x in myset:
#     print(x)


#4 Change Items:

#Once a set is created, you cannot change its items, but you can add new items.

#4 Add Item:

#method1 add()

# myset.add('23')
# print(myset)

#method2 update()
# myset.update(['Data', 1, 'Activator'])
# print(myset)


#5 Remove Item:
#method 1 remove()
# myset.remove('php')
# print(myset)

#method 2 discard()

# myset.discard('php')
# print(myset)

s1 = {1, 2, 3, 4,5}
s2 = {4, 5, 6, 7, 8}
#union
# print(s1|s2)
# print(s2.union(s1))

#intersection
# print(s1&s2)
# print(s1.intersection(s2))

#difference
# print(s1-s2)
# print(s1.difference(s2))
# print(s2.difference(s1))

#symmetric difference
# print(s1^s2)
# print(s1.symmetric_difference(s2))


