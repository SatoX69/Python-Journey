class Parent:
  """
  This is the main parent class
  """
    def __init__(self, name, role="Parent"):
        self._name = name
        self._role = role

x = Parent("Johnson")
print(f"{x._name} is the {x._role}")

class Child(Parent):
  """
  This is the child of the parent class, for this to happen, we need to pass the instance of the parent to the child enclosed in parenthesis
  """
    def __init__(self, name, role):
        super().__init__(name, role)
        # This is the method used for initiating functions or constructor of the parwnt class
    
y = Child("Sarah", "Child")
print(f"{y._name} is the {y._role}")