try:
  print(5/0) # Throws division error
except ZeroDivisionError as x: # This will look for this exact error if it catches error else it will print the entire error instead of debugging it here in this block

  print(x) # error.message
  
# Suppose we want to handle undefined errors:

try:
  V() # V is not defined
  print(5/0) # ZeroDivisionError
except Exception as x:
  """
  If we define the V function then it will catch the ZeroDivisionError error else it will catch the V is not defined error and print just the error message
  """
  print(x)