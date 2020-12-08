from Znaczniki import Znaczniki
from Etykieta import Etykieta
from ZnacznikowaneDane import ZnacznikowaneDane


if __name__ == '__main__':
    ciag1 = ['_', 'abc_', 'abcd_', '_abcde']
    ciag2 = ['__abc', 'abc_', 'abcd_e', 'a_abcde']

    e1 = Etykieta(ciag1)
    e2 = Etykieta(ciag2)

    z = ZnacznikowaneDane()
    z.dopisz(e2)

    print('Operacja == : ')
    print(z == e1)
    print()

    print('Operacja >= : ')
    print(z >= e1)
    print()

    print('Operacja <= : ')
    print(z <= e1)
    print()

    print('Operacja != : ')
    print(z != e1)
    print()
