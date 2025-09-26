'''
Q. How is join() the reverse of split()?
Ans:
- split() breaks a string into a list.
- join() stitches it back together.

Example:
'''
s = "a-b-c"
parts = s.split("-")        # ['a', 'b', 'c']
rejoined = "-".join(parts)  # 'a-b-c'
