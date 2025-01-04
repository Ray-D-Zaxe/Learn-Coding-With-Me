a = {1, 2, 4, 8, 9}
b = set([2, 4, 6, 8, 0])
c = frozenset([0, 1, 2, 3, 4, 5])



d = [7, 4, 2, 4, True, 6, 9, 0, 1, 4, False, 6, 7, 2, 9, 0, 5, 6, 7, 3, 2, 1, 4, 5, 7, 2, 8]
print(set(d))           # Creates a set of the first occurence of each element in list d and prints them
                        # {0, True, 2, 3, 4, 5, 6, 7, 8, 9}
print()



a.add(True)             # True and 1 are considered the same and hence the length and elements of a remains the same
b.add(False)            # False and 0 are considered the same and hence the length and elements of b remains the same

a.add(5)                # 5 is inserted at index 5 ?, or at its location if values were sorted in ascending order
b.add(True)             # True is inserted at index 1 ?, at at its location if values were sorted in ascending order



a.update([4, 5, 6, 7], c)
                        # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, updates the set with the elements of the arguments passed



# Sets are iterable
for i in a:
    pass



a.difference(b)         # {9, 5}, returns a set with the elements only in a, i.e, (a - (a & b)),
                        # removes the elements of b from a and returns the new set
print(f"a = {a}")
print(f"b = {b}")
a-b                     # {9, 5}, returns a set with the elements only in a, i.e, (a - (a & b))
                        # removes the elements of b from a and returns the new set
b-a                     # {0, 6}, returns a set with the elements only in a, i.e, (b - (a & b))
                        # removes the elements of a from b and returns the new set



print(a)                # {1, 2, 4, 5, 8, 9}
a.clear()               # Clears the set a
print(a)                # set()
print()



a = b.copy()            # a is now a copy of set b



b = {2, 4}



#a.remove()             Error as no argument passed
                        # If the item to remove does not exist, remove() will raise an error.
a.remove(6)             # Removes 6 from the set

#a.discard()            Error as no argument passed
a.discard(6)            # Doesn't raise an error for element not present
a.discard(8)            # Discards 8 from the set
a.discard(b)            # Doesn't discards the elements of b from the set a

a.pop()                 # Removes and returns an arbitrary element from the set

a.clear                 # Clears the set

del b                   # Deletes the set b



a = {5*6, 6+8, 7-9, 8+2, 4/7, False + 1, True * 0, True + False, True * False}
                        # a = {0.5714285714285714, 1, 0, -2, 30, 10, 14}


#---------------------------------------------------------------------------------------


a = {1, 2, 4, 8, 9}
b = set([2, 4, 6, 8, 0])
c = a.copy()            # c is now a copy of set a



a.union(b)              # {0, 1, 2, 4, 6, 8, 9}, returns a new set with the union of the specified sets
                        # Can take multiple arguments, a.union(b, c, d), works on other datatypes/datastructures
a | b                   # {0, 1, 2, 4, 6, 8, 9}, same as a.union(b)
                        # Works for multiple sets as operands, a | b | c | d, only works for sets

a.intersection(b)       # {8, 2, 4}, returns a new set with the intersection of the specified sets
                        # Can take multiple arguments, a.intersection(b, c, d), works on other datatypes/datastructures
a & b                   # {8, 2, 4}, same as a.intersection(b)
                        # Works for multiple sets as operands, a & b & c & d, only works for sets

c.intersection_update(b)# {8, 2, 4}, removes the contents of b except the common elements, changes the original set (c)
                        # works for multiple sets as arguments

a.difference(b)         # {1, 9}, returns a set with the elements only in a, i.e, (a - (a & b)),
                        # works for multiple sets as arguments
                        # removes the elements of b from a and returns the new set
a-b                     # {1, 9}, returns a set with the elements only in a, i.e, (a - (a & b))
                        # removes the elements of b from a and returns the new set
                        # works for multiple sets as operands, a - b - c - d, doesn't work for other datatypes
b-a                     # {0, 6}, returns a set with the elements only in a, i.e, (b - (a & b))
                        # removes the elements of a from b and returns the new set

c.difference_update(a)  # None, returns a set with the elements only in a, changes the original set (c),
                        # works for multiple sets as arguments

a.symmetric_difference(b)
                        # {0, 1, 6, 9}, returns a set with the elements in either of the sets, but not in both
                        # works for multiple sets as arguments, doesn't work for other datatypes
a ^ b                   # {0, 1, 6, 9}, same as a.symmetric_difference(b)
                        # works for multiple sets as operands, a ^ b ^ c ^ d, doesn't work for other datatypes

c.symmetric_difference_update(a)
                        # None, same as c.symmetric_difference(b),
                        # changes the original set (c), works for multiple sets as arguments

a.isdisjoint(b)         # False, Returns whether two sets have a intersection or not

a.issubset(b)           # False, Returns whether set (a) is a subset of set (b)
a < b                   # False, Returns whether all items in this set is present in other, specified set(s)

a.issuperset(b)         # False, Returns whether set (a) is a superset of set (b)
a > b                   # False, Returns whether all items in other, specified set(s) is present in this set
