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