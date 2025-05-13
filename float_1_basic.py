'''
- float : double precision number
- Used when we do division or directly write a decimal literal
'''

x=2.51
print(type(x))

'''
- float contructor : float()
- float() = 0.0
- float(x) converts x to float
'''

print(float())
print(float(3))
print(float(True))
print(float(False))

'''
- how float results are displayed/represented
'''

print(0.1)
print(format(0.1,'.17f'))

print(0.2)
print(format(0.2, '.6f'))

print(0.1+0.2)
