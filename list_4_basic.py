'''
APPEND
'''

'''
1. Build a List of Squares
Task:
Given a positive integer n, create a list of the squares of all integers from 1 to n (inclusive) by repeatedly using append().

Goal:
Practice looping and appending new elements to a list.

# Example 1
n = 5
# You should produce: [1, 4, 9, 16, 25]

# Example 2
n = 1
# You should produce: [1]

# Example 3
n = 0
# You should produce: []

'''
from typing import List
def square_them(n: int)->List[int]:
    """
    Return a list of squares from 1^2 to n62
    """
    squares=[]
    for i in range(1,n+1):
        squares.append(i**2)
    return squares

def main():
    n=5
    print(square_them(n))

if __name__=="__main__":
    main()
