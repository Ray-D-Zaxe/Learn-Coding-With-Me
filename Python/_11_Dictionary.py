# Dictonary work as key value pairs, i.e, dictonary = {"key" : "value"}
a = {"year" : 2020, "month" : 1, "day" : 1, 4 : 1, "day" : 2}   # "day" : 2 is ignored
b = dict(year = 2020, month = 1, day = 1)                       # repeating the same key here leads to error
c = {}                                                          # returns empty dictionary

print(f"a : {type(a)} = {a}")
print(f"b : {type(b)} = {b}")
print(f"c : {type(c)} = {c}")