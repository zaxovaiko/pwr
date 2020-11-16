def LevenshteinDistance(s, t):
    n = range(0, len(s) + 1)

    for y in range(1, len(t) + 1):
        l, n = n, [y]
        for x in range(1, len(s) + 1):
            n.append(min(l[x] + 1, n[-1] + 1, l[x-1] + ((t[y-1] != s[x-1]) and 1 or 0)))

    return n[-1]