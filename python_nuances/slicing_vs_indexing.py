'''
Q. What’s the difference between slicing and indexing safety-wise?
Ans:
- **Indexing**: error if out of range  
- **Slicing**: safely returns empty string if range is invalid
'''
# Example
s = "abc"
print(s[1:10])  # "bc" (safe)
# print(s[10])  # IndexError
