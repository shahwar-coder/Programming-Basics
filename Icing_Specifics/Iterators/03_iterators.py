'''
Q1. Where does an iterator actually “remember” its position?
Ans:
Inside the iterator itself.  
The iterable never stores the current position — only the iterator keeps
a private internal pointer/index that moves on each next() call.
'''
# Example
items = [10, 20, 30]
it = iter(items)
print(next(it))   # 10 → pointer now at index 1


'''
Q2. Does the iterable (like a list) change during iteration?
Ans:
No. The iterable is untouched.  
Only the iterator updates its internal pointer.
'''
# Example
lst = [10, 20, 30]
it = iter(lst)
next(it); next(it)
print(lst)   # [10, 20, 30] (unchanged)


'''
Q3. How does the iterator move internally on next() calls?
Ans:
Each next() call:
1) Reads the element at the current pointer  
2) Moves the pointer forward  
3) Raises StopIteration when pointer crosses the end
'''
# Example
it = iter([10,20,30])
print(next(it))  # 10
print(next(it))  # 20


'''
Q4. What happens if next() goes past the end?
Ans:
StopIteration is raised, meaning the iterator is exhausted.
'''
# Example
it = iter([1])
print(next(it))   # 1
# next(it)        # StopIteration


'''
Q5. Where exactly is this pointer stored?
Ans:
Inside the iterator object's internal structure.
List iterators internally store:
• A reference to the list  
• An internal index (the pointer)
'''
# Example (concept)
# list_iterator internally tracks an index


'''
Q6. Can multiple iterators be created from the same iterable?
Ans:
Yes. Each iterator has its own independent pointer.
Multiple iterators = multiple bookmarks in the same book.
'''
# Example
lst = [10,20,30]
a = iter(lst)
b = iter(lst)
print(next(a))  # 10
print(next(b))  # 10 (independent pointers)


'''
Q7. Why is an iterable like a “book” and an iterator like a “bookmark”?
Ans:
Iterable (book) → stores the content  
Iterator (bookmark) → tracks your position  
Multiple bookmarks = multiple independent iterators
'''
# Example (concept)
# Book: [10,20,30], Bookmark A at index 1, Bookmark B at index 0


'''
Q8. Why are iterators consumed?
Ans:
Their pointer only moves forward.  
Once the end is reached, they cannot restart.
'''
# Example
it = iter([3,4])
next(it); next(it)
# next(it)  # StopIteration


'''
Q9. Why isn’t the pointer stored inside the iterable itself?
Ans:
Because iterables must allow multiple independent iterators at the same time.
A global pointer would break this.
'''
# Concept example
# Two active loops over the same list require two different pointers.


'''
Q10. Final summary (memorize this):
Iterable = has data  
Iterator = has pointer  
for-loop = uses iterator protocol automatically  
Only the iterator remembers state.
'''
# Example
# for item in iterable: uses iterator under the hood
