number = 0

while number <= 5:
    print(number)
    number += 1
    
message = ""

while message != "exit":
    message = input("Say anything ")
    if message == "exit":
        print("Exiting the loop")
    else:    
        print(message)
        
# Or we can use Flag and break

message = True

while message:
    message = input("Type something ")
    if message.lower() == "exit":
        break # Breaks out of any loop
    else:
        print(message)

digit = 0

while True:
    if digit >= 10:
        break
    if digit % 2 == 0: # Modulo Operator
        digit += 1
        continue # Starts the loop from the beginning again
    print(digit)
    digit += 1