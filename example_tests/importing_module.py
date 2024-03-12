import function_2
# from function_2 import registrar, code
# from function_2 import registrar as register
# from function_2 import * (Imports all functions) and they will get implicitly defined

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
