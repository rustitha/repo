# A simple Python program by your 'bro' 🐍

# 1. Variables and Data Types
# Think of variables as labeled boxes for storing data.
# Python doesn't need you to specify the data type, it figures it out.

# An integer (whole number)
age = 25

# A string (text)
name = "Charlie"

# A float (number with a decimal)
pi = 3.14159

# A boolean (True or False)
is_student = True

# 2. Printing to the console
# The `print()` function is your best friend for seeing what's happening.
print("Hey there, my name is", name, "and I'm", age, "years old.")
print("The value of pi is:", pi)
print("Is Charlie a student?", is_student)

# 3. Basic Arithmetic
# You can do math with your variables.
# The result is stored in a new variable.
year_born = 2025 - age
print("So, I was probably born in the year", year_born, "!")

# 4. A simple function
# A function is a block of code that does a specific task.
# Use `def` to define it.
def say_hello(person_name):
    # This function takes one argument, `person_name`, and prints a greeting.
    print(f"What's up, {person_name}!")

# Call the function with our `name` variable.
say_hello(name)

# 5. User Input
# Ask the user for some information and store it in a variable.
user_city = input("Where are you from? ")
print(f"Nice! I've heard {user_city} is a cool place.")
