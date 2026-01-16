'''
Q1. What does Generator[a, b, c] mean in typing?
A.
Generator[a, b, c] describes a generator in terms of:
- what it yields,
- what it can receive via send(),
- and what it finally returns when it ends.

It can be read as:
Generator[YieldType, SendType, ReturnType]
'''
# Example:
# Generator[int, str, int]
# yields int
# receives str via .send()
# returns int at the end


'''
Q2. What is the simple mental model for Generator typing?
A.
The simplest mental model is:
Generator[OUT, IN, END]

OUT  → values produced using yield
IN   → values sent using .send()
END  → final value returned when generator finishes
'''
# Example:
# Generator[int, None, None]
# OUT  = int
# IN   = None (no send)
# END  = None (no meaningful return)


'''
Q3. What does the YieldType represent?
A.
YieldType represents the type of values produced by the generator
every time it hits a yield statement.
'''
# Example:
# def gen() -> Generator[int, None, None]:
#     yield 1
#     yield 2
# YieldType = int


'''
Q4. What does the SendType represent?
A.
SendType represents the type of value that can be sent *into*
the generator using the .send() method.
'''
# Example:
# def g() -> Generator[int, str, None]:
#     value = yield 0
#     # value will be a string sent via .send("hello")


'''
Q5. What does the ReturnType represent?
A.
ReturnType represents the final value returned when the generator
finishes execution using return, which is carried by StopIteration.
'''
# Example:
# def g() -> Generator[int, None, int]:
#     yield 1
#     return 42
# StopIteration.value == 42


'''
Q6. Why do most backend generators use Generator[T, None, None]?
A.
Because most backend generators:
- only yield values,
- do not use .send(),
- do not return a meaningful final value.

They are used for streaming data, not two-way communication.
'''
# Example:
# def read_rows() -> Generator[dict, None, None]:
#     for row in rows:
#         yield row
