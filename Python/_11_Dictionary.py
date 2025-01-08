# Dictonary work as key value pairs, i.e, dictionary = {"key" : "value"}
a = {"year" : 2025, "month" : 1, "day" : 1, 4 : 1, "day" : 2}   # "day" : 2 overrides "day" : 1

b = a                                       # a and b, both are bound to the same dictionary, changes in one will affect the other as they are the same

b = a.copy()                                # b is now just a copy of a

b = dict(a)                                 # b is still just a copy of a

b1, b2 = [2, 4, 6], [8, 9, 0]
b = dict.fromkeys(b1, b2)                   # creates a dictionary with the elements of b1 as individual keys and b2 (as a whole) as values,
                                            # {2: [8, 9, 0], 4: [8, 9, 0], 6: [8, 9, 0]}
b = dict.fromkeys(b1)                       # creates a dictionary with the elements of b1 as individual keys and (None) as the values
                                            # {2: None, 4: None, 6: None}

b = dict(year = 2077, month = 3, day = 9)   # repeating the same key here leads to error
c = {}                                      # returns empty dictionary
d = {                                       # dictionaries within dictionary
    "d1" : {
        "year" : 2025,
        "month" : 5,
        "day" : 6
    },
    "d2" : dict(year = 2047, month = 7, day = 8),
    "d3" : b
}


type(a)                                     # returns : <class 'dict'>


print(f":a: {a}")
iterA = iter(a)

print(next(iterA))             # returns 1, the 1st element
print(next(iterA))             # returns 2, the 2nd element

for i in iterA:         # because next() is already used 2 times, starts with the 3rd element and
   print(f":{i}")                 # accesses each element of list a, one at a time



print(f":b = {b}")
x = b.setdefault("year")                    # returns the respective value for the key ("year")
x = b.setdefault("sec")                     # returns (None), since the key ("sec") doesn't exist, updates the dictionary with ("sec") as the key and (None) as the value
x = b.setdefault("sec", 56)                 # returns (None), since "sec" already exists in dictionary (b), doesn't overrides the value
x = b.setdefault("secma", 8)                # returns (8), , updates the dictionary with ("secma") as the key and (8) as the value



a["month"]                                  # returns : 1

a.get("day")                                # returns : 2

"month" in a                                # returns True, checks for only the key and not the value

x = a.keys()                                # Similar to Lists
type(x)                                     # returns <class 'dict_keys'>

y = a.values()                              # Similar to Lists
type(y)                                     # returns <class 'dict_values'>

z = a.items()                               # Similar to a list of tuples of key value pairs
type(z)                                     # returns <class 'dict_items'>



# dictionary is iterable
for i in a:                                 # i is assigned to the keys
    pass
for i in a:                                 # a[i] evaluates tp the value at, key = i
    pass

for i, j in d.items():                      # i is assigned to keys, j is assigned to the values (nested dictionaries)
    pass
    for k in j:                             # k is assigned to the keys of the nested dictionaries and j[k] evaluates to their respective values
        pass

# dict_keys is iterable
for i in x:
    pass

# dict_values is iterable
for i in y:
    pass

# dict_values is iterable
for i in z:                                 # i is a tuple of (key, value)
    pass
for i, j in z:                              # i is assigned to key and j is assigned to value
    pass



a["hour"] = 5                               # adds a new key : value pair
a["hour"] = 6                               # updates the value of the key : value pair

a.update({"time" : 7})                      # adds a new key : value pair
a.update({"time" : 8})                      # updates the value of the key : value pair
a.update(b)                                 # updates (a) with the elements (key value pairs) of dictionary (b)

a.pop("day")                                # removes the key value pair of the specified key, requires atleast one (valid) key as an argument
a.popitem()                                 # removes the last added key value pair, error if the dictionary is empty

b.clear()                                   # removes all elements (key value pairs) of dictionary b

del a["month"]                              # deletes the key : value pair
del b                                       # deletes the dictionary b
