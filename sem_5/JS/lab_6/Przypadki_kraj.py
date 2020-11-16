import Covid_na_dzien


class Przypadki_kraj:
    def __init__(self, kod, kontynent):
        self.__przypadki = []
        self.kodKraju = kod
        self.kontynent = kontynent

    def dopisz(self, dzien):
        if dzien.dzien not in map(lambda x: x.dzien, self.__przypadki):
            self.__przypadki.append(dzien)

    def wprowadzLinie(self, linia):
        if self.kodKraju in linia:
            dzien = Covid_na_dzien.Covid_na_dzien()
            dzien.wprowadzLinie(linia)
            self.dopisz(dzien)

    def wprowadzDane(self):
        obj = Covid_na_dzien.Covid_na_dzien()
        obj.wprowadzDane()
        self.dopisz(obj)

    @property
    def przypadki(self):
        return self.__przypadki

    @property
    def lacznie_zgony(self):
        return sum(map(lambda x: x.zgony, self.__przypadki))

    @property
    def lacznie_zachorowania(self):
        return sum(map(lambda x: x.zachorowania, self.__przypadki))

    def __str__(self):
        return '{}\t{}\t{}\t{}'.format(self.kodKraju, len(self.__przypadki), self.lacznie_zgony, self.lacznie_zachorowania)
