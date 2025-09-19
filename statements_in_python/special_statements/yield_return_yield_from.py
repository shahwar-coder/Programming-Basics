'''
Q. Output for this code ? 
#IMPORTANT
'''

def child():
    yield "a"
    yield "b"
    return "child-finished"

def parent():
    result = yield from child()
    print("Child returned:", result)
    yield "parent-done"

print(list(parent()))


'''
Actual Output:
Child returned: child-finished
['a', 'b', 'parent-done']
'''

'''
Step-by-step explanation:

1) list(parent()) starts iterating the generator returned by parent().

2) parent() runs until it hits `yield from child()`, which delegates to child().

3) child() first executes `yield "a"`:
   - "a" is yielded out to the caller (collected by list()).

4) Next, child() resumes and executes `yield "b"`:
   - "b" is yielded out to the caller (collected by list()).

5) child() then reaches `return "child-finished"`.
   - This causes child() to raise StopIteration with value "child-finished".
   - `yield from` catches that StopIteration and sets result = "child-finished".

6) Execution returns to parent(): the line after `yield from` runs:
   - `print("Child returned:", result)` prints: Child returned: child-finished

7) parent() continues and executes `yield "parent-done"`:
   - "parent-done" is yielded and collected by list().

8) Iteration finishes and list(parent()) contains the yielded values:
   - ['a', 'b', 'parent-done']

Summary of what is printed to stdout:
- First the print inside parent():  Child returned: child-finished
- Then the printed list from the final line: ['a', 'b', 'parent-done']
'''



