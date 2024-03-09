vehicles = ["Toyota", "Audi", "bmw", "Civic", "Honda", "Lamborghini"]

for vehicle in vehicles:
    if vehicle.lower() == "bmw":
        print(vehicle.upper())
    else:
        print(vehicle.title())

# Use == for comparison, and convert vehicle to lowercase for case-insensitive check.

if vehicles[2].lower() != "bmw":
    print(False)

age = 18
name = "Ben"
if age < 18:
    print(f"You are not an adult. You are {age} years old.")
else:
    print("You're not an adult.")

if name == "Ben" and age >= 18:
    print("Ben is old enough")

print("bmw" in vehicles)

if "Delta" not in vehicles:
    print("Delta not found")
    
    
    
attractive = True
person_age = 19

if person_age >= 18:
    message = "Smashable"
elif person_age < 18:
    message = "They are a kid"
elif person_age >= 18 and attractive:
    message = "Smash" # Won't work for if-elif syntax
print(message)


# Rectified snippet
if person_age >= 18:
    message = "Smashable"
if person_age < 18:
    message = "They are a kid"
if person_age >= 18 and attractive:
    message = "Smash"
print(message)

# If-elif stops once the conditions are true on the first instance, contrary to theatter snippet which checks for condition and message the message and prints the last overwritten value