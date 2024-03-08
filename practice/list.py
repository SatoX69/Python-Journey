# List
array = ["Asia", "North America", "South America", "Africa", "Washington DC", "Berlin"]

# Print the original array
print(array)

# Log the array in alphabetical order without modifying the actual values
print(sorted(array))

# Additionally, include `reverse` to sort it in alphabetical order backwards
# print(sorted(array, reverse=True))

# Permanently change the order of items in the array in alphabetical order
array.sort()  # Can include `reverse=True` here too
print(array)

# Array methods and stuff
new_value = array[2]
print(new_value)  # Output: South America

array[2] = "Tokyo"
print(array[2])  # Output: "Tokyo"

# Modifying the array
array.append("London")  # Append London at the end
array.insert(2, "Toronto")  # Inserts Toronto at position 2
array.pop()  # Pops the last item of the array and can additionally take an index param to pop that item
value = array.pop()  # Gets the value of the last item in the array and can additionally take an index param to get the item at that index
# Note: The variable declared `pop()` is a little different from the undeclared explicit `pop()` since it doesn't actually pop the last item but instead gets the value of the last or provided index item
array.remove("Asia")  # Removes the provided item (Only the first occurrence)
array.reverse()  # Reverses the array backwards

# Misc
print(len(array))  # Prints the length of the array

# Slicing Syntax
people = ["Donald", "Biden", "Obama", "Churchill", "Lincoln", "Jovan", "TJ"]
print(people[1:5]) # Biden - Lincoln
print(people[:3]) # Start - Obama
print(people[4:]) # Churchill - End

# Copying Syntax
my_figures = ["Micheal Jackson", "Davidson", "Jesus"]
print(f"I know {my_figures}")
friend_likings = my_figures[:]
friend_likings.append("Walter White")
print(f"My friend loves {friend_likings}")