'''
The dictionary is Python’s built-in mapping type.
Dictionaries map keys to values and these key-value pairs provide a useful way to store data in Python.

dictionaries are constructed with curly braces on either side { }. e.g dict ={ key1:value1, key2:value2,...keyN:valueN }
'''
# employee = { 'name': 'Data Activator', 'age':24, 'team': 'Data Science', 'skill': ['Python', 'Data science', 'R'] }

# 1 Access Dictionary Item:

#method get()
# print(employee.get('team'))

# passing key
# print(employee['team'])


# 2 Changing Values :

#method 1
# employee['age'] = 25
# print(employee)

# using update()
# employee.update({'age':27})
# print(employee)

# 3 Adding Items :

employee = { 'name': 'Data Activator', 'age':24, 'team': 'Data Science', 'skill': ['Python', 'Data science', 'R'] }

#method 1
# employee['exp'] = 2
# print(employee)

#method 2
# employee.update({'exp':5})
# print(employee)

# 4 Removing Items :

# using keyword del

# del employee['name']
# print(employee)

#using pop method()
# employee.pop('age')
# print(employee)



# 5 Check if Key Exists :
# if 'name' in employee:
#     print(employee['skill'])





# 6 Three important methods :
'''
dict.keys()       isolates keys &  The keys are then printed within a list format.
dict.values()     isolates values & The value are then printed within a list format.
dict.items()      returns items in a list format of (key, value) tuple pairs
'''

employee = { 'name': 'Data Activator', 'age':24, 'team': 'Data Science', 'skill': ['Python', 'Data science', 'R'] }

# print(employee.keys())
# print(employee.values())
# print(employee.items())

# 7 loop through dictionary :
# for key in employee:
#     print(key)

# for key in employee:
#     print(employee[key])


# for key , value in employee.items():
#     print(key , value)


# employee.clear()
# print(employee)

# del employee
# print(employee)

# 8 some built-in methods :
'''
Method	                Description
clear()             	Removes all the elements from the dictionary
copy()	                Returns a copy of the dictionary
fromkeys()	            Returns a dictionary with the specified keys and value
get()	                Returns the value of the specified key
items()	                Returns a list containing a tuple for each key value pair
keys()	                Returns a list containing the dictionary's keys
pop()	                Removes the element with the specified key
popitem()	            Removes the last inserted key-value pair
setdefault()	        Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	            Updates the dictionary with the specified key-value pairs
values()	            Returns a list of all the values in the dictionary
'''




