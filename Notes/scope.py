##### Global Scope #####
# Global scope is the scope of the main program
CONSTANT = 0
variable = 1

# This is a global variable and can be accessed anywhere in the program but can only be updated in the global scope (outside of functions) or by using the global keyword


##### Local Scope #####
# Local scope is the scope of a function
def function(number):
    # As variable is created inside the function it is local to the function NOT interacting with the global variable
    variable = number
    print(variable)


##### Global Keyword #####
def function2(number):
    # When we use the global keyword we are telling the function to use the global variable instead of creating a new local variable
    global variable
    # As this is now a global variable it will update the global variable
    variable = number
    print(variable)


##### Lexical (enclosing) Scope #####
# Lexical scope is the scope of any part of your code that is enclosed in another part of your code


def function3(number):
    # This is the outer function
    variable = 15

    def function4(number):
        # This is the inner function
        # This function has access to the outer functions variable In Read Only by default
        variable = number
        print(f"Inner variable is {variable}")

    function4(number)
    print(f"Outer/Local variable is {variable}")


##### Nonlocal Keyword #####
# Nonlocal keyword is used to change the scope of a variable to the outer function
def function5(number):
    # Using the Global Variable to show the difference between the two
    global variable
    outer_variable = 10

    def function6(number):
        # This function has access to the outer functions variable In Read Only by default
        # To change the variable in the outer function we use the nonlocal keyword
        nonlocal outer_variable
        outer_variable = number
        print(variable)

    function6(number)
    variable = outer_variable
    print(variable)


##### Example #####

# Print the global variable before anything changes
print("Global Variable Before Function 1")
print(variable)

# Call the function with 10
print("\nFunction 1, updating variable in local scope")
function(10)

# Print the global variable after the function has been called to display no change
print("Global Variable After Function 1")
print(variable)

# Call the function2 with 10
print("\nFunction 2, updating variable in global scope")
function2(10)

# Print the global variable after the function2 has been called to display the change
print("Global Variable After Function 2")
print(variable)

# Call the function3 with 30
print("\nFunction 3, updating variable in lexical scope")
function3(30)

# Print the global variable after the function3 has been called to display the change
print("Global Variable After Function 3")
print(variable)

print(
    "\nFunction 5, updating variable in lexical scope with nonlocal keyword and global variable"
)
function5(50)

# Print the global variable after the function5 has been called to display the change
print("Global Variable After Function 5")
print(variable)
