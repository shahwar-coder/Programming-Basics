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


'''
Q. Why is using == unsafe for float comparison?
Ans:
Because floating-point arithmetic introduces microscopic errors —  
so two logically equal results may differ by 1e-16 or less.
'''
# Example
x = 0.3
y = 0.1 + 0.2
print(x == y)         # False
print(math.isclose(x, y))  # True
