package Lab_4;

interface IQueue<T> {
    void insert(T e);
    void remove();
    T get(int i);
    boolean isEmpty();
}
