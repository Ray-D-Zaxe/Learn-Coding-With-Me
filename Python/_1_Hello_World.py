print("Hello World")

# Checking Variables

print("For Variables : ")

a = 9
b = 9
c = a

print(f"id(a) : {id(a)}")       # id() returns the address of the argument
print(f"id(b) : {id(b)}")
print(f"id(c) : {id(c)}")

print(f"a is b : {a is b}")
print(f"b is c : {b is c}")
print(f"c is a : {c is a}")
print(f"a is b is c : {a is b is c}")

print()



# Checking Lists

print("For Lists : ")

lst1 = [6, 9]
lst2 = [6, 9]
lst3 = lst1

print(f"id(lst1) : {id(lst1)}")
print(f"id(lst2) : {id(lst2)}")
print(f"id(lst3) : {id(lst3)}")

print(f"lst1 is lst2 : {lst1 is lst2}")
print(f"lst2 is lst3 : {lst2 is lst3}")
print(f"lst3 is lst1 : {lst3 is lst1}")
print(f"lst1 is lst2 is lst3 : {lst1 is lst2 is lst3}")

print()



# Checking Tupils

print("For Tupils : ")

tpl1 = (6, 9)
tpl2 = (6, 9)
tpl3 = tpl1

print(f"id(tpl1) : {id(tpl1)}")
print(f"id(tpl2) : {id(tpl2)}")
print(f"id(tpl3) : {id(tpl3)}")

print(f"tpl1 is tpl2 : {tpl1 is tpl2}")
print(f"tpl2 is tpl3 : {tpl2 is tpl3}")
print(f"tpl3 is tpl1 : {tpl3 is tpl1}")
print(f"tpl1 is tpl2 is tpl3 : {tpl1 is tpl2 is tpl3}")

print()



# Checking Dictonary

print("For Dictonary : ")

dict1 = {'c' : 7}
dict2 = {'c' : 7}
dict3 = dict1

print(f"id(dict1) : {id(dict1)}")
print(f"id(dict2) : {id(dict2)}")
print(f"id(dict3) : {id(dict3)}")

print(f"dict1 is dict2 : {dict1 is dict2}")
print(f"dict2 is dict3 : {dict2 is dict3}")
print(f"dict3 is dict1 : {dict3 is dict1}")
print(f"dict1 is dict2 is dict3 : {dict1 is dict2 is dict3}")

print()



# Checking Set

print("For Set : ")

set1 = {6, 9}
set2 = {6, 9}
set3 = set1

print(f"id(set1) : {id(set1)}")
print(f"id(set2) : {id(set2)}")
print(f"id(set3) : {id(set3)}")

print(f"set1 is set2 : {set1 is set2}")
print(f"set2 is set3 : {set2 is set3}")
print(f"set3 is set1 : {set3 is set1}")
print(f"set1 is set2 is set3 : {set1 is set2 is set3}")

print()



# Checking FrozenSet

print("For FrozenSet : ")

fset1 = frozenset([6, 9])
fset2 = frozenset([6, 9])
fset3 = fset1

print(f"id(fset1) : {id(fset1)}")
print(f"id(fset2) : {id(fset2)}")
print(f"id(fset3) : {id(fset3)}")

print(f"fset1 is fset2 : {fset1 is fset2}")
print(f"fset2 is fset3 : {fset2 is fset3}")
print(f"fset3 is fset1 : {fset3 is fset1}")
print(f"fset1 is fset2 is fset3 : {fset1 is fset2 is fset3}")

print()



# Assignment

a = b = c = 0
b = 1
c : int  = 2
d, e, f = 3, 69, 98
g = None
h = 7

# Type casting

a = bool(a)
b = bool(b)
c = int(c)
d = float(d)
e = chr(e)
f = str(f)

print(f"a : {type(a)} = {a}")
print(f"b : {type(b)} = {b}")
print(f"c : {type(c)} = {c}")
print(f"d : {type(d)} = {d}")
print(f"e : {type(e)} = {e}")
print(f"f : {type(f)} = {f}")
print(f"g : {type(g)} = {g}")
print()


# Typecasting in Lists and Tupils
a = 1, 2, 3, 4, 5
b = (6, 7, 8, 9, 0)

a = list(b)
b = tuple(a)
c =  set(a)
d = frozenset(c)

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print()


a = "7.8"
a = float(a)                    # a = 7.8

a = True * False                # a = 0
a = False + 9                   # a = 9
a = True + 6                    # a = 7
a *= False                      # a = 0
print()

a = print(7)
a                               # Prints 7
print(a)                        # Prints None