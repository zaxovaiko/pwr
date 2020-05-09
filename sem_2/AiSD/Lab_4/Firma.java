package Lab_4;

class Firma {
    private ListQueue<Magazyn> magazyny = new ListQueue<>();

    Firma(int magazyny) {
        for (int i = 0; i < magazyny; i++) {
            this.magazyny.insert(new Magazyn(i + 1));
        }
    }

    void sumaWszystkichKwot() {
        double suma = 0;
        for (int i = 0; i < magazyny.getRozmiar(); i++) {
            Magazyn magazyn = (Magazyn) magazyny.get(i);
            System.out.println(magazyn);
            magazyn.wszystkieZamowienia();
            suma += magazyn.ileMagazynZarobil();
            System.out.printf("Suma wszystkich zakupow w tym magazynie: %3.2f$\n\n", magazyn.ileMagazynZarobil());
        }
        System.out.printf("Suma wszystkich kwot: %3.2f$", suma);
    }
}
