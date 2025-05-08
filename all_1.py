# ============== [10/10] ===================
def all_positive(list_of_nums):
    """
    Return true if every number in list is positive.
    """
    return all(num>0 for num in list_of_nums)

if __name__ == "__main__":
    try:
        tokens = input("Enter integers separated by integers: ")
        list_of_nums = list(map(int, tokens.split()))
        print(all_positive(list_of_nums))
    except ValueError:
        print("Invalid Inputs!")

# ============== [7/10] ===================
'''
# Example input 1:
nums = [3, 14, 1, 9]
print(all_positive(nums))
# Expected output: True

# Example input 2:
nums = [3, -1, 5, 0]
print(all_positive(nums))
# Expected output: False   # because -1 and 0 are not > 0
'''

def all_positive(list_of_num_tokens):
    bool_list=[]
    for num in list_of_num_tokens:
        if num>=0:
            bool_list.append(True)
        else:
            bool_list.append(False)
    return all(bool_list)

try:
    tokens = input()
    list_of_str_tokens = tokens.split()
    list_of_num_tokens = list(map(int, list_of_str_tokens))
    print(all_positive(list_of_num_tokens))
except ValueError:
    print("Invalid Input!")