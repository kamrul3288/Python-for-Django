import utils.constant as constant

# In programming, a variable is a container (storage area) to hold data. For example,
number = 10

firstName = "kamrul"
lastName = "hasan"
print(firstName + lastName)

# Assigning multiple values to multiple variables
firstname, middleName, lastname = "Kamrul", " ", "Hasan"
print(firstname + middleName + lastname)

"""
Rules for Naming Python Variables
Constant and variable names should have a combination of letters in lowercase (a to z) or uppercase (A to Z) or 
digits (0 to 9) or an underscore (_). For example:
"""

# A constant is a special type of variable whose value cannot be changed.
# There are no constants in python, the way exist in C, Java, Kotlin
print(constant.PI)
