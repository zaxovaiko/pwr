package Lab_6;

import java.io.Serializable;
import java.util.Random;

public class Pracownik implements Serializable {
    String imie, nazwisko, dataUrodzenia, stanowisko;
    int pesel;
    double staz, premia, pensja;

    public int getPesel() {
        return pesel;
    }

    public Pracownik() {
        String[] stanowiska = {"dyrektor", "księgowy", "sekretarka", "goniec", "kierowca"};
        int t = new Random().nextInt(20);

        this.pesel = new Random().nextInt(1000000) + 1;
        this.imie = "Imie_" + t;
        this.nazwisko = "Nazwisko_" + t;
        this.dataUrodzenia = new Random().nextInt(30) + 1970 + "." + (new Random().nextInt(12) + 1) + "." + (new Random().nextInt(30) + 1);
        this.stanowisko = stanowiska[new Random().nextInt(5)];
        this.staz = new Random().nextInt(30);
        this.pensja = new Random().nextInt(2000);

        if (staz >= 20) {
            premia = pensja * 0.2;
        } else if (staz >= 10) {
            premia = pensja * 0.1;
        } else {
            premia = 0;
        }
    }

    @Override
    public String toString() {
        return "Pracownik {" +
                "pesel='" + pesel + '\'' +
                ", imie='" + imie + '\'' +
                ", nazwisko='" + nazwisko + '\'' +
                ", dataUrodzenia='" + dataUrodzenia + '\'' +
                ", stanowisko='" + stanowisko + '\'' +
                ", staz=" + staz +
                ", premia=" + premia +
                ", pensja=" + pensja +
                '}';
    }
}
