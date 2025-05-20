print("Hello World")



# Checking Variables

a = 9
b = 9
c = a

# id() returns the address of the argument

id(a)                           # Returns the address of a
id(b)                           # Address is same as a
id(c)                           # Address is same as a

a is b                          # Evalauted as True
b is c                          # Evalauted as True
c is a                          # Evalauted as True
a is b is c                     # Evalauted as True



# Checking for datattype

isinstance(a, int)              # Evalauted as True



# Checking Lists

lst1 = [6, 9]
lst2 = [6, 9]
lst3 = lst1
lst4 = lst1[:]
print(f"id(lst1) : {id(lst1)}\nid(lst4) : {id(lst4)}\n")

id(lst1)                        # returns address of lst1
id(lst2)                        # address different from lst1
id(lst3)                        # address same as lst1
id(f":::{lst3}")

lst1 is lst2                    # Evalauted as False
lst2 is lst3                    # Evalauted as False
lst3 is lst1                    # Evalauted as True
lst1 is lst2 is lst3            # Evalauted as False



# Checking Tuples

tpl1 = (6, 9)
tpl2 = (6, 9)
tpl3 = tpl1

id(tpl1)                        # returns address of tpl1
id(tpl2)                        # address same as tpl1
id(tpl3)                        # address same as tpl1

tpl1 is tpl2                    # Evalauted as True
tpl2 is tpl3                    # Evalauted as True
tpl3 is tpl1                    # Evalauted as True
tpl1 is tpl2 is tpl3            # Evalauted as True



# Checking Dictonary

dict1 = {'c' : 7}
dict2 = {'c' : 7}
dict3 = dict1

id(dict1)                       # returns address of dict1
id(dict2)                       # address different from dict1
id(dict3)                       # address same as dict1

dict1 is dict2                  # Evalauted as False
dict2 is dict3                  # Evalauted as False
dict3 is dict1                  # Evalauted as True
dict1 is dict2 is dict3         # Evalauted as False



# Checking Set

set1 = {6, 9}
set2 = {6, 9}
set3 = set1

id(set1)                        # returns address of set1
id(set2)                        # address different from set1
id(set3)                        # address same as set1

set1 is set2                    # Evalauted as False
set2 is set3                    # Evalauted as False
set3 is set1                    # Evalauted as True
set1 is set2 is set3            # Evalauted as False



# Checking FrozenSet

fset1 = frozenset([6, 9])
fset2 = frozenset([6, 9])
fset3 = fset1

id(fset1)                       # returns address of fset1
id(fset2)                       # address different from fset1
id(fset3)                       # address same as fset1

fset1 is fset2                  # Evalauted as False
fset2 is fset3                  # Evalauted as False
fset3 is fset1                  # Evalauted as True
fset1 is fset2 is fset3         # Evalauted as False



# Assignment

a = b = c = 0                   # a, b, and c will all have the value (0)
b = 1                           # b is assigned to value (1)
c : int  = 2                    # c has the integer value of (2)
d, e, f = 3, 69, 98             # d = 3, e = 69, f = 98
g = None                        # g is assigned to value None
h = 7                           # h i assigned to value 7



# Type casting

a = bool(a)                     # a is typecasted to have a boolian value
b = bool(b)                     # a is typecasted to have a boolian value
c = int(c)                      # c is typecasted to have an integer value
d = float(d)                    # d is typecasted to have a float value
e = chr(e)                      # e is typecasted to have a character value
f = str(f)                      # f is typecasted to have a string value
bytes(5)                        # returns a bytes object of length 5, b'\x00\x00\x00\x00\x00'
bytearray(5)                    # returns a bytearray object of length 5, bytearray(b'\x00\x00\x00\x00\x00')
memoryview(bytes(5))            # returns a memoryview object, <memory at <insert-address>>



# Look at the output for the following
print(f"a : {type(a)} = {a}")
print(f"b : {type(b)} = {b}")
print(f"c : {type(c)} = {c}")
print(f"d : {type(d)} = {d}")
print(f"e : {type(e)} = {e}")
print(f"f : {type(f)} = {f}")
print(f"g : {type(g)} = {g}")
print()


# Typecasting in Lists and Tuple
a = 1, 2, 3, 4, 5               # a is a tuple
b = (6, 7, 8, 9, 0)             # b is also a tuple

a = list(b)                     # elements of b are typecasted as list and assigned to a
b = tuple(a)                    # elements of a are typecasted as tuple and assigned to b
c =  set(a)                     # elements of a are typecasted as set and assigned to c
d = frozenset(c)                # elements of c are typecasted as frozen-set and assigned to d

type(a)                         # returns : <class 'list'>
type(b)                         # returns : <class 'tuple'>
type(c)                         # returns <class 'set'>
type(d)                         # returns <class 'frozenset'>


a = "7.8"
a = float(a)                    # a = 7.8

a = True * False                # a = 0
a = False + 9                   # a = 9
a = True + 6                    # a = 7
a *= False                      # a = 0

a = print(7)
a                               # Prints 7
print(a)                        # Prints None


a = b = 5
id(a)                           # Address of a, same as b
id(b)                           # Address of b, same as a

a += 4
id(a)                           # Address of a changed cuz of change in value
id(b)                           # Address of b remained the same cuz no change in value

b += 4
id(a)                           # Address of a, same as b
id(b)                           # Address of b, same as a



# Boolean values, rest are all true
bool(False)                     # Returns False
bool(None)                      # Returns False
bool(0)                         # Returns False
bool("")                        # Returns False
bool(())                        # Returns False
bool([])                        # Returns False
bool({})                        # Returns False
bool(set())                     # Returns False

print("Number :", input("Input 1 : "), input("Input 2 : "))
                                # First evaluates input 1, then input 2, then executes the print() function
a = 7
