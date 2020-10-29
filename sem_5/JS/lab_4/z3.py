# Zadanie 3

init = int(input('Enter start num: '))
k = int(input('Enter prime numbers count: '))

j = init + 1
while k != 0:
    for i in range(2, j):
        if j % i == 0:
            j += 1
            break
    else:
        print(j)
        j += 1
        k -= 1
