import random
import json
import time

def initiate():
    user = input("Write your UserID: ")
    x = register(code=user)
    if x is None:
        print("Checking the DataBase")
        time.sleep(3)
        print("UserID not available in DB")
        time.sleep(3)
        print("Registering a new instance")
        time.sleep(2)
        name = input("Enter your name: ")
        while not name:
            name = input("Enter your name: ")
        print("...")
        time.sleep(2)
        num = random.randint(111, 222) ** 3 + 100
        register(name=name, code=num, first=True)
    else:
        print("Checking the DataBase")
        time.sleep(3)
        print(f"Hello {x}")

def register(name=None, code=None, first=False):
    if first:
        new_data = {f"{code}": name}
        with open("user.json") as file:
            content = json.load(file)
        content.update(new_data)
        with open("user.json", "w") as file:
            json.dump(content, file)
        print(f"Hello {name}, Your ID is {code}")
    else:
        with open("user.json") as file:
            content = json.load(file)
            if code not in content:
                return None
            else:
                return content[code]

initiate()