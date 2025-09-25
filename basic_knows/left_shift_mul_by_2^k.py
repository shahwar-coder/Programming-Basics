'''
Demonstarte left shift (<< and * 2^k relation) #SAME
'''

def left_shift_demo(num, max_k=4):
  """
  Demonstrate left shift (<< and * 2^k relation) 
  Shows actual shift, equivalent multiplication and binary states.
  """
  for k in range(1,max_k+1):
    shifted=num<<k
    multiplied=num * (2**k)
    print(f"Left Shift : {num}<<{k} -> {shifted}")
    print(f"Multiply : {num}*2^{k} -> {multiplied}")
    print(f"Binary State Shift: {format(num, 'b')}->{format(shifted, 'b')}")
    print('-'*30) # for visual separation

def get_decimal_number(prompt: str)->int:
  """
  Ensure valid decimal number input
  """
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      print("Please enter valid decimal number")

decimal_number=get_decimal_number("Enter a decimal number: ")
left_shift_demo(decimal_number, max_k=4)
