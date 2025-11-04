'''
Q1. What are nested patterns in Python’s match/case?
Ans:
Nested patterns are patterns *inside other patterns*  
used to match complex or layered data structures like tuples or dicts.
'''
# Example
data = ("ok", (200, "Success"))
match data:
    case ("ok", (code, message)):
        print(code, message)   # 200 Success



'''
Q2. Why are nested patterns useful?
Ans:
They let you match and unpack deeply structured data in a single step —  
no need for multiple indexing or separate variable assignments.
'''
# Example
# Instead of:
# if data[0] == "ok":
#     code, msg = data[1]
# Use pattern:
match data:
    case ("ok", (code, msg)):
        print("Code:", code, "Message:", msg)



'''
Q3. Can we use nested patterns with dictionaries too?
Ans:
Yes! You can match dictionary keys and even nested dictionaries inside them.
'''
# Example
response = {"status": "ok", "data": {"id": 101, "name": "Sam"}}
match response:
    case {"status": "ok", "data": {"id": user_id, "name": name}}:
        print(name, user_id)   # Sam 101



'''
Q4. What kinds of data structures support nested matching?
Ans:
Tuples, lists, dictionaries, and even custom objects  
— basically anything structured or containing other data.
'''



'''
Q5. What should we be careful about with nested patterns?
Ans:
Avoid making them too deep — it can hurt readability.  
Use them for clarity, not complexity.
'''



'''
Q6. What’s the main advantage of nested patterns?
Ans:
They combine matching and unpacking for *multi-level data*  
— making code concise, expressive, and ideal for structured inputs like APIs.
'''
