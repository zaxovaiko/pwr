import time

t = time.time()
print(sum(map(lambda x: int(x.split('\t')[4]), open('Covid.txt').readlines()[1:])))
print(time.time() - t)