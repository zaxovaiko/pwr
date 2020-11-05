# Zadanie 6

import math


def generate_pi(n):
    pi = 2.
    for n in range(1, n):
        pi *= 4 * n ** 2 / (4 * n ** 2 - 1)

    print(math.pi - pi)


if __name__ == '__main__':
    [generate_pi(i) for i in [10, 100, 1000]]
