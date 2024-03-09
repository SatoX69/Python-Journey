name = input("May I know your name? ")
name = name.strip()
age = input("May I know your age? ")
message = f"Hello {name}"

if int(age) >= 18:
    message += "\nYou are an Adult"
elif int(age) < 18:
    message += "\nYou are a Minor"

print(message)