a = 1, 2, 3, [3, 6], 4
b = (5, 6, 7, 3, 4, 7, [9, 4, 7], 6, 7, 4)

print(a[2:])

a[3].append(5)      # Appends 5 to the list at index 3
b[6].append(9)      # Appends 9 to the list at index 6
b.count(7)          # Returns the total occurence of element 7 in the tuple b

a.index(2)          # Returns the index of the first occurence of 2
b.index(7, 2)       # Returns the index of the first occurence of 7 starting from index 2
#b.index(7, 3, 5)   Error, since 7 not found between the index range(3, 5)
b.index(7, 3, 6)    # Returns the index of the first occurence of 7 b/w the crange(3, 6)

a = 5*6, 6+8, 7-9, 8+2, 4/7, False + 1, True * 0, True + False, True * False
                    # a = (30, 14, -2, 10, 0.5714285714285714, 1, 0, 1, 0)

a+b                 # returns a new tuple withj the contents of a and b
a and b             # returns b
b and a             # returns a
a or b              # returns a
b and a             # returns a