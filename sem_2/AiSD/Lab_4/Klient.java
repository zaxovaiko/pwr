package Lab_4;

import java.util.Random;

class Klient {
    private String name;
    private ListQueue<Zamowienie> zamowienia = new ListQueue<>();

    Klient() {
        this.name = "Klient_" + (char) (new Random().nextInt(25) + 65);
        for (int i = 0; i < new Random().nextInt(5) + 1; i++) {
            zamowienia.insert(new Zamowienie());
        }
    }

    @Override
    public String toString() {
        return name;
    }

    ListQueue<Zamowienie> getZamowienia() {
        return zamowienia;
    }
}
