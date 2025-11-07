'''
Q6. How accurate is as_integer_ratio()?
Ans:
It’s exact — it converts the binary representation into an exact rational form.  
Even repeating decimals like 0.1 get a long but precise ratio.
'''

# Example
print((0.1).as_integer_ratio())  
# (3602879701896397, 36028797018963968)
