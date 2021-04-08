package pl.edu.pwr.ztw.services;

import org.springframework.stereotype.Service;
import pl.edu.pwr.ztw.data.Books;
import pl.edu.pwr.ztw.data.Readers;
import pl.edu.pwr.ztw.models.Book;
import pl.edu.pwr.ztw.models.Reader;

@Service
public class ReaderService implements IReaderService {
    @Override
    public Book rentBook(int bookId, int readerId) {
        Book book = Books.findById(bookId);
        if (book == null) {
            return null;
        }
        Reader reader = Readers.findById(readerId);
        if (reader == null) {
            return null;
        }
        reader.addBook(book);
        return null;
    }

    @Override
    public Book returnBook(int bookId, int readerId) {
        Book book = Books.findById(bookId);
        if (book == null) {
            return null;
        }
        Reader reader = Readers.findById(readerId);
        if (reader == null) {
            return null;
        }
        Readers.returnBook(reader, book);
        return null;
    }
}
