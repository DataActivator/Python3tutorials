'''
A while loop implements the repeated execution of code based on a given Boolean condition.

while [a condition is True]:
    [do something]

As opposed to for loops that execute a certain number of times, while loops are conditionally based
so you don’t need to know how many times to repeat the code going in.
'''

# Q1:-  run the program until user don't give correct captain name
captain = ''
while captain != 'Virat':
    captain = input('Who is the captain of indian Team :- ')
print('Yes, The captain of india is ' + captain)
print('Yes, the captain of india is {} ' .format(captain))
print(f'Yes, The captain of India is {captain.upper()}')

# break & continue example in while loop
i  = 0
while i<5:
    print(i)
    if i == 3:
        break
    i += 1


# else block in for & while loop
i  = 0
while i<5:
    print(i)
    # if i == 3:
    #     break
    i += 1
else :
    print('After while loop ')

print('Data Activator')




