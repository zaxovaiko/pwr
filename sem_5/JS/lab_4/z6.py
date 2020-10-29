# Zadanie 6

import functools
import math

# First solution
n = 80000000
pi = 2.
for n in range(1, n):
    pi *= 4 * n ** 2 / (4 * n ** 2 - 1)

print(pi, math.pi)
print(abs(math.pi - pi))

# Second solution
print(2 * functools.reduce(lambda x, y: x * y,
                           [float((4 * (i ** 2))) / ((4 * (i ** 2)) - 1) for i in range(1, 90000000)]))
