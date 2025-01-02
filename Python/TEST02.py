limit = int(input("Enter the limit : "))

p = [i for i in range(2, limit)]

c = 0
k = 0

for i in p:
    #print(p)
    dp = p.copy()
    for j in p:
        if j != i and j % i == 0:
            p.remove(j)
            #k += 1
    if dp == p:
        break
    #c += 1

print(p)
#print(f"c = {c}\nk = {k}")
print(len(p))