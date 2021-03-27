package pl.edu.pwr.ztw.validators;

public class BookValidator {
    public static boolean isValidBook(String title, int pages, int authorId) {
        return title.equals("") || pages <= 0 || authorId <= 0;
    }
}
