'''
Q1. What does the max() function do in Python?
Ans:
`max()` returns the **largest element** from a group of values or from an iterable.  
It can also take a `key` to customize how comparisons are made.
'''
# Example
print(max(3, 1, 2))        # 3
print(max([10, 5, 8]))     # 10
print(max((9, 2, 7)))      # 9



'''
Q2. What are the two main ways to use max()?
Ans:
1️⃣ Iterable form → `max([values])`  
2️⃣ Multiple arguments form → `max(a, b, c, ...)`
'''
# Example
print(max([5, 2, 9]))    # 9
print(max(7, 3, 8))      # 8



'''
Q3. How does max() work with strings?
Ans:
For strings, `max()` compares **lexicographically** (alphabetically)  
using Unicode code points.
'''
# Example
print(max("Python"))                 # 'y'
print(max(["banana", "apple"]))      # 'banana'



'''
Q4. What is the purpose of the key parameter in max()?
Ans:
The `key` parameter lets you define a **function** to decide 
how elements should be compared.
'''
# Example
words = ["banana", "apple", "cherry"]
print(max(words, key=len))   # 'banana' (longest word)

nums = [-10, -5, 3, 8]
print(max(nums, key=abs))    # -10 (largest absolute value)



'''
Q5. What does the default parameter do?
Ans:
If the iterable is empty, `default` provides a fallback value instead of raising a `ValueError`.
'''
# Example
print(max([], default="No data"))   # "No data"



'''
Q6. How does max() behave with nested structures like tuples or lists?
Ans:
For tuples/lists, Python compares **element by element** (lexicographically).  
To compare based on a specific inner value, use a `key` function.
'''
# Example
pairs = [(2, 5), (1, 9), (3, 1)]
print(max(pairs))                         # (3, 1) → compares first elements
print(max(pairs, key=lambda x: x[1]))     # (1, 9) → compares second elements


'''
Q7. What happens if elements are of mixed data types?
Ans:
`max()` **cannot compare** incompatible types (like int and str) —  
it raises a `TypeError`.
'''
# Example
# max([1, 'a', 3])  # ❌ TypeError



'''
Q8. How does max() behave with dictionaries?
Ans:
By default, it compares **keys** of the dictionary.  
You can compare **values** using `key=dict.get`.
'''
# Example
scores = {'Ali': 85, 'Zara': 92, 'Hamid': 75}
print(max(scores))                    # 'Zara' (alphabetically last key)
print(max(scores, key=scores.get))    # 'Zara' (highest score)



'''
Q9. What’s the time complexity of max()?
Ans:
It performs **O(n)** comparisons — efficient and implemented in **C** for speed.  
The `key` function does not change complexity.
'''



'''
Q10. When is max() especially useful?
Ans:
✅ Finding the largest item based on a property  
✅ Selecting maximum values by custom metric (length, abs, score, etc.)  
✅ Avoiding errors in empty lists with `default`
'''
