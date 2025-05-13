'''
Key methods on integers:
1. `.bit.length` : number of bits required to represent the magnitude.
2. `.as_integer_ratio` : numerator/denominator form
3. `.bit_count()` : count of/number of '1' bits in the binary representation. 
'''

# .bit_length()
number=5
print("Binary rep of the number (just to manually see) : ", bin(number))
print(number.bit_length())

# .as_integer_ratio()
float_number=35.5
print(float_number.as_integer_ratio())

# .bit_count()
number=5
print("Binary rep of the number (just to manually see) : ", bin(number))
print(number.bit_count())
