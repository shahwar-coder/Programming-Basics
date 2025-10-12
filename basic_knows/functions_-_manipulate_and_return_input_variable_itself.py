'''
258. Add Digits:
https://leetcode.com/problems/add-digits/

-> Add digits until single digit
'''

class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            num=sum(map(int, list(str(num))))
        return num
