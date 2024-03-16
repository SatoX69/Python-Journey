# Old file being committed

# Define a set called 'x
x = { "Hello", "World" }  # This is a set

# Define another set called 'y' with values "Africa", "Asia", and "Europe"
y = {"Africa", "Asia", "Europe"}

# Add the string "New" to set 'x'
x.add("New")

# Add the string "Item" to set 'x'
x.add("Item")

# Remove the string "World" from set 'x'
x.remove("World")

# Safely discard the string "World" from set 'x' if it exists (It won't raise error if the item doesn't exist contrary to remove() method)
x.discard("World")


# To merge two sets, use the update method
y.update(x)

# Update set 'x' with the elements of set 'y' using the union method
x.union(y)

# Clear all elements from set 'x'
x.clear()

# Delete set 'x' - This removes the entire variable from memory
del x


""" More methods here:
https://www.w3schools.com/python/python_sets_methods.asp

https://www.w3schools.com/python/python_sets_join.asp
"""