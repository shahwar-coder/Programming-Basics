'''
Set bits = number of 1's in binary form of the number
Below is an example code having function 'countSetBits' which uses 'bit_count()' # faster than counter or normal loops.
'''

from collections import Counter
class Solution:
    def isPrime(self,n: int)->bool:
        """
        Check if number prime or not
        """
        if n<=1:
            return False
        for i in range(2, n):
            if n%i==0:
                return False
        return True

    def countSetBits(self, n: int)->int:
        """
        Count total 1's in bin form of the number : Total set bits
        """
        return n.bit_count()     


    def countPrimeSetBits(self, left: int, right: int) -> int:
        """
        Count Prime Set Bits
        """
        if left>right:
            return 0
        count=0
        for number in range(left, right+1):
            if self.isPrime(self.countSetBits(number)):
                count+=1
        return count
