package Lab_1;

import java.io.Serializable;

public abstract class Pracownik implements Serializable {
    private String nazwisko;
    private String imię;
    private long pesel;
    private String stanowisko;
    private int staż;

    public Pracownik(String nazwisko, String imię, long pesel, String stanowisko, int staż) {
        this.nazwisko = nazwisko;
        this.imię = imię;
        this.pesel = pesel;
        this.stanowisko = stanowisko;
        this.staż = staż;
    }

    public void wyświetl() {
        System.out.print(toString() + "\n");
    }

    @Override
    public String toString() {
        return String.format("| %-20s | %-20s | %15d | %-20s | %10d | ", nazwisko, imię, pesel, stanowisko, staż);
    }

    public abstract double pensja();
}
