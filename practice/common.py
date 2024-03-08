#print
name = "Andrew"
print("Pleasure being acquainted " + name)


#f string
string = f"My friend's name is {name}"
print(string)


#data type(s)
integer = 10
string = "10"
floating_point = 10.00
#etc


#methods 1
name_with_space = "  jonathan "
# lstrip, strip, rstrip
name_with_space = name_with_space.strip()
print(name_with_space)


#mwthods 2
# upper(), lower(), title(), capitalize()
name_with_space = name_with_space.title()
# Black space trimmed out
print(f"{name_with_space} is my good friend.")

# Multiple Destructuring
x, y, z = "XYZ" # Each letter is the value of the corresponding variable at its position

x, y, z = ["First", "Second", "Third"]


# For exponents, use 2 asterisks (**)
print(10 ** 2)


# Common methods 1
digits = [0, 3, 1, 7, 8, 5, 4, 9, 12, 17] # And so on
print(max(digits))
print(min(digits))
print(sum(digits))

exp = [x ** 2 for x in range(2, 13)]
print(exp)