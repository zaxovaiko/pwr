package Lab_1;

import java.io.*;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    private static Pracownik[] pracowniki = new Pracownik[1];

    public static void main(String[] args) {
        sczytać();
        zapisaćPlik();
        sczytaćPlik();
        wyświetlTabelkę();
    }

    /**
     * Odczytywanie pliku z Pracownikami.
     */
    static void sczytaćPlik() {
        try {
            ObjectInputStream stream = new ObjectInputStream(new FileInputStream("Lab_1.output.txt"));
            pracowniki = new Pracownik[stream.read()];

            int k = 0;
            while (true) {
                try {
                    pracowniki[k++] = (Pracownik)stream.readObject();
                } catch (EOFException e) {
                    break;
                }
            }
            stream.close();
            System.out.println("\nWyświetlenie po odczytywaniu z pliku:");
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }

    /**
     * Zapisywanie Pracowników do pliku.
     */
    static void zapisaćPlik() {
        try {
            ObjectOutputStream stream = new ObjectOutputStream(new FileOutputStream("Lab_1.output.txt"));
            stream.write(pracowniki.length);
            for (Pracownik pracownik : pracowniki) {
                stream.writeObject(pracownik);
            }
            stream.close();
            wyświetlTabelkę();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * Sczytywanie informacji o Pracownikach z klawiatury.
     */
    static void sczytać() {
        Scanner scanner = new Scanner(System.in);
        String linia;
        String[] argumenty;

        int i = 0;
        while (!(linia = scanner.nextLine()).equals("END")) {
            Pracownik[] _pracowniki = new Pracownik[i + 2];
            argumenty = linia.split(",\\s");
            if (argumenty[0].equals("E")) {
                pracowniki[i] = new PracownikEtatowy(
                        argumenty[1],                       // Nazwisko
                        argumenty[2],                       // Imię
                        Integer.parseInt(argumenty[3]),     // PESEL
                        argumenty[4],                       // Stanowisko
                        Integer.parseInt(argumenty[5]),     // Staż
                        Float.parseFloat(argumenty[6]),     // Etat
                        Double.parseDouble(argumenty[7]));  // Stawka
            } else {
                pracowniki[i] = new PracownikGodzinowy(
                        argumenty[1],
                        argumenty[2],
                        Integer.parseInt(argumenty[3]),
                        argumenty[4],
                        Integer.parseInt(argumenty[5]),
                        Double.parseDouble(argumenty[6]),   // Stawka
                        Integer.parseInt(argumenty[7]));    // Liczba godzin
            }
            System.arraycopy(pracowniki, 0, _pracowniki, 0, i++ + 1);
            pracowniki = _pracowniki;
        }

        pracowniki = Arrays.copyOf(pracowniki, pracowniki.length - 1);
        wyświetlTabelkę();
    }

    /**
     * Wyświetlenie tabelki Pracowników przez Iteratora.
     */
    static void wyświetlTabelkę() {
        System.out.println("\n------------------------------------------------------------------------------------------------------------------");
        System.out.printf("| %-20s | %-20s | %-15s | %-20s | %-10s | %-10s |\n", "Nazwisko", "Imię", "Pesel", "Stanowisko", "Staż", "Pensja");
        System.out.println("------------------------------------------------------------------------------------------------------------------");
        Firma firma = new Firma(pracowniki);
        while (!firma.isDone()) {
            firma.next();
        }
        System.out.print("------------------------------------------------------------------------------------------------------------------");
    }
}
