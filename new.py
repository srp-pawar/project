
from multipledispatch import dispatch

# add
def add(a, b):
	c = a + b
	print(c)

# add
def product(a, b, c):
	d = a + b+c
	print(d)

# Uncommenting the below line shows an error	
add(4, 5)

# This line will call the second product method
add(4, 5, 5)
