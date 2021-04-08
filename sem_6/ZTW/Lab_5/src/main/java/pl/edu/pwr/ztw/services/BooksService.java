package pl.edu.pwr.ztw.services;

import org.springframework.stereotype.Service;
import pl.edu.pwr.ztw.data.Books;
import pl.edu.pwr.ztw.models.Book;

import java.util.Collection;
import java.util.Optional;

@Service
public class BooksService implements IBooksService {

    @Override
    public Collection<Book> getBooks() {
        return Books.getBooksRepo();
    }

    @Override
    public Book getBook(int id) {
        return Books.getBooksRepo().stream()
                .filter(b -> b.getId() == id)
                .findAny()
                .orElse(null);
    }

    @Override
    public Book addBook(String title, int pages, int authorId) {
        Book book = new Book(Books.getBooksRepo().size() + 1, title, pages, authorId);
        Books.addBookToRepo(book);
        return book;
    }

    @Override
    public Book updateBook(int id, String title, int pages, int authorId) {
        Optional<Book> res = Books.getBooksRepo().stream().filter(b -> b.getId() == id).findFirst();
        if (res.isPresent()) {
            Book book = res.get();
            book.setTitle(title);
            book.setPages(pages);
            book.setAuthor(authorId);
//            TODO: use patch
            return book;
        }
        return null;
    }

    @Override
    public Book deleteBook(int id) {
        Optional<Book> book = Books.getBooksRepo().stream().filter(b -> b.getId() == id).findFirst();
        if (book.isEmpty()) {
            return null;
        }
        Books.removeById(id);
        return book.get();
    }
}
