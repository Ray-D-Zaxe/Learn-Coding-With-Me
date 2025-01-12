a, b, c = 10, 20, 30

# Short hand if
if (b > a): print("B is greater")

# Short hand if else
print(f'"A is greater" if a > b else "B is greater" : {"A is greater" if a > b else "B is greater"}')

# Nested short hand if else
print(f'"A is greater" if a > b else "B is greater" : {"A is greater" if a > b else "a = b" if a == b else "B is greater"}')

if a > b:
    if a > c:
        print("A is greater")
    else:
        print("C is greator")
else:
    if b > c:
        print("B is greator")
    else:
        print("C is greator")

if c < b and c < a:
    print("C is smaller")
elif b < a and b < c:
    print("B is smaller")
else:
    print("A is smaller")



a = int(input("Enter an integer : "))
match a:                                    # match case, basically switch case
    case 1:
        print("Input is 1")
    case 2:
        print("Input is 2")
    case 3:
        print("Input is 3")
    case _:                                 # default case
        print("Input is not 1, 2, or 3")