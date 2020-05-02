'''
for [iterating variable] in [sequence]:
    [do something]

The [do something] will be executed until the sequence is over.
range(start, end, step)
'''
for num in range(0, 15, 3):
   print(num)

# for loop on sequence type
Dhoni_score = [148, 91, 183, 0, 56, 85]
# total = 0
for score in Dhoni_score:
   print(score)
#     total += score    # total = total + score
# print(total)
#
# print(total/len(Dhoni_score))

# break & continue:
# With the break statement we can stop the loop before it has looped through all the items:
# With the continue statement we can stop the current iteration of the loop, and continue with the next:

# for score in Dhoni_score:
#     # print(score)
#     if score == 0:
#             break
#     print(score)

# for score in Dhoni_score:
#     if score == 183:
#         continue
#     print(score)


# nested for
'''
for [first iterating variable] in [outer loop]: # Outer loop
    [do something]  # Optional
    for [second iterating variable] in [nested loop]:   # Nested loop
        [do something]
'''
num_list = [1, 2, 3]
alpha_list = ['a', ' b', 'c']
for number in num_list:
    print(number)
    for letter in alpha_list:
        print(number, letter)



