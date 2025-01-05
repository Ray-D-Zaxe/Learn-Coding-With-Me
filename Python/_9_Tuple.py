thisTuple = ("apple",)
type(thisTuple)             # Returns <class 'tuple'>

# NOT a tuple
thisTuple = ("apple")
(type(thisTuple))           # Returns <class 'str'>

del thisTuple               # deletes the tuple



a = 1, 2, 3, [3, 6], 4
b = (5, 6, 7, 3, 4, 7, [9, 4, 7], 6, 7, 4)
c = tuple([1, 2, 3, 4, 5])  # returns a tuple
c = tuple((3, 1, 2))        # returns a tuple, the function requires an interable as in input



# Unpacking tuple
x1, x2, x3 = c              # x1 = 1, x2 = 2, x3 = 3
y1, y2, *y3 = a             # y1 = 1, y2 = 2, y3 = [3, 6, 4]
z1, *z2, z3 = a             # z1 = 1, z2 = [3, 6], z3 = 4



print(a)                    # prints the elements of a
print(a[:])                 # prints the elements of a
print(a[1:3])               # prints the elements of a from index 1 to 2
print(a[-5:3])              # prints the elements of a from index -5 to 2
print(a[2:-2])              # prints the elements of a from index 2 to -3



a[3].append(5)              # Appends 5 to the list at index 3
b[6].append(9)              # Appends 9 to the list at index 6
b.count(7)                  # Returns the total occurence of element 7 in the tuple b



a.index(2)                  # Returns the index of the first occurence of 2
b.index(7, 2)               # Returns the index of the first occurence of 7 starting from index 2
#b.index(7, 3, 5)           Error, since 7 not found between the index range(3, 5)
b.index(7, 3, 6)            # Returns the index of the first occurence of 7 b/w the crange(3, 6)



a = 5*6, 6+8, 7-9, 8+2, 4/7, False + 1, True * 0, True + False, True * False
                            # a = (30, 14, -2, 10, 0.5714285714285714, 1, 0, 1, 0)



# Tuples are iterable
for i in a:
    pass



c = c + a                   # same as, c = a + c, creates a new tuple with the contents of a and c
c = c * 2                   # same as, c = 2 * c, creates a new tuple with the contents of c repeated twice



a+b                         # returns a new tuple withj the contents of a and b

a and b                     # returns b
b and a                     # returns a
a or b                      # returns a
b and a                     # returns a

3 in a                      # returns True



# Tuple comprehension

a = (1, 2, 3, 4, 5)
(print(i) for i in a)   # prints each element of tuple (a) in new line, one at a time

fruits = ("apple", "banana", "cherry", "kiwi", "mango")
newTuple = tuple(x for x in fruits if "a" in x)
                        # newTuple = ('apple', 'banana', 'mango')

a = tuple(x for x in range(10) if x % 2 == 0)
                        # a = (0, 2, 4, 6, 8)

a = tuple(x if x % 2 == 0 else "odd" for x in range(10))
                        # a = (0, 'odd', 2, 'odd', 4, 'odd', 6, 'odd', 8, 'odd')
