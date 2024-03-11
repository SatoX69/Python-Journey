# Positional function arguments

def greet():
    print("Hello")
    
greet()

def log(arg):
    print(arg)
    
log("Hello World")

# Or we can add a default value

def log(arg=None):
    print(arg)
    
log() # Logs None if no argument is provided


# Keyword function arguments

def register(name, age, sex=''):
    message = f"{name.title()} is {age} years old"
    if sex.lower() == "male":
        message += "\nTheir pronouns are He/Him"
    elif sex.lower() == "female":
        message += "\nTheir pronouns are She/Her"
    else:
        message += "\nThey would rather not specify their gender"
    print(message)
    
"""
We can do either this:

register("Andrew", 17, "male")

Or this:"""

register(age=16, sex="female", name="Sarah")
# The argument order doesn't matter since we explicitly set the receiving keyword


# Return Values

def sum(n1=None, n2=None):
    return n1 + n2
    
calculate = sum(5, 5)
print(calculate)