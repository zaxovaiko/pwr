import java.util.Objects;

public class Pracownik {
    private String nazwisko;
    private String imie;
    private String pesel;
    private int placa;

    public Pracownik(String nazwisko, String imie, String pesel, int placa) {
        this.nazwisko = nazwisko;
        this.imie = imie;
        this.pesel = pesel;
        this.placa = placa;
    }

    public void dacPodwyzke(int procent) {
        placa += placa * procent / 100;
    }

    public String getNazwisko() {
        return nazwisko;
    }

    public String getImie() {
        return imie;
    }

    public String getPesel() {
        return pesel;
    }

    public int getPlaca() {
        return placa;
    }

    public void setNazwisko(String nazwisko) {
        this.nazwisko = nazwisko;
    }

    public void setImie(String imie) {
        this.imie = imie;
    }

    public void setPesel(String pesel) {
        this.pesel = pesel;
    }

    public void setPlaca(int placa) {
        this.placa = placa;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Pracownik)) return false;
        Pracownik pracownik = (Pracownik) o;
        return placa == pracownik.placa &&
                nazwisko.equals(pracownik.nazwisko) &&
                imie.equals(pracownik.imie) &&
                pesel.equals(pracownik.pesel);
    }

    @Override
    public int hashCode() {
        return Objects.hash(nazwisko, imie, pesel, placa);
    }

    @Override
    public String toString() {
        return "Pracownik\n" +
                "\tnazwisko: " + nazwisko + '\n' +
                "\timie: " + imie + '\n' +
                "\tpesel: " + pesel + '\n' +
                "\tplaca: " + placa + "\n";
    }
}
