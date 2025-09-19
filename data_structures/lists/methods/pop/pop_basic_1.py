'''
1. Last Element Remover
Task:
Write a function that removes the last element from a list of integers and returns both the updated list and the removed element.

Goal:
Practice using pop() with no index (default: last element).

# Example 1
nums = [1, 2, 3, 4]
# Output: ([1, 2, 3], 4)

# Example 2
nums = [99]
# Output: ([], 99)
'''
from typing import TypeVar, List
T=TypeVar('T') # used when we do not know the type, (using for practise here)
def pop_from_nums(nums: List[T])->tuple[List[T], T]:
    """
    Pop last item from list, and return a tuple containing the updated list and the poped item.
    """
    if not nums:
        raise IndexError("List Empty! hence index problem.")
    return (nums, nums.pop()) # nums: bcz mutated, nums.pop() while operation returning bcz possible

def main():
    try:
        nums=[1,2,3,4]
        # nums=[]
        print(pop_from_nums(nums))
    except IndexError as e:
        print(f"Invalid Input: {e}")

if __name__=="__main__":
    main()
