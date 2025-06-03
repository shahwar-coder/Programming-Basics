'''
- list[start:stop:step]
- start: slice startes (inclusive)
- stop: slice ends (exclusive) 
- step: interval or stride
'''

# Level 1: Basic
lst=[1,2,3,4,5,6,7]
print(lst[:4]) # [1, 2, 3, 4]
print(lst[0:4]) # [1, 2, 3, 4]
print(lst[1:4]) # [2, 3, 4]
print(lst[4:4]) # []
print(lst[4:]) # [5,6,7]


# Level 2: Stride
print(lst[::2]) # [1, 3, 5, 7]
print(lst[1::2]) # [2, 4, 6]


# Level 3: Last Element/ Second Last Element
print(lst[-1]) # 7
print(lst[-2]) # 6


# Level 4: Slice Backwards using negative values in start/stop/step
print(lst[-4:]) # [4,5,6,7]
print(lst[-4:-1]) # [4,5,6]
print(lst[-4:-2]) # [4,5]
print(lst[-4:-3]) # [4]
print(lst[-4:-4]) # []


# Level 5: Reverse a List
print(lst[::-1]) # [7, 6, 5, 4, 3, 2, 1]


# Level 6: Shallow Copy
copy=lst[:]
print(copy) # [1, 2, 3, 4, 5, 6, 7]


# Level 7: Edge Cases:
# a. Start Exceeds
print(lst[100:]) # [] ,empty

# b. Stop Exceeds
print(lst[:100]) # [1, 2, 3, 4, 5, 6, 7]

# c. Start > Stop
print(lst[3:1]) # [], empty

# d. Start > Stop (but with negative/backward stride)
print(lst[3:1:-1]) # [4, 3]


# Level 8: reversed and stepped with different values.
print(lst[::-1])
print(lst[::-2])
print(lst[::-3])
print(lst[::-4])
print(lst[::-5])
print(lst[::-6])
print(lst[::-7])

'''
Outputs:
[7, 6, 5, 4, 3, 2, 1]
[7, 5, 3, 1]
[7, 4, 1]
[7, 3]
[7, 2]
[7, 1]
[7]
'''
