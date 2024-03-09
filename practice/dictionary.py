# JSON

registrar = {
    "name": "Andrew",
    "age": 16,
    "nationality": "German",
    "ageIssue": None
}

print(registrar)
registrar["sex"] = "male"

if registrar['age'] < 18:
    registrar['ageIssue'] = "Too young"
    
print(registrar)

del registrar['ageIssue']

item = registrar.get("age" , "Age not provided") # Second argument here is the default false value if "age" doesn't exists, if no secondary args is provided, it will get None value



array = {
    "Ben": "Beef Wellington",
    "Anthony": "Sushi",
    "Sarah": "Baklava",
    "Johnson": "Fried Chicken"
    }
    
for name, fav in array.items(): # Gets both Keys and Its values
    print(f"{name.title()} likes {fav.title()}")
    
for key in array.keys():
  print(key) #Default behavior, keys() isn't needed necessarily
  
for key in array.values():
  print(key) # Opposite of keys(), gets the values from the dict
  

array = {
    "Ben": "Beef Wellington",
    "Anthony": "Sushi",
    "Sarah": "Baklava",
    "Johnson": "Chicken",
    "Johnson": "Lamb",
    "Johnson": "Cat" # The other Johnsons get omitted
    }
    
for x in set(sorted(array)):
    print(x)
    
set_ = { "Ben", "Jamal", "Ben", "Ben", "Tate", "Walt", "Ben", "Jackson" }

print(set_) # Inline Set

print(array)