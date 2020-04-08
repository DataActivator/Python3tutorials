# 1 Python - Basic Syntax
'''
Just like natural languages, a computer programming language comprises of a set of predefined
words which are called keywords.

A prescribed rule of usage for each keyword is called a syntax.
python3 has 33 keywords :-

False None True	and as assert break class continue def del else elif except	finally for from
global if import in is lambda nonlocal not or pass return raise try while with yield

'''

# 2 Python- Indentation
'''Indentation refers to the spaces at the beginning of a code line.
Python uses indentation to indicate a block of code.'''


if 20 > 10:
    print("Twenty is greater than ten!")


# Indentation error
# if 20 > 10:
# print("Twenty is greater than ten!")

for i in range(5):
    print(i)

# 3 Python- Comment

# Comments starts with a #, and Python will ignore them:

# this is a comment
#print('Hello Data Activator')  # comment can be written after code line also

'''
Multiline comment can be achieved by placing # at start of each line or by enclosing all
comment inside (''' ''')
comment1
comment2
comment3
'''
print("Data Activator lets start variable now.")

# 4 Python- Varibales

'''
Variables are containers for storing data values.
Unlike other programming languages, Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.
'''
age = 25
name = 'Data Activator'
print(age)
print(name)

'''
Variable Names:-
A variable can have a short name (like x and y) or a more descriptive name (age, name, total_marks)
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
'''

#Variables do not need to be declared with any particular type
#it can even change type after they have been set.

# to check the type of variable use type()
marks = 25
print(type(marks))
marks = 'Twenty Five'
print(type(marks))
