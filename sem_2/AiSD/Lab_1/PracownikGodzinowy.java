package Lab_1;

public class PracownikGodzinowy extends Pracownik {
    private double stawka;
    private int liczba_godz;

    public PracownikGodzinowy(String nazwisko, String imię, long pesel, String stanowisko, int staż, double stawka, int liczba_godz) {
        super(nazwisko, imię, pesel, stanowisko, staż);
        this.stawka = stawka;
        this.liczba_godz = liczba_godz;
    }

    @Override
    public double pensja() {
        return stawka* liczba_godz;
    }

    @Override
    public String toString() {
        return super.toString() + String.format("%10.2f |", pensja());
    }
}
