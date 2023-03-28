# Tuples are immutable that means you can't update the value

cars = ("bmw", "audi", "Honda")
print(cars)

# cars[0] = "Toyota" it's not working because Tuples are immutable
cars = (1, "audi", "Honda")
print(type(cars[0]))

# Tuples constructor
cars = tuple(("bmw", "audi", "Honda"))
print(cars)