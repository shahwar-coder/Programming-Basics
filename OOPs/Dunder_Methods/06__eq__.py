'''NOTE-1
__eq__ : Defines how == works

In Python, equality isn't always a direct memory comparision.
The default behaviour might check for memory location for some types.
But you can override that with __eq__ method
This __eq__ method defines your business logic for equality, allowing you to decide -
how two objects should be considered equal based on their values or properties, not just their memory location
'''

'''NOTE-2
Primitive types like int, str, float, often have their equality checked by value.
However for custom objects created with classes, the __eq__ method might just check the memory location unless we define otherwise.
'''

class User:
  def __init__(self, id: int, email: str)->None:
    self.id = id
    self.email = email

  def __eq__(self, other):
    if not isinstance(other, User):
      return NotImplemented
    return self.id == other.id

User(1, "a@mail.com") == User(1, "b@mail.com")
# True
    
