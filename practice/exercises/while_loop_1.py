registry = {}

take_poll = True

while take_poll:
    name = input("Write your name: ")
    age = input("Type your age: ")
    year_of_birth = input("Year of birth: ")
    registry["name"] = name
    registry["age"] = age
    registry["birth_year"] = year_of_birth
    ask = input("Would you like to repeat? (y/n): ")
    if ask.lower() == "y": continue
    elif ask.lower() == "n": break
    else: break
    
print(f'Hello {registry["name"]}!\nI have saved your registry')
print(f'You are {registry["age"]} years old and \nYou were born in {registry["birth_year"]}')