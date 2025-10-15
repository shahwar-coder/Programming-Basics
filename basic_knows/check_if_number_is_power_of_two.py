'''
To check if number is power of two.
Bit manipulation 'power'
'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
      return n>0 and (n & (n-1))==0
