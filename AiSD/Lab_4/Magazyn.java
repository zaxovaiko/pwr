package Lab_4;

import java.util.Random;

class Magazyn {
    private String nazwa;
    private ListQueue<Klient> klienci = new ListQueue<>();
    private double sumaZakupow = 0;

    Magazyn(int numer) {
        nazwa = "Magazyn_" + numer;
        for (int i = 0; i < new Random().nextInt(5) + 1; i++) {
            this.klienci.insert(new Klient());
        }
    }

    void wszystkieZamowienia() {
        for (int i = 0; i < klienci.getRozmiar(); i++) {
            Klient klient = (Klient) klienci.get(i);

            double sumaZakupow = 0;
            ListQueue<Zamowienie> zamowienia = klient.getZamowienia();
            System.out.println("\t" + klient + ":");

            for (int j = 0; j < zamowienia.getRozmiar(); j++) {
                Zamowienie zamowienie = (Zamowienie) zamowienia.get(j);
                sumaZakupow += zamowienie.suma();
                System.out.println("\t" + zamowienie);
            }

            System.out.printf("\t\tSuma zakupów klienta: %3.2f$\n", sumaZakupow);
            this.sumaZakupow += sumaZakupow;
        }
    }

    double ileMagazynZarobil() {
        return sumaZakupow;
    }

    @Override
    public String toString() {
        return nazwa;
    }
}
