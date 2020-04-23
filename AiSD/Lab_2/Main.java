package Lab_2;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Menu menu       = new Menu();

        int act;
        System.out.println("1 - Utworzyć listę");
        System.out.println("2 - Wyświetlić liczbę elementów");
        System.out.println("3 - Wyświetlić listę");
        System.out.println("4 - Wyświetlić karty o wartości");
        System.out.println("5 - Wyświetlić karty o kolorze");
        System.out.println("6 - Usunuć powtarzające");
        System.out.println("7 - Wyjść z programy");
        System.out.println("8 - Ilość zakrytych i odkrytych kart");

        while ((act = scanner.nextInt()) != 7) {
            switch (act) {
                case 1: menu.utworzyćListę(); break;
                case 2: menu.wyświetlićLiczbęElementów(); break;
                case 3: menu.wyświetlićListę(); break;
                case 4: menu.wyświetlenieKartoWartości(scanner.next()); break;
                case 5: menu.wyświetlenieKartoKolorze(scanner.next()); break;
                case 6: menu.usunućPowtarzające(); break;
                case 8: menu.ilośćOdkrytychiZakrytychKart(); break;
            }
        }
    }
}
