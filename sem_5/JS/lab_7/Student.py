from Osoba import Osoba
from Przedmioty import Przedmioty

class Student(Osoba):
  def __init__(self, imionia, nazwisko, data_urodzenia):
    Osoba.__init__(self, imionia, nazwisko, data_urodzenia)
    self.__przedmioty = Przedmioty()
    self.__oceny = {}

  @property
  def przedmioty(self):
    return self.__przedmioty

  def dopisz_ocene(self, ocena, nazwa_przedmiotu):
    kod = self.__przedmioty.daj_kod(nazwa_przedmiotu)
    if kod and kod in self.__oceny and self.__oceny[kod] == 2:
      self.__oceny[kod] = [2, ocena]
      return
    if kod and kod not in self.__oceny:
      self.__oceny[kod] = ocena

  def daj_srednia_studiow(self):
    return round(sum([o if type(o) == int else sum(o) for o in self.__oceny.values()]) / len(self.__oceny), 2)

  def __str__(self):
    return '{:<10}'.format(self.daj_srednia_studiow()) + super().__str__() # + ''.join(['\nOcena: {}\tPrzedmiot: {}'.format(ocena, self.__przedmioty.daj_przedmiot(kod)) for kod, ocena in self.__oceny.items()]) + '\n'
