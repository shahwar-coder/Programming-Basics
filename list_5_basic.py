'''
2. Collect Non-Empty Strings
Task:
Given a list of strings words, build a new list containing only the non-empty strings by iterating over words and appending each non-empty element to your result list.

Goal:
Practice conditionally using append() to filter data.

# Example 1
words = ["apple", "", "banana", "", "cherry"]
# You should produce: ["apple", "banana", "cherry"]

# Example 2
words = ["", "", ""]
# You should produce: []

# Example 3
words = ["one", "two", "three"]
# You should produce: ["one", "two", "three"]

'''
from typing import List
def words_filter(words: List[str])->List[str]:
    filtered=[]
    for word in words:
        if word:
            filtered.append(word)
    return filtered

def main():
    words=["apple", "banana", "", "cherry", "", "avocado"]
    # words=[]
    print(words_filter(words))

if __name__=="__main__":
    main()
