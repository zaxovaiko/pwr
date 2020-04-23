package Lab_4;

import java.util.Random;

class Zamowienie {
    private String nazwa;
    private int ilosc;
    private double cena;

    Zamowienie() {
        nazwa = "Produkt_" + (char)(new Random().nextInt(25) + 65);
        ilosc = new Random().nextInt(20) + 1;
        cena = Math.round(Math.random() * new Random().nextInt(5) * 100) / 100.0 + 1;
    }

    double suma() {
        return cena * ilosc;
    }

    @Override
    public String toString() {
        return String.format("\t%s\t%s szt.\t%3.2f$", nazwa, ilosc, cena);
    }
}
