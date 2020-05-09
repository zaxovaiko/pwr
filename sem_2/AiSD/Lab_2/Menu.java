package Lab_2;

import Lab_3.Lista;

import java.util.*;

class Menu {
    private final String[] kolory = {"Kier", "Karo", "Trefl", "Pik"};
    private final String[] wartości = {"As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Walet", "Dama", "Król", "KARTA X"};

    private ArrayList<Karta> karty = new ArrayList<>();
    private Lista<Karta> lista = new Lista<>();

    void utworzyćListę() {
        lista.clear();
        karty.clear();

        int rv, rk;
        boolean znacznik;

        karty.add(new Karta(0, 0, false));
        karty.add(new Karta(0, 0, false));
        karty.add(new Karta(0, 0, false));

        lista.add(new Karta(0, 0, false));
        lista.add(new Karta(0, 0, false));
        lista.add(new Karta(0, 0, false));

        while ((rv = new Random().nextInt(14)) > 0) {
            rk = new Random().nextInt(4);

            if (rv == 13) {
                znacznik = true;
                Karta karta = new Karta(rk, rv, true);
                karty.add(karta);
                lista.add(karta);
                return;
            } else {
                znacznik = false;
            }

            Karta karta = new Karta(rk, rv, znacznik);

            if (karty.size() > 0) {
                int index = karty.size(), i = 0;
                for (Karta card : karty) {
                    if (karta.getWartość() < card.getWartość()) {
                        index = i;
                        break;
                    } else if (karta.getWartość() == card.getWartość()) {
                        if (karta.getKolor() < card.getKolor()) {
                            index = i;
                            break;
                        } else if (karta.getKolor() == card.getKolor()) {
                            if (karty.size() <= i + 1) {
                                index = i + 1;
                                break;
                            } else if (karty.get(i + 1).getKolor() > card.getKolor()) {
                                index = i;
                                break;
                            }
                        }
                    }
                    i++;
                }
                karty.add(index, karta);
                lista.add(index, karta);
            } else {
                karty.add(karta);
                lista.add(karta);
            }
        }
    }

    void usunućPowtarzające() {
        if (karty != null && karty.size() != 0) {
            ArrayList<Karta> noweKarty = new ArrayList<>();
            Lista<Karta> lista = new Lista<>();

            boolean[][] wartosci = new boolean[14][];
            // For each card
            for (Karta karta : karty) {
                int indeksWartości = karta.getWartość();

                if (wartosci[indeksWartości] != null) {
                    if (!wartosci[indeksWartości][karta.getKolor()]) {
                        wartosci[indeksWartości][karta.getKolor()] = true;
                        // to local
                        noweKarty.add(karta);
                        lista.add(karta);
                    }
                } else {
                    boolean[] kolory = new boolean[4];
                    wartosci[indeksWartości] = kolory;
                    wartosci[indeksWartości][karta.getKolor()] = true;
                    // to local
                    noweKarty.add(karta);
                    lista.add(karta);
                }
            }

            karty.clear();
            karty.addAll(noweKarty);
            this.lista.clear();
            this.lista = lista;
        }
    }

    void wyświetlićListę() {
        System.out.println("Wszystkie karty: (1 wiersz - ArrayList, 2 - LinkedList)");

        // Print ArrayList with Iterator
        Iterator iterator = karty.listIterator();
        while (iterator.hasNext()) {
            Karta karta = (Karta) iterator.next();
            System.out.print(karta + ",  ");
        }
        System.out.println();

        // Print LinkedList
        lista.show();
    }

    void wyświetlićLiczbęElementów() {
        System.out.printf("Liczba elementów: %d\n", karty.size());
        System.out.printf("Liczba elementów listy wiązanej: %d\n", lista.size());
    }

    void wyświetlenieKartoWartości(String wartość) {
        System.out.printf("Wszystkie karty o wartości %s (ArrayList): ", wartość);
        Iterator iterator = karty.listIterator();
        while (iterator.hasNext()) {
            Karta karta = (Karta) iterator.next();
            if (wartości[karta.getWartość()].equals(wartość)) {
                System.out.print(wartości[karta.getWartość()] + "-" + kolory[karta.getKolor()] + "\t");
            }
        }
        System.out.println();

        System.out.printf("Wszystkie karty o wartości %s (LinkedList): ", wartość);
        int i = 0;
        while (i < lista.size()) {
            Karta karta = lista.get(i);
            if (wartości[karta.getWartość()].equals(wartość)) {
                System.out.print(wartości[karta.getWartość()] + "-" + kolory[karta.getKolor()] + "\t");
            }
            i++;
        }
    }

    void wyświetlenieKartoKolorze(String kolor) {
        System.out.printf("Wszystkie karty o kolorze %s: ", kolor);
        Iterator iterator = karty.listIterator();
        while (iterator.hasNext()) {
            Karta karta = (Karta) iterator.next();
            if (kolory[karta.getKolor()].equals(kolor)) {
                System.out.print(wartości[karta.getWartość()] + "-" + kolory[karta.getKolor()] + ",  ");
            }
        }
        System.out.println();

        // LinkedList
        System.out.printf("Wszystkie karty o kolorze %s (LinkedList): ", kolor);
        int i = 0;
        while (i < lista.size()) {
            Karta karta = lista.get(i);
            if (kolory[karta.getKolor()].equals(kolor)) {
                System.out.print(wartości[karta.getWartość()] + "-" + kolory[karta.getKolor()] + ",  ");
            }
            i++;
        }
    }

    public void ilośćOdkrytychiZakrytychKart() {
        lista.countOfClosed();
    }
}
