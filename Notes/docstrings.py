# docstrings are used to document the code when creating a function
# docstrings are surrounded by triple quotes


def add(a, b):
    """
    This function adds two numbers

    Args:
        a (int): The first number
        b (int): The second number
    """
    return a + b


# to access the docstring use the __doc__ method to update programmatically
print(add.__doc__)
# prints "This function adds two numbers"
