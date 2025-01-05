import time
limit = int(input("Enter the limit : "))

p = [i for i in range(2, limit)]

c = 0
k = 0

start = time.time()
s1 = time.perf_counter()

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

end = time.time()
e1 = time.perf_counter()

print(p)
#print(f"c = {c}\nk = {k}")
print(len(p))
print(f"Time took for ({limit}) = {end - start} :or: {e1 - s1}")
