# =================== 8.5/10 ======================
# =================== if isalpha(restricted) ======================

def is_alpha(word):
    if not word:
        return False
    for character in word:
        ascii_char = ord(character)
        if not (65 <= ascii_char <= 90 or 97 <= ascii_char <= 122):
            return False
    return True

def all_alpha(list_of_strings):
    """
    Returns True only if all strings are non empty, and all of them only contains alphabets.
    """
    return all(is_alpha(s) for s in list_of_strings)

if __name__=="__main__":
    try:
        tokens=input("Enter strings : ")
        list_of_strings=tokens.split(" ")
        print(all_alpha(list_of_strings))
    except Exception:
        print("Invalid Inputs!")


# =================== 9/10 ======================

# def all_alpha(list_of_strings):
#     """
#     Returns True only if all strings are non empty, and all of them only contains alphabets.
#     """
#     return all(s.isalpha() for s in list_of_strings)

# if __name__=="__main__":
#     try:
#         tokens=input("Enter strings : ")
#         list_of_strings=tokens.split(" ")
#         print(all_alpha(list_of_strings))
#     except Exception:
#         print("Invalid Inputs!")


# =================== 6/10 ======================
# works alomost , but alsoaccepts the symbols apart from characters.
'''
Task: Write a function all_alpha(strings) that returns True if every string in the list strings is non-empty and contains only alphabetic characters (a–z/A–Z), and False otherwise.
'''
# def all_alpha(list_of_strings):
#     """
#     Return True if all the string in the list are non empty and non of them have digits either.
#     """
#     for s in list_of_strings:
#         if s == "":
#             return False
#         if not all(ord(i) not in range(48,58) for i in list(s)):
#             return False
#     return True

# if __name__=="__main__":
#     try:
#         tokens=input("Enter strings : ")
#         list_of_strings=tokens.split(" ") # here splitting by " " a space becomes important because only split() will remove all spaces on side and middle of the input
#         print(all_alpha(list_of_strings))
#     except ValueError:
#         print("Invalid Inputs!")