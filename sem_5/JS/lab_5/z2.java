import java.io.FileNotFoundException;
import java.io.File;
import java.util.Scanner;
import java.lang.Integer;
import java.lang.NumberFormatException;

public class z2 {
    public static void main(String[] args) {
        try {
            int sum = 0;
            Scanner sc = new Scanner(new File("Covid.txt"));
            
            long t = System.nanoTime();
            while (sc.hasNextLine()) {
                String data = sc.nextLine();
                try {
                    sum += Integer.parseInt(data.split("\t")[4]);
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