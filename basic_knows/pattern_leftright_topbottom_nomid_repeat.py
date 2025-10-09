'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *

Print the pattern in the function given to you.
'''

class Solution:
    def pattern20(self, n):
        for i in range(1, n+1):
            left='*'*i
            spaces=' '*2*(n-i)
            right='*'*i
            print(left + spaces + right)
        for i in range(n-1, 0, -1):
            left='*'*i
            spaces=' '*2*(n-i)
            right='*'*i
            print(left + spaces + right)

'''
Step-by-step explanation:

1️⃣ The pattern is symmetric about the middle line.

2️⃣ For the top half (1 → n):
      - Left stars increase by 1 each row.
      - Spaces decrease by 2 each row.
      - Right stars mirror the left.

3️⃣ For the bottom half (n-1 → 1):
      - Reverse the logic — stars decrease and spaces increase.

Example (n=5):
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
'''

