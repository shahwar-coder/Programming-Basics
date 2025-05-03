# take float and print it, Value error added great value in catching something when input is not float.

try:
    float_number = float(input("Enter a float number : "))
    print(f"Float Number : {float_number}")
except ValueError:
    print("What you have input is not floating number!")