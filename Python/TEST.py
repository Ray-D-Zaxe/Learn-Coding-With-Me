# Prime number generator

import time

limit = int(input("Enter the limit : "))


start = time.time()
s1 = time.perf_counter()

prime_list = [True] * limit
prime_list[0] = prime_list[1] = False

i = 2
while (i * i) <= limit:
    if prime_list[i]:
        for j in range((i * i), limit, i):
            prime_list[j] = False
    i += 1


primes = [i for i in range(2, limit) if prime_list[i]]

end = time.time()
e1 = time.perf_counter()

print(f"{primes[0]}, {primes[1]}, ..., {primes[-2]}, {primes[-1]}")
print(f"The no. of primes : {len(primes)}")
print(f"Time took for ({limit}) = {end - start} :or: {e1 - s1}")




