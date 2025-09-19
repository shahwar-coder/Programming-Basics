'''
1. Remove First Occurrence
Task:
Given a list of integers nums and a target value x, remove the first occurrence of x from nums using remove(). If x is not present, catch the exception and return the list unchanged.

Goal:
Practice basic use of list.remove() and handling a missing-value ValueError.

# Example 1
nums = [1, 2, 3, 2, 4]
x = 2
# After removal: [1, 3, 2, 4]

# Example 2
nums = [5, 6, 7]
x = 10
# After removal attempt: [5, 6, 7]  (no change, no error)

# Example 3
nums = []
x = 1
# After removal attempt: []  (no change)
'''
from typing import List
def removal_of_x(nums: List[int], x: int)->List[int]:
    try:
        nums.remove(x)
        return nums
    except ValueError:
        return nums # as expected, returning unchanged list, not error message

def main():
    nums=[1,2,3,2,4]
    x=2

    # nums = [5, 6, 7]
    # x = 10

    # nums = []
    # x = 1
    print(removal_of_x(nums, x))

if __name__=="__main__":
    main()
