'''
🧩 Task 1: Check for Empty Strings
Write a function has_empty_string(strings: list) -> bool that returns True if any string in the list is empty (""). Otherwise, return False.
'''

# ============== using all() negation/ instead of any() 8.5/10 ==============
# def is_empty_string_present(strings):
#     return not all(strings)

# if __name__=="__main__":
#     try:
#         tokens=input()
#         strings=tokens.split(" ")
#         print(is_empty_string_present(strings))
#     except Exception:
#         print("Invalid Inputs!")


# ============== using any() 10/10 ==============

def is_empty_string_present(strings):
    # return any(len(s)==0 for s in strings) or below line both are correct
    return any(s=="" for s in strings)

if __name__=="__main__":
    try:
        tokens=input()
        strings=tokens.split(" ")
        print(is_empty_string_present(strings))
    except Exception:
        print("Invalid Inputs!")
