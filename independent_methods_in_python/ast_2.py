'''
2️⃣ Count Keys in a Dictionary
Description:
You’re given a string representing a dictionary. Parse it and return how many keys it contains.

Example:

input_str = "{'apple': 2, 'banana': 3, 'cherry': 5}"
# After parsing: {'apple':2, 'banana':3, 'cherry':5}
# Number of keys: 3
output = 3
'''

import ast
def count_dict_keys(tokens: str)->int:
    ast_tokens=ast.literal_eval(tokens)
    if not isinstance(ast_tokens, dict):
        raise ValueError("Input correct dict please!")
    return len(ast_tokens)

def main():
    try:
        tokens=input("enter a dict : ")
        print(f"Total Keys in the Dict : {count_dict_keys(tokens)}")
    except (ValueError, SyntaxError):
        print("Invalid Inputs!")

if __name__=="__main__":
    main()
