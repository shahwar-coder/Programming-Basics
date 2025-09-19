user_input = input("enter your value : ").strip().lower()
def take_bool(user_input):
    if user_input in ('1', 'true', 'yes', 'y'):
        return True 
    elif user_input in ('0', 'false', 'no', 'n'):
        return False
    else:
        raise ValueError("Invalid Boolean Input!")
print(take_bool(user_input))
