'''
Q. How can space complexity be reduced?
Ans:
✅ Reuse variables instead of creating new ones.  
✅ Prefer in-place algorithms.  
✅ Use generators/yield instead of lists for large data.  
✅ Avoid deep recursion when possible.
'''
# Example of space-efficient design
def square_in_place(arr):
    for i in range(len(arr)):
        arr[i] *= arr[i]
    return arr
# No extra list → O(1) auxiliary space
