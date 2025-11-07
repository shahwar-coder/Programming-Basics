'''
Q. How does int() handle whitespace or signs in strings?
Ans:
It ignores leading/trailing spaces and recognizes `+` or `-` signs.
'''
# Example
print(int("   +42  "))  # 42
print(int("-99"))        # -99
