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