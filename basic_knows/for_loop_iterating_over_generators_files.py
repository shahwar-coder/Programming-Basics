'''
Q12. Can for loops iterate over generators or files?
Ans:
Yes! For loops work with any object that follows the *iterator protocol*,  
including generators, files, and custom iterable classes.
'''
# Example
def gen():
    for i in range(3):
        yield i

for val in gen():
    print(val)  # 0 1 2

with open("sample.txt") as f:
    for line in f:
        print(line.strip())
