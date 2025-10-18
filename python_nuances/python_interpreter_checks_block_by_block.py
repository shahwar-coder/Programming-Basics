'''
Python checks indentation strictly — not line-by-line, but block-by-block.
'''

if 5>2:
  print("5 is more than 2")
    print("2: 5 is more than 2")

'''
Intuitively we think, okay 2nd print will give error, but atleast 1st print should be printed right?
-> Answer to this is : Python (interpreter) checks block by block not line by line, so if block is considered here.
'''
