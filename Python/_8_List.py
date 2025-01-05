a = [1, 2, 3]
b = a                   # a and b, both are bound to the same list

c = [2] * 6
print(f"c = {c}")



b.append(7)             # appends 7 at the end of both b and a

b = a.copy()            # b has now a copy of a, i.e, b is different then a



b.append(9)             # appends 9 only at the end of b

a.extend(b)             # appends the content of b at the end of a
a.extend([2, 4, 6])     # appends [2, 4, 6] at the end of a

a.insert(3, 5)          # inserts 5 at index 3



a.count(2)              # returns the total occurances of 2 in a
a.index(3)              # returns the index of the first occurence of 3



a.pop()                 # deletes the last value of a
a.remove(2)             # removes the first occurence of 2
del a[2]                # deletes the element at index 2



a.reverse()             # reverse the list a
a.sort(reverse = True)  # reverse the list a
a.sort()                # sorts the list a, uses timesort algorithm
def myfunc(n):
  return abs(n - 50)    # returns the absolute value of the difference between n and 50

a = [100, 50, 65, 82, 23]
a.sort(key = myfunc)
print(a)

a = ["banana", "Orange", "Kiwi", "cherry"]
a.sort(key = str.lower)
print(a)



print(a)                # prints the elements of a
print(a[:])             # prints the elements of a
print(a[2:7])           # prints the elements of a from index 2 to 6
print(a[-7:7])          # prints the elements of a from index -7 to 6
print(a[3:-3])          # prints the elements of a from index 3 to -3



len(a)                  # returns the length of a
max(a)                  # returns the max element in a
min(a)                  # returns the min element in a



a.clear()               # clears the list (a)

del a                   # deletes the list (a)



a = [5*6, 6+8, 7-9, 8+2, 4/7, False + 1, True * 0, True + False, True * False]
                        # a = [30, 14, -2, 10, 0.5714285714285714, 1, 0, 1, 0]



# Lists are iterable
for i in a:
    pass



a + b                   # Concatinates list a and b
a and b                 # returns a
b and a                 # returns b
a or b                  # returns b
b or a                  # returns a
not a                   # returns False



# List comprehension
# newlist = [expression for item in iterable if condition == True]
# newlist = [expression if condition == True else expression for item in iterable]


a = [1, 2, 3, 4, 5]
[print(i) for i in a]   # prints each element of list (a) in new line, one at a time



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
                        # newlist = ['apple', 'banana', 'mango']



a = [x for x in range(10) if x % 2 == 0]
                        # a = [0, 2, 4, 6, 8]



a = [x if x % 2 == 0 else "odd" for x in range(10)]
                        # a = [0, "odd", 2, "odd", 4, "odd", 6, "odd", 8, "odd"]



a = [1, 2, 3, [3, 6], 4]
b = [5, 6, 7, 3, 4, 7, [9, 4, 7], 6, 7, 4]
c = list([1, 2, 3, 4, 5])  # returns a tuple
c = list((3, 1, 2))        # returns a tuple, the function requires an interable as in input



# Unpacking List
x1, x2, x3 = c              # x1 = 1, x2 = 2, x3 = 3
y1, y2, *y3 = a             # y1 = 1, y2 = 2, y3 = [3, 6, 4]
z1, *z2, z3 = a             # z1 = 1, z2 = [3, 6], z3 = 4


print(f"x1 = {x1}, x2 = {x2}, x3 = {x3}")
print(f"y1 = {y1}, y2 = {y2}, y3 = {y3}")
print(f"z1 = {z1}, z2 = {z2}, z3 = {z3}")



names = ["John", "Jane"]
foods = ["pizza", "sushi"]
for name, food in names, foods:
                # Access the values of names as name and food and when names is exhausted only then repeates
                # the same for foods
    print(name + " likes " + food)