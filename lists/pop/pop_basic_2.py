'''
2. Middle Out
Task:
Given a list and an index, remove the element at that index using pop() and return it. If the index is invalid, return "Index out of range".

Goal:
Practice using pop(i) with error handling.

# Example 1
arr = ['a', 'b', 'c', 'd']
index = 2
# Output: 'c', arr becomes ['a', 'b', 'd']

# Example 2
arr = [1]
index = 5
# Output: 'Index out of range'

'''
from typing import List, TypeVar, Union
T=TypeVar('T')
def pop_at_index(arr: List[T], index: int)->Union[T,str]:
    """
    Remove and return the element at `index`. 
    If `index` is out of range, return "Index out of range".
    """
    try:
        return arr.pop(index)
    except IndexError:
        return "Index out of range"

def main():
    arr=['a','b','c','d']
    index=2
    # index=5
    print(pop_at_index(arr, index))


if __name__=="__main__":
    main()
