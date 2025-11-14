'''
Q1. Is an iterator’s position stored in real physical memory?
Ans:
Yes. The iterator stores a tiny integer pointer in RAM.  
This pointer tracks which element will be returned next.
'''
# Example
it = iter([10,20])
next(it)  # pointer moves from 0 → 1


'''
Q2. Where exactly is this pointer stored?
Ans:
Inside the iterator object itself.  
Not inside the list and not globally — only inside the iterator's memory block.
'''
# Example (concept)
# RAM:
#   list → [10,20,30]
#   iterator → { pointer=0, reference_to_list }


'''
Q3. Does the iterable (like a list) store any pointer or state?
Ans:
No. The iterable only stores data.  
All state (current position) lives inside the iterator.
'''
# Example
lst = [10,20,30]
it = iter(lst)
next(it)
print(lst)   # list unchanged


'''
Q4. How does the pointer change during iteration?
Ans:
Each next() call:
1) accesses list[pointer]
2) increments pointer
3) raises StopIteration when pointer passes the end
'''
# Example
it = iter([10,20,30])
print(next(it))  # 10 (pointer=1)
print(next(it))  # 20 (pointer=2)


'''
Q5. Why is the pointer stored only in the iterator, not the iterable?
Ans:
Because multiple iterators must work independently.  
One iterable → many iterators → each has its own pointer.
'''
# Example
lst = [10,20]
a = iter(lst); b = iter(lst)
print(next(a))  # 10
print(next(b))  # 10  (independent pointers)


'''
Q6. What happens to the pointer when the iterator is destroyed?
Ans:
The iterator object is garbage-collected, and its pointer disappears.  
The iterable remains unchanged.
'''
# Example
it = iter([1])
del it  # pointer memory freed


'''
Q7. Is the iterator pointer a large data structure?
Ans:
No. It is usually just a small integer stored inside the iterator.
'''
# Example (concept)
# pointer = simple integer index


'''
Q8. Why do some iterators store more than just a pointer?
Ans:
Complex iterators (dict iterators, generators, file iterators) may store:
• internal stacks  
• last yielded values  
• references to parent objects  
But the key idea remains: state lives *inside the iterator*.
'''


'''
Q9. Do iterators modify the original iterable in memory?
Ans:
Never. Iterators only read.  
The iterable's memory stays unchanged unless you modify it explicitly.
'''


'''
Q10. Final mental model:
Iterable = stored data  
Iterator = tiny object in memory containing:  
   • a reference to the iterable  
   • an internal pointer (index)  
for-loop = uses the iterator’s pointer behind the scenes
'''
