package Lab_7;

public class Main {
    public static void main(String[] args) {
        System.out.printf("%30s |  Insert  |  Bubble  |  Select  |   Heap   |   Quick   |    Merge\n", "");
        for (int i = 0; i < 97; i++)
            System.out.print("-");

        System.out.printf("\n%30s |", "Dane losowe");
        new Sortowanie(0);

        System.out.printf("\n%30s |", "Dane posortowane rosnąco");
        new Sortowanie(1);

        System.out.printf("\n%30s |", "Dane posortowane malejąco");
        new Sortowanie(2);
    }
}
