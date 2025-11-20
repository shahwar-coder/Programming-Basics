'''
❓ **Question:**  
Given a list of integers, how can you use **bitwise operations** (instead of modulo %) to **filter out only the odd numbers** in Python?

🧠 Hint:  
Odd numbers have their **least significant bit (LSB) = 1**, so you can use:  
    num & 1 == 1
'''

# ✅ Code: Filter odd numbers using bitwise AND
numbers = [3, 10, 17, 22, 35, 40, 51]

odd_numbers = [x for x in numbers if x & 1]

print("Odd numbers:", odd_numbers)
