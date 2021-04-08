package pl.edu.pwr.ztw.data;

import pl.edu.pwr.ztw.models.Book;
import pl.edu.pwr.ztw.models.Reader;

import java.util.ArrayList;
import java.util.List;

public class Readers {
    private static List<Reader> readersRepo = new ArrayList<>();

    static {
        readersRepo.add(new Reader(1, "Adam", "Kowalski"));
        readersRepo.add(new Reader(2, "Weronika", "Dynka"));
    }

    public static Reader findById(int id) {
        for (Reader r: readersRepo) {
            if (r.getId() == id) {
                return r;
            }
        }
        return null;
    }

    public static void returnBook(Reader reader, Book book) {
        reader.removeBook(book);
    }

    public static boolean addBook(Book book, int readerId) {
        for (Reader r: readersRepo) {
            if (r.getId() == readerId) {
                r.addBook(book);
                return true;
            }
        }
        return false;
    }
}
