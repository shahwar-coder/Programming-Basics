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