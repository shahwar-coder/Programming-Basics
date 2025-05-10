# int

user_input = input()

def str_to_int_possible(user_input):
    for character in user_input:
        ord_character = ord(character)
        if ord_character not in range(48,58):
            return False
    return True

is_possible = str_to_int_possible(user_input)

if is_possible:
    print(int(user_input))
else:
    print("Invalid input, cannot be converted to integer")