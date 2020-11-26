from distance import LevenshteinDistance

class Przedmioty:
  def __init__(self):
    self.__przedmioty = {}

  def daj_kod(self, nazwa):
    nazwy = [x for x in self.__przedmioty.items() if LevenshteinDistance(x[1], nazwa) < 2]
    return None if len(nazwy) > 1 or len(nazwy) == 0 else nazwy[0][0]

  def dopisz_przedmiot(self, kod, nazwa):
    if kod in self.__przedmioty or nazwa in self.__przedmioty.values():
      return -1
    self.__przedmioty[kod] = nazwa
    return len(self.__przedmioty)

  def daj_przedmiot(self, kod):
    return self.__przedmioty[kod] if kod in self.__przedmioty.keys() else None

  def __str__(self):
    return '\n'.join('[{}]:\t{}'.format(*x) for x in self.__przedmioty.items())
