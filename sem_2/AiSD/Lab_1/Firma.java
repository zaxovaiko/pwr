package Lab_1;

public class Firma implements Iterator {

    private int pos = 0;
    private Pracownik[] pracowniki;

    public Firma(Pracownik[] pracowniki) {
        this.pracowniki = pracowniki;
    }

    @Override
    public void prev() {
        System.out.println(pracowniki[pos]);
        --pos;
    }

    @Override
    public void next() {
        System.out.println(pracowniki[pos]);
        ++pos;
    }

    @Override
    public void first() {
        System.out.println(pracowniki[0]);
    }

    @Override
    public void last() {
        System.out.println(pracowniki[pracowniki.length - 1]);
    }

    @Override
    public boolean isDone() {
        return pos < 0 || pos >= pracowniki.length;
    }

    @Override
    public Pracownik current() {
        return pracowniki[pos];
    }

    @Override
    public boolean hasNext() {
        return pos + 1 < pracowniki.length;
    }

    @Override
    public boolean hasPrev() {
        return pos - 1 >= 0;
    }
}
