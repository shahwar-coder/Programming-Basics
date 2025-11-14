'''
Q1. What is the difference between an iterable and an iterator?
Ans:
An iterable can be looped over (list, tuple, string).  
An iterator gives one value at a time and remembers its position.
Create an iterator using iter().
'''
# Example
items = [1, 2, 3]
it = iter(items)
print(next(it))   # 1


'''
Q2. How do you manually iterate using iter() and next()?
Ans:
Call iter() to get an iterator, then call next() repeatedly  
until StopIteration is raised.
'''
# Example
text = "hi"
it = iter(text)
print(next(it))  # h
print(next(it))  # i


'''
Q3. What is the iterator protocol in Python?
Ans:
An object is an iterator if it implements:
• __iter__()  → returns itself  
• __next__()  → returns next value or raises StopIteration
'''
# Example
# All Python iterators follow this protocol.


'''
Q4. How do you create your own custom iterator class?
Ans:
Write a class with __iter__() returning self and __next__()
returning the next item or raising StopIteration.
'''
# Example
class CountToThree:
    def __iter__(self):
        self.x = 1
        return self
    def __next__(self):
        if self.x <= 3:
            val = self.x
            self.x += 1
            return val
        raise StopIteration

for n in CountToThree():
    print(n)
# Output:
# 1
# 2
# 3


'''
Q5. Why do Python for-loops not need explicit iter() or next()?
Ans:
Because for-loops automatically call iter() and repeatedly call next()
behind the scenes until StopIteration ends the loop.
'''
# Example
# Behind the scenes: for x in [1,2,3] uses iter() and next()


'''
Q6. Why are iterators useful in Python?
Ans:
They save memory by producing items lazily (one at a time),
work well with large data, and allow custom iteration behavior.
'''
# Example
# Reading a huge file line-by-line uses an iterator.


'''
Q7. What happens when next() is called after an iterator is exhausted?
Ans:
Python raises StopIteration, meaning there are no more items.
'''
# Example
it = iter([1])
print(next(it))        # 1
# next(it)             # StopIteration


'''
Q8. Can an iterator be reused after it is exhausted?
Ans:
No. Once exhausted, next() always raises StopIteration.
You must create a new iterator.
'''
# Example
lst = [10, 20]
it = iter(lst)
next(it)   # 10
next(it)   # 20
# next(it)  # StopIteration (cannot reuse)


'''
Q9. Are all iterators also iterables?
Ans:
Yes. Every iterator implements __iter__() which returns itself,
so an iterator is both iterable and an iterator.
'''
# Example
# it = iter([1,2,3])
# iter(it) is it  → True


'''
Q10. Main difference between iterables and iterators?
Ans:
Iterables store all items in memory and can restart iteration.  
Iterators produce items on demand and cannot restart once finished.
'''
# Example
# list = [1,2,3] → reusable
# iter(list) → one-time use iterator
