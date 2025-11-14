'''
Q1. How do you convert JSON text into Python objects?
Ans:
Use json.loads() to parse a JSON-formatted string into Python types 
(dict, list, int, str, etc.).
'''
# Example
import json
data = json.loads('{"name": "Ali", "age": 25}')
print(data["name"])   # Ali



'''
Q2. How do you convert Python objects back into JSON text?
Ans:
Use json.dumps() to serialize Python data structures into a JSON string.
'''
# Example
person = {"name": "Aisha", "age": 20}
json_str = json.dumps(person)
print(json_str)   # {"name": "Aisha", "age": 20}



'''
Q3. What Python types can be converted to JSON?
Ans:
json.dumps() accepts dict, list, tuple, string, int, float, True, False, and None.
Invalid types (like sets or custom objects) must be converted manually.
'''
# Example
print(json.dumps([1, "hi", True, None]))



'''
Q4. How do Python types map to JSON types?
Ans:
Python → JSON mapping:
dict → object  
list/tuple → array  
str → string  
int/float → number  
True/False → true/false  
None → null
'''
# Example
print(json.dumps({"active": True, "score": None}))



'''
Q5. How do you format JSON for readability?
Ans:
Use indent for pretty printing, separators to control spacing,
and sort_keys to alphabetically sort dictionary keys.
'''
# Example
obj = {"b": 2, "a": 1}
print(json.dumps(obj, indent=4, sort_keys=True))



'''
Q6. Why is JSON commonly used in Python applications?
Ans:
Because JSON is lightweight, language-independent, easy to parse,
and perfect for APIs, configs, logging, and data exchange.
'''
# Example
# Example use case: Convert API response (JSON) into Python dict



'''
Q7. How do you handle non-serializable Python types like sets or custom objects?
Ans:
Convert them manually (e.g., list(set)), or pass a default function
to json.dumps() that defines how to convert unsupported types.
'''
# Example
print(json.dumps({ "numbers": list({1,2,3}) }))



'''
Q8. Does json.loads() accept JSON from files?
Ans:
json.loads() works with strings.  
For files, use json.load(file_object) which reads and parses automatically.
'''
# Example
# with open("data.json") as f:
#     data = json.load(f)



'''
Q9. How do you write JSON to a file properly?
Ans:
Use json.dump() with indent for readable output.
'''
# Example
# with open("output.json", "w") as f:
#     json.dump({"x": 10}, f, indent=4)



'''
Q10. What are separators in json.dumps() used for?
Ans:
They control how items and key-value pairs are separated, useful for compact or custom formatting.
Default: (',', ': ')  
Custom: (',', ':')
'''
# Example
print(json.dumps({"x": 1, "y": 2}, separators=(",", ":")))
