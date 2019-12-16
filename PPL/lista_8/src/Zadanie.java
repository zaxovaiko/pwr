public class Zadanie {
    private String nazwa;
    private String tryb;
    private String status = "WPrzygotowaniu";
    private Pracownik pracownik;

    public Zadanie(String nazwa, String tryb) {
        this.tryb = tryb;
        this.nazwa = nazwa;
    }

    public void setPracownik(Pracownik p) {
        pracownik = p;
        status = "WToku";
    }

    public void finish() throws Exception {
        if (status.equals("WToku")) {
            status = "Zakonczone";
            return;
        }

        throw new Exception("Zadanie juz skonczone.");
    }

    public Pracownik getPracownik() {
        return pracownik;
    }

    public String getStatus() {
        return status;
    }

    public String getTryb() {
        return tryb;
    }

    public String getNazwa() {
        return nazwa;
    }

    @Override
    public String toString() {
        return "Zadanie\n" +
                "\tnazwa: " + nazwa + "\n" +
                "\ttryb: " + tryb + "\n" +
                "\tstatus: " + status + "\n" +
                "\tpracownik: " + (pracownik == null ? "BRAK" : pracownik.getPesel()) + "\n";
    }
}
