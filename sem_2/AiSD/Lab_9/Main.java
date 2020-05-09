package Lab_9;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String e = scanner.nextLine();

        String rpn = new RPNConverter().convert(e);
        RPNTree tree = new Converter().convert(rpn);

        System.out.print("Drzewo: ");
        tree.printHorizontally();

        System.out.print("\nInfix: ");
        tree.printInOrder();

        System.out.print("\nPostfiks: ");
        tree.printPostOrder();

        System.out.println("\nLiscia: " + tree.leafs());
        System.out.println("Wierzcholky: " + tree.nodes());
        System.out.println("Wysokosc: " + tree.height());

        System.out.println("Wynik: " + tree.solve());
    }
}