# functions, which are named blocks of code that are designed to do one specific job
def greet_user():
    print("Welcome Kamrul Hasan")


greet_user()


# Passing Information to a Function
def greet_user(name=""):
    print("Welcome " + name)


greet_user(name="Kamrul Hasan")


# Returning a Simple Value
def sum_two_number(num1: int, num2: int):
    return num1 + num2


value = sum_two_number(num1=10, num2=15)
print(value)


# Making an Argument Optional
def get_formatted_name(first_name: str, last_name: str, middle_name: str = ''):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name


print(get_formatted_name(first_name="Kamrul", last_name="Hasan"))


# Passing Tuples
def make_pizza(*ingredients):
    # You’ll often see the generic parameter name *args, which collects arbitrary positional arguments like this.
    print(ingredients)


make_pizza('mushrooms', 'green peppers', 'extra cheese')


# Passing non-specific keyword arguments.
def build_profile(first_name: str, last_name: str, **user_info):
    # You’ll often see the parameter name **kwargs used to collect non-specific keyword arguments.
    user_info["first_name"] = first_name
    user_info["last_name"] = last_name
    return user_info


profile = build_profile(first_name="Kamrul", last_name="Hasan", location="Dhaka", field="CSE", hobby="Coding, Gaming")
print(profile)

