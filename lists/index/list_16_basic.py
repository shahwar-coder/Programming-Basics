'''
3. 🧩 Dynamic Search Target
Task:
Given a list of animals and a variable target_animal, return the index where it first occurs.
If it's not found, return "No such animal".

# Example
animals = ['cat', 'dog', 'rabbit', 'dog']
target_animal = 'dog'
# Output: 1

# Example
target_animal = 'lion'
# Output: "No such animal"
'''
from typing import List, Union
def first_animal_index(animals: List[str], target_animal: str)->Union[int,str]:
    """
    Return the first instance/index of the target animal
    """
    try:
        return animals.index(target_animal)
    except ValueError:
        return "No such animal"

def main():
    animals = ['cat', 'dog', 'rabbit', 'dog']
    target_animal = 'dog'
    print(first_animal_index(animals, target_animal))

if __name__=="__main__":
    main()
