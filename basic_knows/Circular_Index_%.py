nums = [10, 20, 30]
n = len(nums)

for i in range(10):  # go beyond list length intentionally
    circular_index = i % n
    print(f"i={i:2} -> index={circular_index} -> value={nums[circular_index]}")

# i= 0 -> index=0 -> value=10
# i= 1 -> index=1 -> value=20
# i= 2 -> index=2 -> value=30
# i= 3 -> index=0 -> value=10
# i= 4 -> index=1 -> value=20
# i= 5 -> index=2 -> value=30
# ...
