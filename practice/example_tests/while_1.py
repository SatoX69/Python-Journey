jobless = ["Prashant", "Ben", "Sarah", "Lewis", "David"]
employed = []

for employee in employed:
  # This loop won't work since employed list is empty
    print(f"{employee.title()} is Employed")

while jobless:
    user = jobless.pop()
    print(f"Employing {user.title()}")
    employed.append(user.title())
    
for employee in employed:
    print(f"{employee.title()} is Employed")