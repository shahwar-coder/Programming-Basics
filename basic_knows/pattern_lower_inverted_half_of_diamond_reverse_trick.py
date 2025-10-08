'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

    * 
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *

Print the pattern in the function given to you.
'''

class Solution:
    def pattern9(self, n):
        for i in range(1, n+1):
            print(' '*(n-i) + '*'*(2*i-1))
        for i in range(n, 0, -1):
            print(' '*(n-i) + '*'*(2*i-1))

# IMPORTANT : ====>>>> Just write the same loop only reverse.


'''
Here in the middle the lines repeat, if the lines you want NOT to repeat, you can simply do a 'minus 1' from n in second loop.
'''
class Solution:
    def pattern9(self, n):
        for i in range(1, n+1):
            print(' '*(n-i) + '*'*(2*i-1))
        for i in range(n-1, 0, -1):
            print(' '*(n-i) + '*'*(2*i-1))
          
