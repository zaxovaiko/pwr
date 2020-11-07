import time

country = input('Enter country: ')
t = time.time()


def mapFunc(x):
    arr = x.split('\t')
    return int(arr[4]) if country == arr[6] else 0


print(sum(map(mapFunc, open('Covid.txt').readlines()[1:])))
print(time.time() - t)