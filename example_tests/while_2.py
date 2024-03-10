people = ["Jamal", "jamal", "jamal", "Andrew", "tate", "ben", "jamal", "tate", "sarah"]

index = 0
while index < len(people):
    current_name = people[index]
    people.pop(index)
    people.insert(index, current_name.title())
    index += 1

while 'jamal' in people:
    people.remove('jamal')

print(people)