'''
Q. What does math.isclose(a, b) do?
Ans:
It checks whether two numbers are **approximately equal**,  
accounting for tiny floating-point errors that occur during calculations.
'''
# Example
import math
print(math.isclose(0.1 + 0.2, 0.3))  # True
print((0.1 + 0.2) == 0.3)            # False (due to rounding)
