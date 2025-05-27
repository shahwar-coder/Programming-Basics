'''
2. Insert Separators
Task:
Given a list of words words and a separator string sep, produce a new list out that is the same as words but with sep inserted between every two original words. Build out using insert() calls on an initially empty list.

Goal:
Practice strategically inserting elements to interleave a separator.

# Example 1
words = ["a", "b", "c"]
sep   = "-"
# Steps in your code might look like:
#   out starts []
#   insert "a" → ["a"]
#   insert "-" → ["a","-"]
#   insert "b" → ["a","-","b"]
#   insert "-" → ["a","-","b","-"]
#   insert "c" → ["a","-","b","-","c"]
# Final: ["a", "-", "b", "-", "c"]

# Example 2
words = ["hello"]
sep   = ","
# Final: ["hello"]  (no separators needed)
'''
from typing import List
def add_separators(words: List[str], sep: str)->List[str]:
    """"Return a new list with separators"""
    with_separators=[]
    for i,word in enumerate(words):
        if i==0:
            with_separators.append(word)
        else:
            with_separators.append(sep)
            with_separators.append(word)
    return with_separators

def main():
    words = ["a", "b", "c"]
    sep   = "-"

    # words = ["hello"]
    # sep   = ","
    print(add_separators(words, sep))

if __name__=="__main__":
    main()
