public class Specjalista extends Pracownik {
    private int premia;

    public Specjalista(String nazwisko, String imie, String pesel, int placa) {
        super(nazwisko, imie, pesel, placa);
    }

    public int getPremia() {
        return premia;
    }

    public void setPremia(int premia) {
        this.premia = premia;
    }

    @Override
    public String toString() {
        return "Specjalista\n" +
                "\tnazwisko: " + getNazwisko() + '\n' +
                "\timie: " + getImie() + '\n' +
                "\tpesel: " + getPesel() + '\n' +
                "\tplaca: " + getPlaca() + "\n" +
                "\tpremia: " + premia + "\n";
    }
}