'''
- while
- while loop runs "unless a condition is met"
- it's like saying "keep doing untile the condition is met"
'''

# Example
count=1
while count<4:
    # do something
    count+=1

# Infinite Loop
while True:
    print("Running Forever...!!!")
    break # this break is essential to defeat infinity loop

# Example "Infinite" use?
user_input=""
while user_input!="exit":
    user_input=input("Enter your choice : ")
# Here we keep asking user's choice untile he wants to exit.
