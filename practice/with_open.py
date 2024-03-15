with open("example.txt") as file:
  x = file.read()
  print(x)


# open can have 2 args, w, r+, a, r

with open("example.txt", "w") as file:
  file.write("Overwrite File")
  
"""
w for writeable,
r+ for read and write
a for append
r for read (default if not provided)
"""