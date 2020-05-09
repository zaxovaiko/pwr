package Lab_3;

import Lab_2.Karta;

public class Element {
    private Karta value;
    private Element next;

    public Element(Karta value) {
        this.value = value;
    }

    public Karta getValue() {
        return value;
    }

    public void setValue(Karta value) {
        this.value = value;
    }

    public Element getNext() {
        return next;
    }

    public void setNext(Element next) {
        this.next = next;
    }

    @Override
    public String toString() {
        return String.format("%s", value);
    }
}
