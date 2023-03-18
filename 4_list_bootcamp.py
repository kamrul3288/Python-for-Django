bicycles = ["Hero", "Fonix", "Redline"]
motorcycles = ['honda', 'yamaha', 'suzuki']
cars = ['bmw', 'audi', 'toyota', 'subaru']

print(bicycles)

# Accessing Elements in a List
print(bicycles[0])
print(f"My first bicycle was : {bicycles[1]}")

# Modifying Elements in a List
print("\n--------------------Modifying Elements in a List------------------")
motorcycles.append("ducati")
print(f"Append Operation: {motorcycles}")

motorcycles[0] = "Hero Honda"
print(f"Index Operation: {motorcycles}")

# Insert item in list
motorcycles.insert(0, "TVS")
print(f"Insert Operation: {motorcycles}")

# Remove item from the list
del motorcycles[0]
print(f"Delete Operation: {motorcycles}")

motorcycles.pop()
print(f"Pop Operation: {motorcycles}")
motorcycles.pop(0)
print(f"Pop Operation 0 Index: {motorcycles}")

# Removing an Item by Value
motorcycles.remove("yamaha")
print(f"Remove yamaha by value operation: {motorcycles}")

# Organizing a List
print("\n--------------------Organizing a List------------------")
print("Actual List: ", cars)

cars.sort()
print("Sort List: ", cars)

cars.sort(reverse=True)
print("Sort List with reverse: ", cars)
print("Sort List Temporarily: ", sorted(cars))

cars.reverse()
print("Reverse List: ", cars)
print("length of list: ", len(cars))