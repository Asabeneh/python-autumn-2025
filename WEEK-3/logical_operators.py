# Logical operators: and, or and negation

print(4 > 3 and 3 > 2) # True and True => True
print(4 > 3 and 3 < 2) # True and False => False
print(4 < 3 and 3 < 2) # False and False => False 

# Or
print(4 > 3 or 3 > 2) # True or True => True
print(4 > 3 or 3 < 2) # True or False => True
print(4 < 3 or 3 < 2) # False or d False => False 

# negation

print(not True) # False
print(not not False)
print(not 4 > 3 and 3 > 2)

# Boolean => True or False
