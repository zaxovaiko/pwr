package Lab_4;

public class ListQueue<T> implements IQueue {

    private class Element {
        private T znaczenie;
        private Element nastepny;

        Element(T znaczenie) {
            this.znaczenie = znaczenie;
        }

        Element getNastepny() {
            return nastepny;
        }

        void setNastepny(Element nastepny) {
            this.nastepny = nastepny;
        }

        T getZnaczenie() {
            return znaczenie;
        }
    }

    private Element glowa;
    private int rozmiar = 0;

    int getRozmiar() {
        return rozmiar;
    }

    @Override
    public Object get(int i) {
        Element e = glowa;

        int obecny = 0;
        while (obecny != i && e.getNastepny() != null) {
            e = e.getNastepny();
            obecny++;
        }

        return e.getZnaczenie();
    }

    @Override
    public void insert(Object e) {
        Element element = new Element((T) e);

        if (glowa == null) {
            glowa = element;
        } else {
            Element obecnyElement = glowa;
            while (obecnyElement.getNastepny() != null) {
                obecnyElement = obecnyElement.getNastepny();
            }

            obecnyElement.setNastepny(element);
        }
        rozmiar++;
    }

    @Override
    public void remove() {
        if (glowa != null) {
            glowa = glowa.getNastepny();
            rozmiar--;
        }
    }

    @Override
    public boolean isEmpty() {
        return glowa == null;
    }
}
