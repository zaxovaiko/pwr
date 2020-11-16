import distance
import Przypadki_kraj


class Nazwy_krajow:
    def __init__(self):
        self.__nazwy = {}
        self.przypadki = {}

    def zapiszPrzypadek(self, kod, linia):
        if kod in self.przypadki:
            self.przypadki[kod].wprowadzLinie(linia)

    @property
    def nazwy(self):
        return self.__nazwy

    def dopisz(self, kod, nazwa, kontynent):
        if kod in self.__nazwy or kod == '' or kod == ' ':
            return

        for val in self.__nazwy.values():
            if distance.LevenshteinDistance(nazwa, val) < 2:
                return

        self.__nazwy[kod] = nazwa
        self.przypadki[kod] = Przypadki_kraj.Przypadki_kraj(kod, kontynent)

    def getNazwe(self, kod):
        return self.__nazwy[kod] if kod in self.__nazwy else None

    def getKodKraju(self, nazwa):
        kody = [kraj for kraj in self.__nazwy.values() if distance.LevenshteinDistance(nazwa, kraj) < 2]
        return kody[0] if len(kody) == 1 else 'Niejednoznacznosc nazwy: %s kandydatow' % len(kody)
