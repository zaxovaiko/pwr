package Lab_5;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        reverse();
        run();
    }

    static void reverse() throws Exception {
        System.out.println("Wprowadź ONP wyrażenie:");
        Scanner scanner = new Scanner(System.in);
        InfixtoPostfix converter = new InfixtoPostfix();
        System.out.println("Tradycyjne wyrażenie: " + converter.reverseConvert(scanner.nextLine()));
        System.out.println();
    }

    static void run() throws Exception {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Wpisz wyrażenie i zatwierdź enterem:");
        while (scanner.hasNext()) {
            InfixtoPostfix converter = new InfixtoPostfix();
            String expresion = scanner.next();

            try {
                String onpExpression = converter.convert(expresion);
                System.out.println(expresion + " == " + onpExpression);
                System.out.println(converter.calc());
            } catch (Exception e) {
                e.printStackTrace();
            }

            System.out.println("Wpisz wyrażenie i zatwierdź enterem");
        }
    }
}
