'''
__repr__ --> controls how objects looks when:
printed
logged
inspected in debugger
'''

class User:
  def __init__(id, name):
    self.id = id
    self.name = name

  def __repr__(self):
    return f"User(id={self.id}, name={self.name})"

print(User(1, "Rahul"))
# User(id=1, name=Rahul)

# So basically this is how I wanted the object to look, when I print etc.
# Helpful, otherwise it will be painful debugging.
