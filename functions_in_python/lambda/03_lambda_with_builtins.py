'''
Q1. Why are lambda functions often used with built-in functions?
Ans:
Because `map()`, `filter()`, and `sorted()` often need **a short, inline function**  
for simple transformations or comparisons — and lambdas are perfect for that.
'''
# Example
nums = [1, 2, 3, 4, 5]
print(list(map(lambda x: x * 2, nums)))  # [2, 4, 6, 8, 10]


'''
Q2. How does lambda work with map()?
Ans:
`map(func, iterable)` applies a function to **each element** in the iterable  
and returns a new iterator of transformed results.
'''
# Example
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]


'''
Q3. How does lambda work with filter()?
Ans:
`filter(func, iterable)` keeps only the elements for which the lambda returns **True**.  
It’s used for selecting or filtering data.
'''
# Example
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)  # [1, 3, 5, 7]


'''
Q4. How does lambda work with sorted()?
Ans:
In `sorted(iterable, key=func)`, the `key` lambda determines **how** elements are compared.  
The function doesn’t change elements — it just defines their sorting order.
'''
# Example
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
# [('Tobias', 22), ('Emil', 25), ('Linus', 28)]


'''
Q5. How do you sort strings by length using lambda?
Ans:
Use `key=lambda x: len(x)` — it sorts based on the length of each string.
'''
# Example
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)  # ['pie', 'apple', 'banana', 'cherry']


'''
Q6. What does map() return — a list or something else?
Ans:
`map()` returns a **map object (iterator)**, not a list.  
You need to wrap it with `list()` (or `tuple()`) to see results.
'''
# Example
nums = [1, 2, 3]
result = map(lambda x: x + 1, nums)
print(result)          # <map object at ...>
print(list(result))    # [2, 3, 4]


'''
Q7. What happens if the lambda used in filter() returns non-boolean values?
Ans:
Python treats non-zero/non-empty results as **True**,  
so it still works — but explicit booleans are preferred.
'''
# Example
nums = [0, 1, 2, 3]
print(list(filter(lambda x: x, nums)))  # [1, 2, 3]


'''
Q8. Can we use lambda with multiple keys in sorted()?
Ans:
Yes — by returning tuples from the lambda for multi-level sorting.
'''
# Example
students = [("Ali", 25), ("Zara", 22), ("Ali", 20)]
sorted_students = sorted(students, key=lambda x: (x[0], x[1]))
print(sorted_students)
# [('Ali', 20), ('Ali', 25), ('Zara', 22)]


'''
Q9. What are practical use cases of lambda + built-ins?
Ans:
✅ Data transformation (map)  
✅ Data filtering (filter)  
✅ Custom sorting (sorted)  
✅ Functional-style pipelines (chained processing)
'''
# Example
nums = [1, 2, 3, 4, 5]
result = list(map(lambda x: x**2, filter(lambda n: n % 2 == 0, nums)))
print(result)  # [4, 16]


'''
Q10. Summary:
Ans:
✅ Common Lambda Use with Built-ins  
| Function     | Purpose                            | Lambda Example                            | Output Example       |
|-----------   |----------------------------------  |-----------------------------------------  |--------------------- |
| **map()**    | Transform all elements             | `map(lambda x: x*2, lst)`                 | `[2, 4, 6]`          |
| **filter()** | Keep elements passing condition    | `filter(lambda x: x > 0, lst)`            | `[1, 2, 3]`          |
| **sorted()** | Custom sort order                  | `sorted(lst, key=lambda x: len(x))`       | `['a', 'abc']`       |

'''
# Example Summary
nums = [1, 2, 3, 4, 5]
print(list(map(lambda x: x**2, nums)))                     # [1, 4, 9, 16, 25]
print(list(filter(lambda x: x % 2 == 0, nums)))            # [2, 4]
print(sorted(["hi", "hello", "hey"], key=lambda x: len(x))) # ['hi', 'hey', 'hello']
