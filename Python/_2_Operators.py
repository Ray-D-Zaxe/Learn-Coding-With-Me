# Assignment Operator

a = 56                          # assigns the value 56 to a
a += 4                          # a becomes a + 4, i.e, 60
a -= 20                         # a becomes a - 20, i.e, 40
a *= 2                          # a becomes a * 2, i.e, 80
a **= 2                         # a becomes a ** 2, i.e, 6400
a //= 2                         # a becomes a // 2, i.e, 3200
a /= 2                          # a becomes a / 2, i.e, 1600.00, returns the value in float
a %= 3                          # a becomes a % 2, i.e, 1, i.e, the remainder or mod/modulus

a = 18
a &= 7                          # a becomes 2, 18 and 7
a |= 5                          # a becomes 7, 2 or 5
a ^= 3                          # a becomes 4, 7 xor 3
a <<= 2                         # a becomes 14, 4 left shifted by 2
a >>= 2                         # a becomes 4, 14 right shifted by 2

print("Using type hints :")
a : str = 'Yo'                  # using type hints
b: float = 5.6
print(f'a = {a}\nb = {b}')

print("Assigning multiple values at once :")
a = b = 5                       #Assigning multiple values at once
print(f'a = {a} = b = {b}')
a, b = 15, 4 
print(f'a = {a}\nb = {b}')



# Arithmatic Operator
print()
print("Arithmatic Operators :")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a ** b = {a ** b}")
print(f"a / b = {a / b}")
print(f"a // b = {a // b}")
print(f"a % b = {a % b}")

a, b = 5.6, 56
print(f'a + b = {a + b}, for a = {a}, and b = {b}')



# Comparison Operator
print()
print("Comparison Operators :")
print(f"a > b = {a > b}")
print(f"a < b = {a < b}")
print(f"a == b = {a == b}")
print(f"a != b = {a != b}")
print(f"a >= b = {a >= b}")
print(f"a <= b = {a <= b}")



# Logical Operators
print()
a, b = True, False

print(f"Comparison Operators : (for a = {a}, and b = {b})")
print(f"a and b = {a and b}")
print(f"a or b = {a or b}")
print(f"not a = {not a}")



# Bitwise Operators
print()
a, b = 15, 6
print(f"BitWise Operators : (for a = {a}, and b = {b})")

print(f"~a : {~a}, (not a)")
print(f"a & b : {a & b}, (a and b)")
print(f"a << 2 : {a << 2}, (a left shifted by 2)")
print(f"a >> 2 : {a >> 2}, (a right shifted by 2)")
print(f"a ^ b : {a ^ b}, (a xor b)")
print(f"a | b : {a | b}, (a or b)")



# Membership and Identity Operators
print()
print("Membership Operators :")
fruits = ["apple", "banana", "cherry"]

print(f'"banana" in fruits : {"banana" in fruits}')       # True
print(f'"grape" not in fruits {"grape" not in fruits}')    # True

print("Identity Operators :")

a = ["apple", "banana"]
b = ["apple", "banana"]
c = a

print(f"a is c : {a is c}")     # True, because c is a reference to a
print(f"a is b : {a is b}")     # False, because a and b are different objects
print(f"a == b : {a == b}")     # True, because a and b have the same content



# Ternary Operator
print()
a, b = 10, 20
print("Ternary Operator :")

min = a if a < b else b
print(f"min = {min}")