class Human:
    def __init__(self, name, age=0):
      """
      __init___(self)
      init is the keyword for constructor and the provided self param is the keyword for referencing to its own self on the corresponding instance
      """
        self.name = name.title()
        self._age = int(age)
        self.mood = "Neutral"
    
    def increment_age(self):
        if self._age is not None:
            self._age += 1
            
    def mind(self, feel):
        if not feel:
            self.mood = "Neutral"
        else:
            self.mood = feel
    def checkAge(self):
        if self._age < 18:
            return "a minor"
        else:
            return "an adult"            
    def status(self):
        return f"{self.name} is {self._age} years old.\nHe is feeling {self.mood}\nHe is {self.checkAge()}"

man = Human("Jamal", 3)
man.increment_age()
print(man._age)

for x in range(0, 11):
    man.increment_age()

print(man._age)
print(man.status())

for x in range(0, 19):
    man.increment_age()

man.mind("Sad")
print(man.status())
man.increment_age()
print(man.status())