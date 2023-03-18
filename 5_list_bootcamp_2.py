cars = ['bmw', 'audi', 'toyota', 'subaru']

# Looping Through an Entire List with for loop
for car in cars:
    print("For Looping Cars Item: ", car)
print("Cars Looping ended. Thank you.")

# Making Numerical Lists
for value in range(1, 5):
    print("Apply range function: ", value)

print("\n----------Using range() to Make a List of Numbers-----------")
values = list(range(5, 10))
for value in values:
    print("List with range item: ", value)

squares = []
for value in range(1, 5):
    square = value * 2
    squares.append(square)

print("squares: ", squares)

# Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("Max Number", max(digits))
print("Min Number", min(digits))

# List Comprehensions
squares = [value ** 2 for value in range(1, 11)]
print("List Comprehensions: ", squares)

# Working with Part of a List
print("\n---------------Working with Part of a List-------------")
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Slicing 0 to 3 index: ", players[0:3])
print("Slicing 0 to 4 index", players[:4])
print("Slicing 2 to rest", players[2:])
print("Slicing -4 to rest", players[:-4])

print("\n--------------Copying a List----------------")
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My food list: ", my_foods)
print("Copy my food list: ", friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')
print("After append my food list: ", my_foods)
print("After append firend food list: ", friend_foods)

"""
Tuples 
However, sometimes you’ll want to create a list of items that cannot change. Tuples allow you to do just 
that. Python refers to values that cannot change as immutable, and an immutable list is called a tuple.
"""
dimensions = (200, 50)
# dimensions[0] = "300" not working
print("Tuples :", dimensions[0])

