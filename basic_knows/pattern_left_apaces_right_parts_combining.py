'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

1        1
12      21
123    321
1234  4321
1234554321

Print the pattern in the function given to you.
'''

class Solution:
    def pattern12(self, n):
        for i in range(1, n+1):
            left = "".join(str(j) for j in range(1, i+1))
            spaces = " " * (2*n-2*i)
            right = "".join(str(j) for j in range(i, 0, -1))
            print(left + spaces + right)


'''
Step-by-step explanation:

1️⃣ For each row i (1 → n):
   - Left half: "1..i"
   - Middle spaces: (2*n − 2*i)
   - Right half: "i..1"

2️⃣ Example for n=5:
   Row 1: left="1", spaces=8, right="1"       → 1        1
   Row 2: left="12", spaces=6, right="21"     → 12      21
   Row 3: left="123", spaces=4, right="321"   → 123    321
   Row 4: left="1234", spaces=2, right="4321" → 1234  4321
   Row 5: left="12345", spaces=0, right="54321" → 1234554321
'''
