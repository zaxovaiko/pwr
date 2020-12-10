from Znaczniki import Znaczniki
from Etykieta import Etykieta
from ZnacznikowaneDane import ZnacznikowaneDane


if __name__ == '__main__':
    ciag1 = ['_', 'abc_', 'abcd_', '_abcde', '324#$']
    ciag2 = ['__abc', 'abc_', 'abcd_', '_abcde']

    e1 = Etykieta(ciag1)
    e2 = Etykieta(ciag2)

    # Etykiety
    print(' Etykiety '.center(40, '-'))
    print('Operation[+]:', e1 + e2)
    print('Operation[-]:', e1 - e2)
    print('Operation[*]:', e1 * e2)
    print('Operation[==]: {:>25}'.format(str(e1 == e2)))
    print('Operation[>=]: {:>25}'.format(str(e1 >= e2)))
    print('Operation[<=]: {:>25}'.format(str(e1 <= e2)))
    print('Operation[!=]: {:>25}'.format(str(e1 != e2)))
    print('-' * 40)
    print()

    z = ZnacznikowaneDane()
    z.dopisz(e2)

    # ZnacznikowaneDane
    print(' ZnacznikowaneDane '.center(45, '-'))
    print('Operacja[==]: ', z == e1)
    print('Operacja[>=]: ', z >= e1)
    print('Operacja[<=]: ', z <= e1)
    print('Operacja[!=]: ', z != e1)
    print('-' * 45)

# FIXME: Należy przygotować dane ilustrujące wszechstronnie działanie powyższych klas.
