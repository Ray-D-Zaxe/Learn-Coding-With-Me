a = {1, 2, 4, 8, 9}
b = set([2, 4, 6, 8, 0])
c = frozenset([0, 1, 2, 3, 4, 5])

d = [7, 4, 2, 4, True, 6, 9, 0, 1, 4, False, 6, 7, 2, 9, 0, 5, 6, 7, 3, 2, 1, 4, 5, 7, 2, 8]
print(set(d))   # Creates a set of the first occurence of each element in list d and prints them
                # {0, True, 2, 3, 4, 5, 6, 7, 8, 9}
print()



a.add(True)     # True and 1 are considered the same and hence the length and elements of a remains the same
b.add(False)    # False and 0 are considered the same and hence the length and elements of b remains the same

a.add(5)        # 5 is inserted at index 5 ?, or at its location if values were sorted in ascending order
b.add(True)     # True is inserted at index 1 ?, at at its location if values were sorted in ascending order

a.update([4, 5, 6, 7], c)
                # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, updates a with the union of the specified sets



pass



a.difference(b) # {9, 5}, returns a set with the elements only in a, i.e, (a - (a & b)),
                # removes the elements of b from a and returns the new set
print(f"a = {a}")
print(f"b = {b}")
a-b             # {9, 5}, returns a set with the elements only in a, i.e, (a - (a & b))
                # removes the elements of b from a and returns the new set
b-a             # {0, 6}, returns a set with the elements only in a, i.e, (b - (a & b))
                # removes the elements of a from b and returns the new set
print()

print(a)        # {1, 2, 4, 5, 8, 9}
a.clear()       # Clears the set a
print(a)        # set()
print()

a = b.copy()    # a is now a copy of set b

a = {5*6, 6+8, 7-9, 8+2, 4/7, False + 1, True * 0, True + False, True * False}
                    # a = {0.5714285714285714, 1, 0, -2, 30, 10, 14}

names = ["John", "Jane"]
foods = ["pizza", "sushi", "burgers"]
for name, food in names, foods:
    print(name + " likes " + food)