'''
Q1. What does the min() function do in Python?
Ans:
`min()` returns the **smallest element** from a group of values or from an iterable.  
It can also take a `key` to customize comparisons.
'''
# Example
print(min(3, 1, 2))        # 1
print(min([10, 5, 8]))     # 5
print(min((9, 2, 7)))      # 2



'''
Q2. What are the two main ways to use min()?
Ans:
1️⃣ Iterable form → `min([values])`  
2️⃣ Multiple arguments form → `min(a, b, c, ...)`
'''
# Example
print(min([5, 2, 9]))    # 2
print(min(7, 3, 8))      # 3



'''
Q3. How does min() work with strings?
Ans:
For strings, it compares **lexicographically** (alphabetically),  
based on Unicode code points.
'''
# Example
print(min("Python"))                   # 'P'
# | Character | Unicode (`ord()`) |
# | --------- | ----------------- |
# | P         | 80                |
# | y         | 121               |
# | t         | 116               |
# | h         | 104               |
# | o         | 111               |
# | n         | 110               |
print(min(["banana", "apple"]))        # 'apple'



'''
Q4. What is the purpose of the key parameter in min()?
Ans:
The `key` parameter lets you define a **function** to customize how elements are compared.
'''
# Example
words = ["banana", "apple", "cherry"]
print(min(words, key=len))   # 'apple' (shortest word)

nums = [-10, -5, 3, 8]
print(min(nums, key=abs))    # 3 (smallest by absolute value)



'''
Q5. What does the default parameter do?
Ans:
If the iterable is empty, `default` provides a fallback value instead of raising a `ValueError`.
'''
# Example
print(min([], default=0))   # 0



'''
Q6. How does min() behave with nested structures like tuples or lists?
Ans:
For tuples/lists, Python compares elements **position-wise** (lexicographically).  
To compare inner values, use a `key` function.
'''
# Example
pairs = [(2, 5), (1, 9), (3, 1)]
print(min(pairs))                         # (1, 9) → smallest first element
print(min(pairs, key=lambda x: x[1]))     # (3, 1) → smallest second element



'''
Q7. What happens if elements are of mixed data types?
Ans:
`min()` **cannot compare** incompatible data types (like int and str) —  
it raises a `TypeError`.
'''
# Example
# min([1, 'a', 3])  # ❌ TypeError



'''
Q8. How does min() behave with dictionaries?
Ans:
By default, it compares **keys** of the dictionary.  
You can compare **values** using `key=dict.get`.
'''
# Example
scores = {'Ali': 85, 'Zara': 92, 'Hamid': 75}
print(min(scores))                    # 'Ali' (alphabetically smallest key)
print(min(scores, key=scores.get))    # 'Hamid' (lowest score)



'''
Q9. What’s the time complexity of min()?
Ans:
It performs **O(n)** comparisons — efficient and implemented in **C** for speed.  
The `key` function doesn’t change the complexity.
'''



'''
Q10. When is min() especially useful?
Ans:
✅ Selecting smallest item based on a property  
✅ Finding minimum by custom metric (length, abs, score, etc.)  
✅ Avoiding errors in empty lists with `default`
'''
