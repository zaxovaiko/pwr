from random import randint
from Pracownik import Pracownik
from Student import Student
from Przedmioty import Przedmioty


def wypisz_studentow(studenty):
  # Prints all students in alphabetical order
  print(' Studenty '.center(70, '='))
  [print(s) for s in sorted(studenty, key=lambda x: x.nazwisko)]


def wypisz_pracownikow(pracowniki):
  # Prints all workers in alphabetical order
  print(' Pracowniki '.center(70, '='))
  [print(s) for s in sorted(pracowniki, key=lambda x: x.nazwisko)]


def wypisz_studentow_wg_sredniej(studenty):
  # Prints all students in custom order by avg mark
  print(' Lista studentow wg sredniej oceny '.center(70, '='))
  [print(x) for x in sorted(studenty, key=lambda y: y.daj_srednia_studiow())[::-1]]


def max_ocenione_publikacji(pracowniki):
  # Prints one or more workers with the biggest mark
  print(' Pracownik z najwieksza ocena '.center(70, '='))

  _sum = lambda y: sum(map(lambda x: x[1], y.publikacje))
  
  prac = sorted(filter(lambda x: x.wiek > 40 and x.wiek < 50, pracowniki), key=_sum)[::-1]
  [print(i) for i in filter(lambda y: _sum(y) == _sum(prac[0]), prac)]


def read_lines(filename):
    return open(filename).read().split('\n')


if __name__ == '__main__':
  # Read data
  studenty = [Student(*x.split(',')) for x in read_lines('data/students.csv')]
  pracowniki = [Pracownik(*x.split(',')) for x in read_lines('data/workers.csv')]
  
  # Read subjects
  for s in studenty:
    for p in read_lines('data/subjects.csv'):
      s.przedmioty.dopisz_przedmiot(*p.split(','))
      s.dopisz_ocene(randint(2, 5), p.split(',')[1])

  # Read publications
  for i, p in enumerate(open('data/publications.csv').read().split('\n')):
    if i // 5 >= len(pracowniki): break
    pracowniki[i // 5].dopisz_publikacje([*map(int, p.split(','))])

  # Write data
  print()
  max_ocenione_publikacji(pracowniki)
  wypisz_studentow(studenty)
  wypisz_pracownikow(pracowniki)
  wypisz_studentow_wg_sredniej(studenty)