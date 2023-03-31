"""Module – Module or library is a file that contains definitions of several functions, classes, variables, etc.,
which is written by someone else for us to use. Pip – Pip is a package manager for Python, i.e., pip command can be
used to download any external module in Python."""

import utils.new_module as module
from calculator_102 import Calculator
module.greeting()


# PIP is a package manager for Python packages, or modules if you like.
# https://pypi.org/project/pip/
# Run your project directory terminal pip install --upgrade pip

calculator = Calculator()
print(calculator.value)

calculator.add(50)
print(calculator.value)

calculator.multiply(2)
print(calculator.value)