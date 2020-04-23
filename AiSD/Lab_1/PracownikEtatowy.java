package Lab_1;

public class PracownikEtatowy extends Pracownik {
    private float etat;
    private double stawka;

    public PracownikEtatowy(String nazwisko, String imię, long pesel, String stanowisko, int staż, float etat, double stawka) {
        super(nazwisko, imię, pesel, stanowisko, staż);
        this.etat = etat;
        this.stawka = stawka;
    }

    @Override
    public double pensja() {
        return stawka * etat;
    }

    @Override
    public String toString() {
        return super.toString() + String.format("%10.2f |", pensja());
    }
}
