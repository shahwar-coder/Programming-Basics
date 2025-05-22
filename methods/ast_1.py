'''
1️⃣ Sum of Numbers in a List
Description:
You’re given a string representing a list of integers. Parse it and return the sum of the numbers.

Example:
input_str = "[1, 2, 3, 4, 5]"
# After parsing: [1, 2, 3, 4, 5]
# Sum: 15
output = 15
'''
import ast
def sum_of_numbers(tokens: str)->int:
    # here we receive list but in doulbe quotes ie, string
    ast_tokens=ast.literal_eval(tokens)
    if not isinstance(ast_tokens, list) or not all(isinstance(token, int) for token in ast_tokens):
        raise ValueError("Input must be list of integers!")
    return sum(ast_tokens)

def main():
    try:
        tokens=input("Enter number list of numbers with [] : ") #but actually by default string will be taken.
        print(sum_of_numbers(tokens))

    except (ValueError,SyntaxError):
        print("Invalid Inputs!")

if __name__=="__main__":
    main()

