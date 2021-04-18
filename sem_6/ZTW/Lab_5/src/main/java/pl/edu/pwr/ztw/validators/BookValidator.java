package pl.edu.pwr.ztw.validators;

public class BookValidator {
    public static boolean isValidBook(String title, Integer pages, Integer authorId) {
        return title.equals("") || pages <= 0 || authorId <= 0;
    }
}
