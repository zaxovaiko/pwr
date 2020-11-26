import uuid
import datetime as dt

class Osoba:
  def __init__(self, imiona, nazwisko, data_urodzenia):
    self.__imiona = [imiona] if type(imiona) == str else imiona[:3] if type(imiona) == list else []
    self.__nazwisko = nazwisko
    self.__data_urodzenia = data_urodzenia
    self.__id = str(uuid.uuid4())

  @property
  def nazwisko(self):
    return self.__nazwisko

  @property
  def wiek(self):
    return int(dt.date.today().year - dt.datetime.strptime(self.__data_urodzenia, '%d.%m.%Y').year)

  def __str__(self):
    return '[{}] {:>15} {:15} {:>10} lat'.format(self.__id[:4], self.__imiona[0], self.__nazwisko, self.wiek)
