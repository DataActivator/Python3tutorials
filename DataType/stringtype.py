#Strings are objects of Python's built-in class 'str'.
#stirng can be written in single quotes ('hello'), double quotes ("hello") or triple quotes('''hello''')


name = '''Data Activator'''
# # 1. Data Activator learn 'python' course
# #2. Data Activator learn "python" course
# #. Data Activator "learn" 'python' course
mesaage = '''Data Activator "learn" 'python' course'''
print(mesaage)

# name = 'DataActivator'
#            | D | a | t | a | A | c | t | i | v | a | t | o | r |
#index       | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12|
#            |-13|-12|-------      -------     ------| -3| -2| -1|
print(len(name))

print(name[:4])
print(name[4:])
print(name[4:10])
print(name[start:end:stride])
print(name[::2])
print(name[-4:])

'''
String operations:-
Operator	                   Description	
  []     (slice)               Returns the character at the given index.A negative index counts the position from the right side.
[ : ]	(Range-slice)          Fetches the characters in the range specified by two index operands separated by the : symbol
  +	 (Concatenation)           Appends the second string to the first
  *	 (Repetition)              Concatenates multiple copies of the same string	
  in	                       Returns true if a character exists in the given string	
not in	                       Returns true if a character does not exist in the given string  
'''
greet = 'Welcome'
name = 'DataActivator'
# 1 using +
message = greet +" "+ name
#2 string format
message = '{} {} ' .format(greet,name)
# #3 f format
message = f'{greet} {name.lower()}'

print(message)
print(greet*3)
print('w' in greet)



# All string methods returns new values. They do not change the original string
name = 'Data Activator'

name = name.replace('Activator', 'Science')
print(name)
print(name.endswith('e'))

print(help(str))

'''
Method	           Description
capitalize()	   Converts the first character to upper case
casefold()	       Converts string into lower case
center()	       Returns a centered string
count()	           Returns the number of times a specified value occurs in a string
encode()	       Returns an encoded version of the string
endswith()	       Returns true if the string ends with the specified value
expandtabs()	   Sets the tab size of the string
find()	           Searches the string for a specified value and returns the position of where it was found
format()	       Formats specified values in a string
format_map()	   Formats specified values in a string
index()	           Searches the string for a specified value and returns the position of where it was found
isalnum()	       Returns True if all characters in the string are alphanumeric
isalpha()	       Returns True if all characters in the string are in the alphabet
isdecimal()	       Returns True if all characters in the string are decimals
isdigit()	       Returns True if all characters in the string are digits
isidentifier()	   Returns True if the string is an identifier
islower()	       Returns True if all characters in the string are lower case
isnumeric()	       Returns True if all characters in the string are numeric
isprintable()	   Returns True if all characters in the string are printable
isspace()	       Returns True if all characters in the string are whitespaces
istitle()	       Returns True if the string follows the rules of a title
isupper()	       Returns True if all characters in the string are upper case
join()	           Joins the elements of an iterable to the end of the string
ljust()	           Returns a left justified version of the string
lower()	           Converts a string into lower case
lstrip()	       Returns a left trim version of the string
maketrans()	       Returns a translation table to be used in translations
partition()	       Returns a tuple where the string is parted into three parts
replace()	       Returns a string where a specified value is replaced with a specified value
rfind()	           Searches the string for a specified value and returns the last position of where it was found
rindex()	       Searches the string for a specified value and returns the last position of where it was found
rjust()	           Returns a right justified version of the string
rpartition()	   Returns a tuple where the string is parted into three parts
rsplit()	       Splits the string at the specified separator, and returns a list
rstrip()	       Returns a right trim version of the string
split()	           Splits the string at the specified separator, and returns a list
splitlines()	   Splits the string at line breaks and returns a list
startswith()	   Returns true if the string starts with the specified value
strip()	           Returns a trimmed version of the string
swapcase()	       Swaps cases, lower case becomes upper case and vice versa
title()	           Converts the first character of each word to upper case
translate()	       Returns a translated string
upper()	           Converts a string into upper case
zfill()	           Fills the string with a specified number of 0 values at the beginning
'''