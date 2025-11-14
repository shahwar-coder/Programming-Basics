'''
Check if Array is Sorted.
'''

# COPY OF ARRAY NOT RQUIRED (as not manipulated)
class Solution:
    def arraySortedOrNot(self, arr, n):
        if sorted(arr) == arr:
            return True
        else:
            return False

# sorted(arr) does NOT mutate arr — it returns a new sorted list.
