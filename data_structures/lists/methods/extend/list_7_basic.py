'''
1. Merge Two Lists
Task:
Given two lists of integers, a and b, produce a new list c that starts as a copy of a and then extends with all elements of b.

Goal:
Practice using extend() to concatenate two lists in place.

# Example 1
a = [1, 2, 3]
b = [4, 5]
# After merging: = [1, 2, 3, 4, 5]

'''
from typing import List
def extending(a: List[int], b: List[int])->List[int]:
    """
    Return an extened a with b.
    """
    a.extend(b) #do not return directing while oprating, this is wrong : return a.extend(b)
    return a #instead return the original list which is now mutated

def main():
    a = [1, 2, 3]
    b = [4, 5] 
    print(extending(a,b))

if __name__=="__main__":
    main()
