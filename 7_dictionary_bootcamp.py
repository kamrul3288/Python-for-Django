# A dictionary in Python is a collection of key-value pairs.

alien_0 = {'color': 'green', 'points': 5}
print(alien_0["color"])

alien_0["x_position"] = 15
alien_0["y_position"] = 30

print(alien_0)

# Starting with an Empty Dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# Modifying Values in a Dictionary
alien_0["color"] = "red"
print(alien_0)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

if alien_0["speed"] == "slow":
    x_increment = 1

elif alien_0["speed"] == "medium":
    x_increment = 2

else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

# Removing Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0["color"]
print(alien_0)

# Using get() to Access Values
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get("points", "No point value assigned")
print(point_value)

# Looping Through a Dictionary
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

for key, value in alien_0.items():
    print(f"Key: {key} Value: {value}")

for key in alien_0.keys():
    print(key)

for value in alien_0.values():
    print(value)
