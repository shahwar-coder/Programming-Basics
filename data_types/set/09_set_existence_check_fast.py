'''
Q. Why are sets ideal for membership checks?
Ans. Because checking existence in a set is very fast (O(1)).
'''
# Example
visited = {"home", "login", "profile"}
"login" in visited   # True (fast)
