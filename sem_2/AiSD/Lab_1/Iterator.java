package Lab_1;

public interface Iterator {
    void prev();
    void next();
    void first();
    void last();
    boolean hasNext();
    boolean hasPrev();
    boolean isDone();
    Pracownik current();
}
