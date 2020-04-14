'''
A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements.
Just as strings are defined as characters between quotes('')
lists are defined by having values between square brackets [ ]
Each element or value that is inside of a list is called an item
 '''
mylist = ['DS', 'ML', 'DL', 'AI', 'NLP', 'CV', 'Python', 'Java', 'C#', 'C++', 'R']
#           0     1     2     3     4      5       6        7      8      9     10
#          -11   -10   -9    -8    -7     -6      -5       -4     -3     -2     -1

print(type(mylist))

#Access List item:
print(mylist[5])
print(mylist[-1])
print(mylist[-5:])
print(mylist[::2])


#Change Item value in list:
mylist[1] = 'GO'
print(mylist)




#Check if Item Exists:
print('nlp' in mylist)
print('Java' not in mylist)



#Add  item in list:
#method1 append()
mylist.append('Covid-19')
print(mylist)
#method2 insert()
mylist.insert(0, 'covid-19')
print(mylist)



#Remove item from list:

#method1 remove()
mylist.remove('AI')
print(mylist)

#method2 pop()
mylist.pop(1)
print(mylist)

#method 3 del()
del mylist[3]
print(mylist)





#loop through list:

for x in mylist:
    print(x)
for index, item in enumerate(mylist, start=1):
    print(index, item)


#join two list:
L1 = ['a','b', 'c', 'g', 'v', 's']
L2 = [12, 34, 56, 3, 45, 908, 1]
# using +operator
L3 = L1+L2
print(L3)


# L1.append(L2)
# print(L1)
#
for item in L2:
    L1.append(item)
print(L1)



L1.extend(L2)
print(L1)




#some more built-in methods:
L1 = ['a','b', 'c', 's', 'v', 'g']
L2 = [12, 34, 56, 3, 45, 908, 1]

print(max(L2))
print(min(L2))
print(sum(L2))
L2.reverse()
print(L2)
L1.sort()
print(L1)
L2.sort(reverse=True)
print(L2)
L2.sort()
print(L2)
newList = sorted(L2)
print(newList)



#using list() to create a new list
string ='Hello'
listnew = list(string)
print(listnew)













'''
Operator	                   Description	
 []     (slice)                Returns the item at the given index. A negative index counts the position from the right side.
[ : ]	(Range-slice)          Fetches items in the range specified by the two index operands separated by : symbol.
  +	    (Concatenation)        Returns a list containing all the elements of the first and the second list.
  *	    (Repetition)           Concatenates multiple copies of the same list.	
  in	                       Returns true if an item exists in the given list.	
not in	                       Returns true if an item does not exist in the given string
'''

'''
List built-in methods:-

Method	         Description

append()	     Adds an element at the end of the list
clear()	         Removes all the elements from the list
copy()	         Returns a copy of the list
count()	         Returns the number of elements with the specified value
extend()	     Add the elements of a list (or any iterable), to the end of the current list
index()	         Returns the index of the first element with the specified value
insert()	     Adds an element at the specified position
pop()	         Removes the element at the specified position
remove()	     Removes the item with the specified value
reverse()	     Reverses the order of the list
sort()	         Sorts the list
'''
