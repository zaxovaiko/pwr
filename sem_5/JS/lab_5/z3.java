import java.io.FileNotFoundException;
import java.io.File;
import java.util.Scanner;
import java.lang.Integer;
import java.lang.NumberFormatException;

public class z3 {
    public static void main(String[] args) {
        try {
            int sum = 0;
            Scanner scInput = new Scanner(System.in);
            Scanner sc = new Scanner(new File("Covid.txt"));
            
            System.out.print("Enter country: ");
            String country = scInput.next();

            long t = System.nanoTime();
            while (sc.hasNextLine()) {
                String data = sc.nextLine();
                try {
                    String[] arr = data.split("\t");
                    if (country.equals(arr[6])) {
                        sum += Integer.parseInt(arr[4]);
                    }
                } catch (NumberFormatException err) {}
            }

            System.out.println(sum);
            System.out.println((System.nanoTime() - t) / 1_000_000_000.0);
            sc.close();
        } catch (FileNotFoundException e) {
            System.out.println("File not found");
        }
    }
}