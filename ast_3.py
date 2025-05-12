'''
Question:
Write a Python script that takes a list of strings—each string representing a valid Python literal—and for each string:

Safely parses it into the corresponding Python object using ast.literal_eval.

Prints the original string, the parsed value, and the type of that value.

Mini Input Example:
literals = [
    "123",
    "'hello'",
    "[1, 2, 3]"
]
Expected Output:
"123"   → 123   <class 'int'>
"'hello'" → hello <class 'str'>
"[1, 2, 3]" → [1, 2, 3] <class 'list'>
'''
import ast
def take_out_literals_from_string(listified_tokens: list):
    for token in listified_tokens:
        print(f"token : {token}")
        ast_token=ast.literal_eval(token) #argument should always be string
        print(f"{token} -> {ast_token} -> {type(ast_token)}")


def main():
    try:
        tokens=input("Input Objects : ") #by default it will be a string
        listified_tokens=tokens.split()
        print(f"Listified Tokens: {listified_tokens}")
        take_out_literals_from_string(listified_tokens)
    except Exception:
        print("Invalid Input!")

if __name__=="__main__":
    main()
