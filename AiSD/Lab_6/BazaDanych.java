package Lab_6;

import java.io.*;
import java.util.ArrayList;
import java.util.Comparator;

class BazaDanych {
    class E {
        E next;
        E prev;
        Pracownik value;

        E(Pracownik p) {
            value = p;
        }
    }

    private E head = null;

    void read() throws IOException, ClassNotFoundException {
        ObjectInputStream br = new ObjectInputStream(new FileInputStream("output.txt"));
        head = null;
        Object obj;
        try {
            while ((obj = br.readObject()) != null) {
                dodac((Pracownik) obj);
            }
        } catch (EOFException e) {
            // error
        }

        System.out.println("Zczytano wszystko z pliku.");
        br.close();
    }

    void add(Pracownik p) {
        ArrayList<Pracownik> pracowniks = new ArrayList<>();

        pracowniks.add(p);
        E e = head;
        while (e != null) {
            pracowniks.add(e.value);
            e = e.next;
        }

        pracowniks.sort(Comparator.comparing(Pracownik::getPesel));
        head = null;
        for (Pracownik pracownik : pracowniks) {
            dodac(pracownik);
        }

        System.out.println("Pracownika " + p.pesel + " dodano do bazy.");
    }

    private void dodac(Pracownik p) {
        E new_node = new E(p), last = head;
        new_node.next = null;

        if (head == null) {
            new_node.prev = null;
            head = new_node;
        } else {
            while (last.next != null)
                last = last.next;

            last.next = new_node;
            new_node.prev = last;
        }
    }

    void show(int pesel) {
        E e = head;
        while (e != null) {
            if (e.value.pesel == pesel) {
                System.out.println(e.value);
                return;
            }
            e = e.next;
        }
        System.out.println("Pracownika nie znaleziono.");
    }

    void remove(int pesel) {
        E e = head;
        while (e != null) {
            if (e.value.pesel == pesel) {
                System.out.println("Pracownika " + e.value.pesel + "usunieto.");

                if (e.prev == null) {
                    head = e.next;
                    e.next.prev = null;
                    return;
                }

                if (e.next == null) {
                    e.prev.next = null;
                    return;
                }

                e.prev.next = e.next;
                e.next.prev = e.prev;
                return;
            }
            e = e.next;
        }
        System.out.println("Pracownika nie znaleziono (remove).");
    }

    void showAll() {
        System.out.println("Wszystkie pracowniki:");
        E e = head;
        while (e != null) {
            System.out.println(e.value);
            e = e.next;
        }
    }

    void update(int pesel, Pracownik r) {
        E e = head;
        while (e != null) {
            if (e.value.pesel == pesel) {
                e.value = r;
                System.out.println("Dane pracownika aktualizowano.");
                return;
            }
            e = e.next;
        }
        System.out.println("Pracownika nie znaleziono (update).");
    }

    void write() throws IOException {
        ObjectOutputStream bw = new ObjectOutputStream(new FileOutputStream("output.txt"));

        E e = head;
        while (e != null) {
            bw.writeObject(e.value);
            e = e.next;
        }
        System.out.println("Zapis do pliku zrobiono.");
        bw.close();
    }

    void averagePensja() {
        double sum = 0;
        E e = head;
        int l = 0;
        while (e != null) {
            sum += e.value.pensja;
            e = e.next;
            l++;
        }
        System.out.println("\nSriednia pensja na firmie: " + sum / l);

        e = head;
        int count = 0;
        while (e != null) {
            if (e.value.pensja < (sum / l)) {
                count++;
            }
            e = e.next;
        }

        System.out.println("Ilość pracownikó, których pensja jest mniejsza od " + (sum/l) + ": " + count);
    }
}
