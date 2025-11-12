"""
Reverse a String (In-place)

Task:
Reverse a string represented as a list of characters 's'.

Requirements:
- Reverse the list in place using O(1) extra memory.
- Do not return anything; modify the given list directly.

Examples:
Input:  s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Input:  s = ["b","y","e"]
Output: ["e","y","b"]
"""

class Solution: 
    def reverseString(self, s):
        s.reverse()
        # As much as we would naturally want to return something,
        # here we don’t need to — the list 's' is modified in place.
        # LeetCode checks the mutated list directly, not the return value.
