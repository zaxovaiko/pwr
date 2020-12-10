from Znaczniki import Znaczniki


class Etykieta:
    def __init__(self, ciagi=[]):
        self.znaczniki = Znaczniki()
        for x in ciagi:
            try:
                self.znaczniki.dopisz_ciag(x)
            except Exception:
                pass

    def __add__(self, o):
        return Etykieta([*self.znaczniki.akceptowane, *o.znaczniki.akceptowane])

    def __mul__(self, o):
        return Etykieta(list(set(self.znaczniki.akceptowane).intersection(o.znaczniki.akceptowane)))

    def __sub__(self, o):
        return Etykieta(list(filter(lambda x: x not in o.znaczniki.akceptowane, self.znaczniki.akceptowane)))

    def __eq__(self, o):
        return set(self.znaczniki.akceptowane) == set(o.znaczniki.akceptowane)

    def __le__(self, o):
        return all(list(map(lambda x: x in o.znaczniki.akceptowane, self.znaczniki.akceptowane)))

    def __ge__(self, o):
        return all(list(map(lambda x: x in self.znaczniki.akceptowane, o.znaczniki.akceptowane)))

    def __ne__(self, o):
        return list(set(self.znaczniki.akceptowane).intersection(o.znaczniki.akceptowane)) == 0

    def __str__(self):
        return ', '.join(self.znaczniki.akceptowane)
