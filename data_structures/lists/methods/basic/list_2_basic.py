'''
Accessing elemets :
1> Indexing
2> Slicing
'''

# Indexing:
nums=[1,2,3,4,5]
print(nums[0])
print(nums[-1])
a = nums[1],nums[2]
print(f"a = {a} , Type of a : {type(a)}")

# Slicing:
a=nums[1:]
print("a : ", a)

b=nums[1:3]
print("b : ", b)

c=nums[:]
print("c : ", c)

d=nums[::]
print("d : ", d)

e=nums[::2]
print("e : ", e)

f=nums[::-1] # also reversing #important
print("f : ", f)
