# Zadanie 2

init = int(input('Enter start num: '))

j = init + 1
while True:
    for i in range(2, j):
        if j % i == 0:
            j += 1
            break
    else:
        print(j)
        break
