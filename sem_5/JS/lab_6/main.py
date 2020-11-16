import Przypadki_swiat

if __name__ == '__main__':
    ps = Przypadki_swiat.Przypadki_swiat()
    ps.zczytajPlik('Covid_1.txt')

    def p1():
        print('Kraj o największej liczbie zgonów: ',
              ps.kraje.getNazwe(max([*ps.kraje.przypadki.values()], key=lambda x: x.lacznie_zgony).kodKraju))


    def p2():
        print('Kontynent o największej liczbie przypadków: ', end='')
        kontynenty = {}
        for i in [*ps.kraje.przypadki.values()]:
            if i.kontynent not in kontynenty:
                kontynenty[i.kontynent] = 0
            kontynenty[i.kontynent] += i.lacznie_zachorowania
        print(max(kontynenty, key=kontynenty.get))


    def p3():
        print('Najgorszy dzień świata (największa liczba zgonów przypadków na swiecie): ', end='')
        days = {}
        for d in [j for i in ps.kraje.przypadki.values() for j in i.przypadki]:
            if d.dzien not in days:
                days[d.dzien] = 0
            days[d.dzien] += d.zachorowania
        print(max(days, key=days.get))


    def p4():
        print('Najgorszy dzień dla każdego kontynentu:')
        kontynenty = {}
        for i in [*ps.kraje.przypadki.values()]:
            if i.kontynent not in kontynenty:
                kontynenty[i.kontynent] = []
            for j in i.przypadki:
                kontynenty[i.kontynent].append(j)
        for k in kontynenty:
            print('\t{:40s} - {}'.format(k, max(kontynenty[k], key=lambda x: x.zachorowania).dzien))


    def p5():
        print('Najgorszy dzień dla każdego kraju: ')
        for i in ps.kraje.przypadki.values():
            print('\t{:40s} - {}'.format(ps.kraje.getNazwe(i.kodKraju),
                                       max(i.przypadki, key=lambda x: x.zachorowania).dzien))

    p1()
    p2()
    p3()
    p4()
    p5()
