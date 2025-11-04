import math
class Solution:
    def countDigit(self, n):
        if n==0:
            return 1
        return int(math.log10(abs(n))) + 1
