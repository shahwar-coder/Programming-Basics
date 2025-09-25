def get_int_input(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter an integer.")

age = get_int_input("Enter age: ")
print("You entered:", age)

'''
- Protects against program crashes when user enters invalid input.
- Keeps prompting until valid data is given → robust user experience.
- Encapsulates input logic in one place → reusable across program.
'''
