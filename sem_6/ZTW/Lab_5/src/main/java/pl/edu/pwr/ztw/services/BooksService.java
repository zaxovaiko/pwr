package pl.edu.pwr.ztw.services;

import org.springframework.stereotype.Service;
import pl.edu.pwr.ztw.models.Book;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.Optional;

@Service
public class BooksService implements IBooksService {
    private static List<Book> booksRepo = new ArrayList<>();

    static {
        booksRepo.add(new Book(1,"Potop", 936, 1));
        booksRepo.add(new Book(2,"Wesele", 150, 2));
        booksRepo.add(new Book(3,"Dziady", 292, 3));
    }

    @Override
    public Collection<Book> getBooks() {
        return booksRepo;
    }

    @Override
    public Book getBook(int id) {
        return booksRepo.stream()
                .filter(b -> b.getId() == id)
                .findAny()
                .orElse(null);
    }

    @Override
    public Book addBook(String title, int pages, int authorId) {
        Book book = new Book(booksRepo.size() + 1, title, pages, authorId);
        booksRepo.add(book);
        return book;
    }

    @Override
    public Book updateBook(int id, String title, int pages, int authorId) {
        Optional<Book> res = booksRepo.stream().filter(b -> b.getId() == id).findFirst();
        if (res.isPresent()) {
            Book book = res.get();
            book.setTitle(title);
            book.setPages(pages);
            book.setAuthor(authorId);
            return book;
        }
        return null;
    }

    @Override
    public Book deleteBook(int id) {
        Optional<Book> book = booksRepo.stream().filter(b -> b.getId() == id).findFirst();
        if (book.isEmpty()) {
            return null;
        }
        booksRepo.removeIf(b -> b.getId() == id);
        return book.get();
    }
}
