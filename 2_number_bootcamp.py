#
"""
The number data types are used to store the numeric values.
Python supports integers, floating-point numbers and complex numbers.
"""

# integer number
number = 10
print(number, "is type of", type(number))

# floating point number
number = 10.10
print(number, "is type of", type(number))

# complex number
number = 8 + 2j
print(number, "is type of", type(number))

# Type Conversion in Python
print(1 + 2.0)

print(int(2.3))
print(float(10))
print("I am " + str(8) + " years old")

# Round number
print(round(8.1))
print(round(8.6))

# Round number by decimal point number
print(round(3.141626, 2))

# Absolute Value
print(f"-5 absolute number is: {abs(-5)}")

# height and minimum number
print(f"[4,8] the height number is: {max(4,8)}")
print(f"[4,8,13,1,7] the height number is: {min(4,8,13,1,7)}")

# convert binary number
print(f"34 binary number is: {bin(34)}")