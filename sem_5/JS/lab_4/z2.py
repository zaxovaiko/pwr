# Zadanie 2


def next_prime(init):
    j = init + 1
    while True:
        for i in range(2, j):
            if j % i == 0:
                j += 1
                break
        else:
            print(j)
            return j


if __name__ == "__main__":
    next_prime(int(input('Enter start num: ')))
