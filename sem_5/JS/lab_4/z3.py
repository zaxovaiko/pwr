# Zadanie 3

import z2

if __name__ == "__main__":
    init = int(input('Enter initial value: '))
    k = int(input('Enter number count (k): '))

    while k != 0:
        init = z2.next_prime(init) + 1
        k -= 1
