from utils import levenshtein_distance


class Znaczniki:
    MAX_DL = 20
    MIN_DL = 3

    def __init__(self):
        self.akceptowane = []
        self.odrzucone = []

    def dopisz_ciag(self, ciag):
        if ciag in self.akceptowane or ciag in self.odrzucone:
            raise Exception('Ciag juz jest w tabele')

        if ciag.count('_') > 2 or len(ciag) > self.MAX_DL or len(ciag) < self.MIN_DL:
            self.odrzucone.append(ciag)
            raise Exception('Bledny ciag')

        self.akceptowane.append(ciag)

    def daj_ciag(self, ciag, odleglosc):
        return list(filter(lambda x: levenshtein_distance(x, ciag) < odleglosc))

    def daj_akceptowane(self, lista_ciagow):
        return list(filter(lambda x: x in self.akceptowane, lista_ciagow))

    def daj_odrzucone(self, lista_ciagow):
        return list(filter(lambda x: x in self.odrzucone, lista_ciagow))

    def __str__(self):
        return 'znaczniki'
