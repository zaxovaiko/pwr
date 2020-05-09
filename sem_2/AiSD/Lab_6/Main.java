package Lab_6;

import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException, ClassNotFoundException {
        Scanner scanner = new Scanner(System.in);
        System.out.println("1. Utworzenie nowej bazy danych\n" +
                "2. Odczyt bazy z pliku\n" +
                "3. Wyświetlenie wszystkich rekordów\n" +
                "4. Wyświetlenie danych jednego pracownika\n" +
                "5. Dopisanie nowego pracownika\n" +
                "6. Usunięcie pracownika z bazy\n" +
                "7. Aktualizowanie danych pracownika\n" +
                "8. Zapis bazy do pliku\n" +
                "9. Wyswietlić śriednią pensję\n" +
                "10. Zakończyć program\n"
        );

        BazaDanych db = new BazaDanych();

        while (true) {
            String command = scanner.next();
            switch (command) {
                case "1":
                    db = new BazaDanych();
                    break;
                case "2":
                    db.read();
                    break;
                case "3":
                    db.showAll();
                    break;
                case "4":
                    System.out.println("Wprowadz PESEL: ");
                    db.show(scanner.nextInt());
                    break;
                case "5":
                    db.add(new Pracownik());
                    break;
                case "6":
                    System.out.println("Wprowadz PESEL do usuniecia: ");
                    db.remove(scanner.nextInt());
                    break;
                case "7":
                    System.out.println("Wprowadz PESEL do aktualizacji: ");
                    db.update(scanner.nextInt(), new Pracownik());
                    break;
                case "8":
                    db.write();
                    break;
                case "9":
                    db.averagePensja();
                    break;
                default:
                    return;
            }
        }
    }
}