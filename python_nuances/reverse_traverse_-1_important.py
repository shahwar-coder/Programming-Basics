"""
Reverse range() in Python
-------------------------

🔹 range(start, stop, step) includes 'start' but EXCLUDES 'stop'.
🔹 For reverse traversal down to index 0:
       range(len(nums) - 2, -1, -1)
   → 'stop = -1' ensures loop includes index 0.
"""

nums = [1, 2, 3, 4]
n = len(nums)
rightSum = [0] * n

for i in range(n - 2, -1, -1):
    rightSum[i] = rightSum[i + 1] + nums[i + 1]

print(rightSum)  # [9, 7, 4, 0]
