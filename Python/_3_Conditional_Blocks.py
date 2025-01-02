a, b, c = 10, 20, 30
print(f'A is greater" if a > b else "B is greater" : {"A is greater" if a > b else "B is greater"}')

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