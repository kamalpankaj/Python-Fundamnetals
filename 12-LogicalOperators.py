#Logical Operators 
"""In Python, Logical operators are used on conditional statements 
(either True or False). They perform Logical AND,
Logical OR and Logical NOT operations."""

# Logical AND Operator
print("""1. ('Logical AND Operator') Called Logical 'AND' operator. 
If both the operands are true then condition becomes true. for Example: """)
print("X=true &  Y=False then Result is: ")
X= True
Y= False
print(X and Y)
print("X= true & Y=True then Result is: ")
X=True
Y=True
print(X and Y)
print("X=False & Y=Flase then Result is: ")
X=False
Y=False
print(X and Y)

# Logical OR Operator
print("""2. ('Logical OR Operator') If Both the operands are true then condition
becomes true, if one operand are true & one operand are flase then condition
becomes true & if both the operands are flase then condition becomes flase.
For Examples: """)
print("X=True & Y=False then Result is: ")
X=True
Y=False
print(X or Y)
print("X=True & Y=True then Result is: ")
X=True
Y=True
print(X or Y)
print("X=False & Y=False then Result is: ")
X=False
Y=False
print(X or Y)

# Logical Not Operator
print("""3. ('Logical Not Operator) The Logical 'Not' operator is change true value 
to false. False to true For Example: """)
print("X=True & Y=False")
X=True
print("X = "+str(X))
Y=False
print("Y = "+str(Y))
print("After Using of 'Not' Logical Operator")
Z= not X
print("X = "+str(Z))
Z= not Y
print("Y = "+str(Z))