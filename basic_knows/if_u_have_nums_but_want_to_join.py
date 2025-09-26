nums = [1, 2, 3]
# " ".join(nums)  → ❌ TypeError
print(" ".join(map(str, nums)))  # ✅ "1 2 3"
