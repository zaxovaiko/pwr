package Lab_2;

public class Karta {
    private final String[] kolory = {"Kier", "Karo", "Trefl", "Pik"};
    private final String[] wartości = {"As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Walet", "Dama", "Król", "KARTA X"};

    private int kolor;
    private int wartość;
    private boolean znacznik;

    public Karta(int kolor, int wartość, boolean znacznik) {
        this.kolor = kolor;
        this.wartość = wartość;
        this.znacznik = znacznik;
    }

    public boolean getZnacznik() {
        return znacznik;
    }

    public int getKolor() {
        return kolor;
    }

    public int getWartość() {
        return wartość;
    }

    @Override
    public String toString() {
        if (wartość == 13) {
            return "{ }";
        }
        return wartości[wartość] + "[" + kolory[kolor] + "] " + (znacznik ? "#" : "");
    }

    @Override
    public boolean equals(Object o) {
        Karta karta = (Karta) o;
        return kolor == karta.kolor && wartość == karta.wartość && znacznik == karta.znacznik;
    }
}