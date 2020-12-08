from Etykieta import Etykieta


class ZnacznikowaneDane:
    def __init__(self, ciagi=[]):
        self.etykieta = Etykieta(ciagi)

    def dopisz(self, etykieta):
        if etykieta == self.etykieta:
            return False
        self.etykieta = etykieta
        return True

    def __eq__(self, etykieta):
        # TODO: Return ciagi not bool value
        return ZnacznikowaneDane(self.etykieta if self.etykieta == etykieta else [])

    def __le__(self, etykieta):
        return ZnacznikowaneDane(self.etykieta if self.etykieta <= etykieta else [])

    def __ge__(self, etykieta):
        return ZnacznikowaneDane(self.etykieta if self.etykieta >= etykieta else [])

    def __ne__(self, etykieta):
        return ZnacznikowaneDane(self.etykieta if self.etykieta != etykieta else [])

    def __str__(self):
        return 'Nie ma akceptowanych ciagow.' if len(self.etykieta.znaczniki.akceptowane) == 0 else '\n'.join(self.etykieta.__str__())
