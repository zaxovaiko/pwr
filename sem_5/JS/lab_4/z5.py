# Zadanie 5


def calc(arr):
    arr_copy = list(filter(lambda x: type(x) == float or type(x) == int, arr))
    a = len(arr_copy)
    b = sum(arr_copy) / a
    c = sum(map(lambda x: (x - b) ** 2, arr_copy)) / a
    d = min(arr_copy)
    e = max(arr_copy)
    return a, b, c, d, e


print(calc([1, 2, 3.5, 4, 'world', 5, 6, 7.5, 8, 'hello']))
