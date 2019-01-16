import math
import cProfile

# python -m timeit -n 100 -s "import task4_1" "task4_2_1.f_simpleInt()"

n = int(input("введите n = "))
k=n


def f_simpleInt():
    nn = 2
    while 1:
        nn += 1
        for i in range(2, nn):
            if nn % i == 0:
                break
            elif i == nn - 1:
                yield nn


genSimInt = f_simpleInt()

for i in range(k):
    si = next(genSimInt)

print(si)

#cProfile.run('f_simpleInt()')
# 1    0.000    0.000    0.000    0.000 task4_2_1.py:10(f_simpleInt)



# Решето Эратосфена
def bit_sieve(n):
    if n < 2:
        return []
    bits = [1] * n
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(2, sqrt_n):
        if bits[i - 2]:
            for j in range(i + i, n + 1, i):
                bits[j - 2] = 0
    return bits

sieve = bit_sieve(int(1.5 * k * math.log(k)) + 1)
i = 0
while k:
    k -= sieve[i]
    i += 1
print(i + 1)

# 100 loops, best of 3: 2.19 usec per loop (5)
# 100 loops, best of 3: 2.55 usec per loop (10)
# 100 loops, best of 3: 4.23 usec per loop (20)
# 100 loops, best of 3: 10.2 usec per loop (100)
# 100 loops, best of 3: 133 usec per loop (1000)

#cProfile.run('bit_sieve(100)')
# 1    0.000    0.000    0.000    0.000 task4_2_1.py:34(bit_sieve)
# 1    0.000    0.000    0.000    0.000 task4_2_1.py:34(bit_sieve)



