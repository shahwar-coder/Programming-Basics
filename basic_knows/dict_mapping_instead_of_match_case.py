number_map={
  1: "One",
  2: "Two",
  3: "Three"
}

def number_to_word(number: int)->str:
  """
  Return number in word
  """
  return number_map.get(number, "Unknown Number")

print(number_to_word(2))
print(number_to_word(8))

# Two
# Unknown Number
