'''
1. Check Exact Frequency
Task:
Write a function that takes a list of integers nums and an integer k, and returns True if any element in nums appears exactly k times. Otherwise, return False. Use count() to determine frequencies.

Goal:
Practice using count() to check for a specific frequency.

# Example 1
nums = [1, 2, 2, 3, 2, 4]
k = 3
# 2 appears exactly 3 times, so output: True

# Example 2
nums = [5, 5, 5, 5]
k = 2
# No element appears exactly twice; output: False

# Example 3
nums = []
k = 1
# Empty list → nothing can appear once; output: False
'''
from typing import List
def occurrence_check(nums: List[int], k: int)->bool:
    """
    Return True if any element occurs k times in the list, else False 
    """
    for n in set(nums): # instead of just using nums we used set(nums) , so we only check one unique element once.
        if nums.count(n)==k:
            return True
    return False 

    # Note : The solution might be O(n2) so we may need to think of making it more efficient.
    # It can be done through collections : Counter. (Which form frequency list)
    # Check ""list_13.py""

def main():
    nums = [1, 2, 2, 3, 2, 4]
    k = 3
    print(occurrence_check(nums, k))

if __name__=="__main__":
    main()
