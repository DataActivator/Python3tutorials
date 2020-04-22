'''
A tuple is a data structure that is an immutable, or unchangeable, ordered sequence of elements.
Tuples have values between parentheses ( ) separated by commas , .
'''
# mytuple = ('DS', 'ML', 'DL', 'AI', 'NLP', 'CV', 'Python', 'Java', 'C#', 'C++', 'R')
#           0     1     2     3     4      5       6        7      8      9     10
#          -11   -10   -9    -8    -7     -6      -5       -4     -3     -2     -1

# 1 Access tuple item:
# print(len(mytuple))
# print(mytuple[-1])
# print(mytuple[:8])
# print(mytuple[-6:])
# print(mytuple[:10:2])

# 2 Check if Item Exists:
# print('ML' not in mytuple)
# if 'NLP' in mytuple:
#     print('data activator')


# 3 loop through tuple:
# print(mytuple)
# for item in mytuple:
#     print(item)
# for index, item in enumerate(mytuple, start = 1):
#     print(index ,item)

# 4 join two tuple:
# mytuple = ('DS', 'ML', 'DL', 'AI', 'NLP', 'CV', 'Python', 'Java', 'C#', 'C++', 'R')
# t1 = (1, 2, 3, 4, 5)
# newtuple = mytuple + t1
# print(newtuple)

# 5 some built-in methods:

# print(min(mytuple))
# print(max(mytuple))
# print(sum(t1))

# 6 the tuple() constructor:

# myteam = tuple(('Dhoni', 'Virat','Rohit'))
# print(myteam)
# l1 = [ 2, 45, 678,90 ]
# newtuple1 = tuple(l1)
# print(newtuple1)



# 7 Change Item value in tuple:

# mytuple = ('DS', 'ML', 'DL', 'AI', 'NLP', 'CV', 'Python', 'Java', 'C#', 'C++', 'R')
# mytuple [5] = 'Go'
# print(mytuple)
# newtuple = list(mytuple)
#
# newtuple.insert(5, 'Go')
# print(newtuple)

#Add item in tuple:


#Remove item from tuple:
# del mytuple
# print(mytuple)

# onetuple = ('Dhoni')
# print(type(onetuple))

onetuple = ('Dhoni',)
print(type(onetuple))





