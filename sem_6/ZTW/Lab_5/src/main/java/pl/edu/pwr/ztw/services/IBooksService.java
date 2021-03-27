package pl.edu.pwr.ztw.services;

import pl.edu.pwr.ztw.models.Book;

import java.util.Collection;

public interface IBooksService {
    public abstract Collection<Book> getBooks();
    public abstract Book getBook(int id);
    public abstract Book addBook(String title, int pages, int authorId);
    public abstract Book updateBook(int id, String title, int pages, int authorId);
    public abstract Book deleteBook(int id);
}
