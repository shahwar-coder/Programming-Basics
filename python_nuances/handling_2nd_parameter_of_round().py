'''
Q. How does round() handle the ndigits parameter?
Ans:
- Positive ndigits → round to that many decimals.  
- Negative ndigits → round to tens, hundreds, etc.
'''
# ✅ Positive ndigits → rounds to decimal places
print(round(3.14159, 2))   # 3.14
print(round(9.8765, 3))    # 9.877
print(round(12.3456, 0))   # 12.0   → 0 decimals

# ✅ Negative ndigits → rounds to tens, hundreds, thousands
print(round(1234, -1))     # 1230   → nearest 10
print(round(1234, -2))     # 1200   → nearest 100
print(round(67890, -3))    # 68000  → nearest 1000

# ✅ Edge and nuance cases
print(round(25, -1))       # 30     → halfway rounds to even (Banker’s rounding)
print(round(2.675, 2))     # 2.67   → floating-point precision effect
print(round(2.675, -2))    # 0.0    → rounds to nearest 100 (2.675 < 50 → 0)
