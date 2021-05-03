class Player:
    def __init__(self, inverted=False, name='', color=''):
        self.field = [4, 4, 4, 4, 4, 4, 0]
        self.inverted = inverted
        self.color = color
        self.name = name

    def get_name(self):
        return self.color + 'Player ' + self.name

    def __str__(self):
        return self.color + ('\t' + '\t'.join(map(str, self.field)) if not self.inverted else '\t'.join(map(str, reversed(self.field))))
