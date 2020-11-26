class Covid_na_dzien:
    def __init__(self):
        self.__dzien = None
        self.__zachorowania = None
        self.__zgony = None

    def wprowadzLinie(self, linia):
        data = linia.split('\t')
        self.__dzien = data[0]
        self.__zachorowania = int(data[4])
        self.__zgony = int(data[5])

    def wprowadzDane(self):
        self.__dzien = input('Wprowadz date: ')
        self.__zachorowania = int(input('Wprowadz ilosc zachorowan: '))
        self.__zgony = int(input('Wprowadz ilosc zgonow: '))

    @property
    def dzien(self):
        return self.__dzien

    @property
    def zachorowania(self):
        return self.__zachorowania

    @property
    def zgony(self):
        return self.__zgony

    def __str__(self):
        return '{}\t{}\t{}'.format(self.__dzien.replace('.', '/'), self.__zachorowania, self.__zgony)