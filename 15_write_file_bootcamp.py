"""
Python provides inbuilt functions for creating, writing, and reading files.
There are two types of files that can be handled in python,
1)Text files:
2) Binary files:
"""

# Read Only (‘r’)
# Read and Write (‘r+’)
# Write Only (‘w’)
# Write and Read (‘w+’)
# Append Only (‘a’)
# Append and Read (‘a+’)

country_file = open(file="utils/countries.txt", mode="w")

# this line on code create new file with the value
country_file.write("US")
country_file.close()