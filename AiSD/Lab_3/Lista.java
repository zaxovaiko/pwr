package Lab_3;

import Lab_2.Karta;

public class Lista<E> implements IList<E> {
    private Element head = null;

    public void show() {
        if (head != null) {
            Element e = head;
            while (e.getNext() != null) {
                System.out.print(e + ",  ");
                e = e.getNext();
            }
            System.out.println(e);
        }
    }

    public void countOfClosed() {
        int count = 0;
        Element e = head;
        while (e != null) {
            if (e.getValue().getZnacznik()) {
                count++;
            }
            e = e.getNext();
        }

        System.out.println("Ilość otwartych: " + count);
        System.out.println("Ilość zakrytych: " + (size() - count));
    }

    @Override
    public boolean isEmpty() {
        return head == null;
    }

    @Override
    public void clear() {
        head = null;
    }

    @Override
    public int size() {
        int size = 1;
        Element e = head;
        while (e.getNext() != null) {
            size++;
            e = e.getNext();
        }
        return size;
    }

    @Override
    public boolean add(int index, E value) {
        Element _new = new Element((Karta) value);

        if (index < size()) {
            if (head == null) {
                head = _new;
            } else {
                int i = 0;
                Element cur = head;
                Element prev = head;

                if (index > 0) {
                    while (cur.getNext() != null && i++ != index) {
                        prev = cur;
                        cur = cur.getNext();
                    }

                    Element tmpcur = cur;
                    cur = _new;
                    cur.setNext(tmpcur);
                    prev.setNext(cur);
                } else {
                    Element tmpHead = head;
                    _new.setNext(tmpHead);
                    head = _new;
                }
            }
            return true;
        }

        add(value);
        return true;
    }

    @Override
    public boolean add(E value) {
        if (head == null) {
            head = new Element((Karta) value);
            return true;
        }
        Element e = head;
        while (e.getNext() != null) {
            e = e.getNext();
        }
        e.setNext(new Element((Karta) value));
        return true;
    }

    @Override
    public boolean contains(E value) {
        Element e = head;
        while (e.getNext() != null) {
            if (e.getValue().equals(value)) {
                return true;
            }
            e = e.getNext();
        }
        return false;
    }

    @Override
    public E get(int index) {
        if (index > size() || index < 0) {
            return null;
        }
        Element e = head;
        while (index > 0 && e != null) {
            index--;
            e = e.getNext();
        }
        return (E) e.getValue();
    }

    @Override
    public E set(int index, E value) {
        Element e = head;
        int i = 0;
        while (e.getNext() != null) {
            if (i == index) {
                e.setValue((Karta) value);
                return (E) e.getValue();
            }
            i++;
            e = e.getNext();
        }
        return null;
    }

    @Override
    public int indexOf(E value) {
        Element e = head;
        int index = 0;
        while (e != null) {
            if (e.getValue().equals(value)) {
                return index;
            }
            index++;
            e = e.getNext();
        }
        return -1;
    }

    @Override
    public E remove(int index) {
        if (head != null && index < size()) {
            Element cur = head;
            Element prev = head;
            int i = 0;

            if (index > 0) {
                while (cur.getNext() != null && i++ != index) {
                    prev = cur;
                    cur = cur.getNext();
                }

                prev.setNext(cur.getNext());
                return (E) cur.getValue();
            } else {
                head = head.getNext();
            }
        }
        return null;
    }

    @Override
    public boolean remove(E value) {
        Element e = head;
        while (e.getNext().getNext() != null) {
            if (e.getNext().getValue().equals(value)) {
                e.setNext(e.getNext().getNext());
                return true;
            }
            e = e.getNext();
        }
        return false;
    }
}
