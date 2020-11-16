import Nazwy_krajow


class Przypadki_swiat:
    def __init__(self):
        self.kraje = None

    def zczytajPlik(self, filename):
        rows = open(filename).readlines()
        self.kraje = Nazwy_krajow.Nazwy_krajow()

        for row in rows[1:]:
            data = row.split('\t')
            self.kraje.dopisz(data[8], data[6], data[10])

        for row in rows[1:]:
            self.kraje.zapiszPrzypadek(row.split('\t')[8], row)
