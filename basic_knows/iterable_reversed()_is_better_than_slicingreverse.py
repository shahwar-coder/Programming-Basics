'''
Q5. Is `reversed()` more efficient than slicing (`[::-1]`) in Python? Why?

Ans:
Yes — **`reversed()` is generally better in terms of memory efficiency**, and its time complexity can also be more optimal depending on the use case.

👉 **Reason:**  
- `reversed(seq)` returns a **reverse iterator**, not a new list or string.  
- `seq[::-1]` creates a **full reversed copy** in memory.

So `reversed()` avoids building a new object and simply iterates over the existing sequence in reverse order.
'''
nums = [1, 2, 3, 4, 5]

# Using reversed()
for n in reversed(nums):
    print(n, end=" ")    # 5 4 3 2 1

# Using slicing
for n in nums[::-1]:
    print(n, end=" ")    # 5 4 3 2 1

'''
| Method          |                    Time Complexity                   | Space Complexity | Description                    |
| :-------------- | :--------------------------------------------------: | :--------------: | :----------------------------- |
| `reversed(seq)` | **O(1)** (to create iterator) + O(n) (when iterated) |     **O(1)**     | Returns iterator; doesn’t copy |
| `seq[::-1]`     |                       **O(n)**                       |     **O(n)**     | Creates a full reversed copy   |
'''
