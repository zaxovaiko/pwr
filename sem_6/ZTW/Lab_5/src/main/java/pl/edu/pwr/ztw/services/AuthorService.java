package pl.edu.pwr.ztw.services;

import org.springframework.stereotype.Service;
import pl.edu.pwr.ztw.models.Author;
import pl.edu.pwr.ztw.models.Book;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

@Service
public class AuthorService implements IAuthorService {

    private static List<Author> authorsRepo = new ArrayList<>();

    @Override
    public Collection<Author> getAuthors() {
        return authorsRepo;
    }

    @Override
    public Author getAuthor(int id) {
        return authorsRepo.stream().filter(a -> a.getId() == id).findFirst().orElse(null);
    }

    @Override
    public Author updateAuthor(int id, String firstName, String lastName, int age) {
        Author author = authorsRepo.stream().filter(a -> a.getId() == id).findFirst().orElse(null);
        if (author == null) {
            return null;
        }
        author.setFirstName(firstName);
        author.setLastName(lastName);
        author.setAge(age);
        return author;
    }

    @Override
    public Author deleteAuthor(int id) {
        Author author = authorsRepo.stream().filter(a -> a.getId() == id).findFirst().orElse(null);
        if (author == null) {
            return null;
        }
        authorsRepo.removeIf(a -> a.getId() == id);
        return author;
    }

    @Override
    public Author addAuthor(String firstName, String lastName, int age) {
        Author author = new Author(authorsRepo.size() + 1, firstName, lastName, age, new ArrayList<>());
        authorsRepo.add(author);
        return author;
    }

    @Override
    public Book addBook(int id, Book book) {
        Author author = authorsRepo.stream().filter(a -> a.getId() == id).findFirst().orElse(null);
        if (author == null) {
            return null;
        }
        author.addBook(book);
        return book;
    }
}
