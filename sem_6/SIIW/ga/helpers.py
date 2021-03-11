def read_file(filename):
    with open('./data/' + filename) as f:
        size = list(map(int, f.readline().split(';')))
        coordinates = [list(map(int, i.split(';'))) for i in f.readlines()]
        return size, coordinates