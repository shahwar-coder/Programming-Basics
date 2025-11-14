'''
Q1. What are the main regex functions in Python?
Ans:
Python’s re module provides:
- re.findall() → returns all matches in a list  
- re.search() → first match (Match object or None)  
- re.split() → splits string based on pattern  
- re.sub() → replace pattern with new text
'''
# Example
import re
print(re.findall(r"\d+", "Age 21, Room 305"))  # ['21', '305']



'''
Q2. What do regex meta-characters like . ^ $ * + ? do?
Ans:
These special symbols control pattern matching:
. any char  
^ start of string  
$ end of string  
* zero or more  
+ one or more  
? zero or one  
Use them to build powerful matching rules.
'''
# Example
print(re.findall(r"he.+o", "hello heyo h3llo"))  # ['hello', 'heyo']



'''
Q3. What are character sets and special sequences in regex?
Ans:
- [] → match any one character from set  
- \d → digit, \w → word character, \s → whitespace  
- \D, \W, \S → opposites  
- \b → word boundary  
These shortcuts simplify pattern creation.
'''
# Example
print(re.findall(r"\b\w+", "Hello world_123!"))  # ['Hello', 'world_123']



'''
Q4. What is the purpose of grouping with parentheses ()?
Ans:
Grouping lets you capture parts of a match or apply quantifiers
to an entire sub-pattern.
'''
# Example
match = re.search(r"(abc)+", "abcabcxyz")
print(match.group())   # abcabc



'''
Q5. What attributes does a Match object provide?
Ans:
A Match object (from re.search or re.match) provides:
- .group() → matched text  
- .span()  → (start, end) indices  
- .string → original string
'''
# Example
m = re.search(r"\d+", "Room 404")
print(m.group(), m.span())  # 404 (5, 8)



'''
Q6. Why use raw strings (r"...") for regex patterns?
Ans:
Raw strings prevent Python from interpreting backslashes,
allowing patterns like r"\d+\s+\w+" to stay readable.
'''
# Example
print(re.findall(r"\d+\s\w+", "12 apples, 33 bananas"))



'''
Q7. What does the | operator do in regex?
Ans:
| means OR. It matches either the pattern on the left or the right.
'''
# Example
print(re.findall(r"cat|dog", "cat dog catalog"))  # ['cat', 'dog', 'cat']



'''
Q8. How do regex flags improve flexibility?
Ans:
Use flags like re.IGNORECASE, re.MULTILINE, re.DOTALL
to change matching behavior (case-insensitive, multi-line, match newlines).
'''
# Example
print(re.findall(r"hello", "HELLO", flags=re.IGNORECASE))  # ['HELLO']



'''
Q9. What is a common mistake when using regex quantifiers?
Ans:
Quantifiers like * and + are greedy by default—they match as much as possible.
Use ? after them to make them non-greedy.
'''
# Example
print(re.findall(r"<.*?>", "<tag>text</tag>"))  # ['<tag>', '</tag>']

