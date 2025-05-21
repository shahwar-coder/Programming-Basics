'''
#APPEND

3. Running Sum
Task:
Given a list of integers nums, construct a running sum list where the ith element is the sum of nums[0] through nums[i]. Build it by starting with an empty result list and appending each new cumulative total.

Goal:
Combine accumulation with append() to build a prefix-sum list.

# Example 1
nums = [1, 2, 3, 4]
# You should produce: [1, 3, 6, 10]

# Example 2
nums = [5, -2, 7]
# You should produce: [5, 3, 10]

# Example 3
nums = []
# You should produce: []

'''
from typing import List
def running_sum(numbers: List[int])->List[int]:
    total=0
    new_list=[]
    for num in numbers:
        total+=num
        new_list.append(total)
    return new_list

def main():
    numbers=[1,2,3,4,5]
    print(running_sum(numbers))

if __name__=="__main__":
    main()
