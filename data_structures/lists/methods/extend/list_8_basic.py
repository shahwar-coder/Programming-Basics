'''
2. Merge Two Lists (BUT RETURN A NEW LIST THIS TIME) # Aiming to preserve 'a'
Task:
Given two lists of integers, a and b, produce a new list c that starts as a copy of a and then extends with all elements of b.

Goal:
Practice using extend() to concatenate two lists in place.

# Example 1
a = [1, 2, 3]
b = [4, 5]
# After merging: c = [1, 2, 3, 4, 5]

# Example 2
a = []
b = [10, 20, 30]
# After merging: c = [10, 20, 30]

# Example 3
a = [7, 8]
b = []
# After merging: c = [7, 8]
'''

from typing import List
def extending(a: List[int], b: List[int])->List[int]:
    """
    Return an extened a with b.
    """
    c=a.copy() #to preserve 'a' , # 'c' as we wanted to return a new list altogether. 
    c.extend(b) #do not return directing while oprating, this is wrong : return c.extend(b)
    return c #instead return the original list which is now mutated

def main():
    a = [1, 2, 3]
    b = [4, 5] 
    print(extending(a,b))

if __name__=="__main__":
    main()
