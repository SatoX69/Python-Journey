import function_2

x = function_2.registrar("Joe", "Biden", field="Clown", occupation="President", age= '> 50')
print(x)
x = function_2.code(999, "User_10", "User_20", "User_30")
print(x)


"""
Or we can write:
import function_2 as process

x = process.registrar("Joe", "Biden", field="Clown", occupation="President", age= '> 50')
print(x)
x = process.code(999, "User_10", "User_20", "User_30")
print(x)

Here the module is imported with the name "process"
"""
