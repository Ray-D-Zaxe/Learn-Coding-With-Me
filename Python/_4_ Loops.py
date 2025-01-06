# For loop using range
# range takes (destination) or (start, destination), or (start, destination, steps)

print()
print("for i in range(5):")
for i in range(5):
    print(i)



print()
print("for i in range(1, 5):")
for i in range(1, 5):
    print(i)



print()
print("for i in range(1, 10, 2):")
for i in range(1, 10, 2):
    print(i)

print(f"Outside loop, i = {i}")



print()
print("for i in '21 pilots':")
for i in "21 pilots":
    print(i)

print(f"Outside loop, i = {i}")



# For loop using list
print()
print("for fruit in fruits: (list)")
fruits = ["apple", "bannana", "cheery"]
for fruit in fruits:
    print(fruit)

print(f"Outside loop, fruit = {fruit}")



# For loop using tupils
print()
print("for alphabet in alphabets: (tupils)")
alphabets = ('a', 'b', 'c', 'd', 'e')
for alphabet in alphabets:
    print(alphabet)

print(f"Outside loop, alphabet = {alphabet}")



# For loop using dictonary
print()
print("for key, value in dictonary:")
dictonary = {1 : 'a', 2 : 'b', 3 : 'c', 4 : 'd', 5 : 'e'}
for key, value in dictonary.items():
    print(f"{key} : {value}")

print(f"Outside loop, key = {key}, value = {value}")



# While loop
print()
count = 0
print("while count < 5:")
while count < 5:
    print(count)
    count += 1
else:                           # else is optional
    print("Loop Completed !!!")
print(f"Outside loop, count = {count}")



# For with pass
print()
print("for i in range(5): if i == 3: pass")
for i in range(5):
    if i == 3:
        pass
    print(i)



# For with break
print()
print("for i in range(5): if i == 3: break")
for i in range(5):
    if i == 3:
        break
    print(i)



# For with continue
print()
print("for i in range(5): if i == 3: continue")
for i in range(5):
    if i == 3:
        continue
    print(i)



# For with else
print()
print('for i in range(3): print(i) else: ("Loop Completed !!!")')
for i in range(3):
    print(i)
else:
    ("Loop Completed !!!")