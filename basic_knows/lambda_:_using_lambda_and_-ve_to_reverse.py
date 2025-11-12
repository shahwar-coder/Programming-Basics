# Example
nums = [5, 1, 3, 9]
print(sorted(nums, key=lambda x: -x))  # [9, 5, 3, 1]

# • sorted() normally sorts in ascending order.
# • key=lambda x: -x → negates each number before comparison.
# • Negative values reverse the order effectively.
# • Result: sorts in descending order → [9, 5, 3, 1]
