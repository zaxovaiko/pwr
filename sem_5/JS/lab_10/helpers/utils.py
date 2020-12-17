def read_data_as_list(filename):
  return list(map(lambda x: x.split('\t'), open(filename).read().split('\n')[1:]))


def flt(value, index, symbols, array):
  return list(filter(lambda x: levenshtein_distance(x[index] if type(x) == list else x, str(value)) < symbols, array)) 


def levenshtein_distance(s, t):
  n = range(0, len(s) + 1)
  for y in range(1, len(t) + 1):
      l, n = n, [y]
      for x in range(1, len(s) + 1):
          n.append(min(l[x] + 1, n[-1] + 1, l[x-1] + ((t[y-1] != s[x-1]) and 1 or 0)))
  return n[-1]