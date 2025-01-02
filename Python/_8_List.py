a = [1, 2, 3]
b = a                   # a and b, both are bound to the same list

c = [2] * 6
print(f"c = {c}")



b.append(7)             # appends 7 at the end of both b and a

b = a.copy()            # b has now a copy of a, i.e, b is different then a

b.append(9)             # appends 9 only at the end of b

a.extend(b)             # appends the content of b at the end of a
a.extend([2, 4, 6])     # appends [2, 4, 6] at the end of a

a.insert(3, 5)          # inserts 5
print(f"a.count(2) : {a.count(2)}")     # returns the total occurances of 2 in a
print(f"a.index(2) : {a.index(3)}")     # returns the index of the first occurence of 3
print()

a.pop()                 # deletes the last value of a
a.remove(2)             # removes the first occurence of 2

a.reverse()             # reverse the list a

a.sort()                # sorts the list a, uses timesort algorithm

print(a)
print(a[:])
print(a[2:7])
print(a[-7:7])
print(a[3:-3])

len(a)                  # returns the length of a
max(a)                  # returns the max element in a
min(a)                  # returns the min element in a

a.clear()               # clears the list

a = [5*6, 6+8, 7-9, 8+2, 4/7, False + 1, True * 0, True + False, True * False]
                        # a = [30, 14, -2, 10, 0.5714285714285714, 1, 0, 1, 0]

a+b                     # Concatinates list a and b
a and b                 # returns a
b and a                 # returns b
a or b                  # returns b
b or a                  # returns a
not a                   # returns False