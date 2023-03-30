# The try and except block in Python is used to catch and handle exceptions.


# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally-block lets you execute code, regardless of the result of the try- and except blocks.


try:
    x = int(input("Input an integer"))
    print(x)

except ValueError:
    print("Invalid Input Value")

else:
    print("Nothing went wrong")

finally:
    print("try except finished")
