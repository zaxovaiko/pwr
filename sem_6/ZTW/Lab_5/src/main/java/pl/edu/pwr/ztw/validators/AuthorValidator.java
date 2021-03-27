package pl.edu.pwr.ztw.validators;

public class AuthorValidator {
    public static boolean isValidAuthor(String firstName, String lastName, int age) {
        return firstName.equals("") || lastName.equals("") || age <= 0 || age >= 140;
    }
}
