'''
 Today we will learn the decision control if, else, elif statements in Python
'''

# write a program to check wheteher it is Even number or not ?
if 10<5:
    print('condition True')
else :
    print('condition false')

'''
num =  int(input('Enter a number : '))  # '10'
if num % 2 == 0 :
    print('Even number')
else :
    print('Not even i.e Odd number')
'''


Ind = ['Virat', 'Dhoni', 'Rohit', 'Bumrah']
Aus = ['Smith', 'Warner', 'Starc', 'Maxwell']
Eng = ['Butler', 'stokes', 'Anderson', 'Morgan']

name = input('Enter a players name : ')

if name in Ind :
    print('Player is from India')
elif name in Aus :
    print('australian player')
elif name in Eng :
    print('England Player')
else :
    print('No match for this player')
