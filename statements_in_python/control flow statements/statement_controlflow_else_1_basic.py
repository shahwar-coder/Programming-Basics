'''
- else
- control flow statement
- else defines a "fallback block" is to come
- runs only when none of the previous if/elif conditions are True

example:
age = 10

if age > 18:
    print("Adult")
elif age > 12:
    print("Teen")
else:
    print("Child")

- Only 1 else is allowed per if chain
- And it must be the last block

'''

# Simple Example
age=23
if age > 18:
    print("Adult")
elif age > 12:
    print("Teen")
else:
    print("Child")

# Else Taboo : 'else' with for / while loops

'''
- lesser known but very powerful
- Let's see an Example: "Searching"
'''

def find_target(nums, target):
    for n in nums:
        if n == target:
            print("Found!")
            break
    else:
        print("Not found.")  # only runs if target was never matched

