package Lab_3;

public interface IList<E> {
    boolean isEmpty();
    void clear();
    int size();
    boolean add(int index, E value);
    boolean add(E value);
    boolean contains(E value);
    E get(int index);
    E set(int index, E value);
    int indexOf(E value);
    E remove(int index);
    boolean remove(E value);
}
