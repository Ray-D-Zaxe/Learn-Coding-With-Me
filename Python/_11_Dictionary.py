# Dictonary work as key value pairs, i.e, dictionary = {"key" : "value"}
a = {"year" : 2025, "month" : 1, "day" : 1, 4 : 1, "day" : 2}   # "day" : 2 overrides "day" : 1
b = dict(year = 2025, month = 1, day = 1)                       # repeating the same key here leads to error
c = {}                                                          # returns empty dictionary



type(a)                                     # returns : <class 'dict'>



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

del a["month"]                              # deletes the key : value pair
