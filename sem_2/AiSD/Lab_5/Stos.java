package Lab_5;

public class Stos<T> implements Stack<T> {

    class E {
        private T value;
        private E prev;

        E(T v) {
            value = v;
        }
    }

    private E head = null;

    @Override
    public boolean empty() {
        return head == null;
    }

    @Override
    public void push(T e) {
        E newE = new E(e);
        newE.prev = head;
        head = newE;
    }

    @Override
    public T pop() {
        T v = head.value;
        head = head.prev;
        return v;
    }

    @Override
    public T peek() {
        return head.value;
    }
}