'''
3. Reverse a List Using Stack (pop)
Task:
Use a loop and pop() to reverse a list by popping elements off one list and appending to another.

Goal:
Simulate stack behavior and understand how popping reverses order.

# Example 1
original = [10, 20, 30]
# Output: [30, 20, 10]

# Example 2
original = []
# Output: []
'''
from typing import List, TypeVar
T=TypeVar('T')

def simulate_stack(original: List[T])->List[T]:
    """
    Return reverse of the list (pop and loop to be used to simulate stack)
    """
    the_reversed=[]
    while original: # in case you want to preserve the original, you can use temp=original.copy()
        the_reversed.append(original.pop())
    return the_reversed

def main():
    original=[10,20,30]
    print(simulate_stack(original))

if __name__=="__main__":
    main()
