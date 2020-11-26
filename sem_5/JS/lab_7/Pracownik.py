from Osoba import Osoba

class Pracownik(Osoba):
  def __init__(self, imiona, nazwisko, data_urodzenia):
    Osoba.__init__(self, imiona, nazwisko, data_urodzenia)
    self.__publikacje = []

  @property
  def publikacje(self):
    return self.__publikacje

  def dopisz_publikacje(self, publikacja):
    self.__publikacje.append(publikacja)

  def daj_do_oceny(self):
    lata = sorted(self.daj_puste_lata())[:-5:-1]
    return sum([x[1] for x in self.__publikacje if x[0] in lata])

  def daj_puste_lata(self):
    return list(set(map(lambda x: x[0], self.__publikacje)))

  def __str__(self):
    return '{:<10}'.format(self.daj_do_oceny()) + super().__str__() # + ''.join(['\nRok: {}\tOcena: {}'.format(*x) for x in self.__publikacje]) + '\n'