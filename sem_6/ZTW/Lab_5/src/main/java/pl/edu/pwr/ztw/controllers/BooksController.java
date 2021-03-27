package pl.edu.pwr.ztw.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import pl.edu.pwr.ztw.services.IBooksService;
import pl.edu.pwr.ztw.validators.BookValidator;

@RestController
public class BooksController {
    @Autowired
    IBooksService booksService;

    @RequestMapping(value = "/books", method = RequestMethod.GET)
    public ResponseEntity<Object> getBooks(){
        return new ResponseEntity<>(booksService.getBooks(), HttpStatus.OK);
    }

    @RequestMapping(value = "/books/{id}", method = RequestMethod.GET)
    public ResponseEntity<Object> getBook(@PathVariable("id") int id){
        return new ResponseEntity<>(booksService.getBook(id), HttpStatus.OK);
    }

    @RequestMapping(value = "/books/{id}", method = RequestMethod.PUT)
    public ResponseEntity<Object> updateBook(@PathVariable("id") int id, String title, int pages, int authorId){
        title = title.strip();
        if (BookValidator.isValidBook(title, pages, authorId)) {
            return new ResponseEntity<>("Invalid data", HttpStatus.NOT_ACCEPTABLE);
        }
        return new ResponseEntity<>(booksService.updateBook(id, title, pages, authorId), HttpStatus.OK);
    }

    @RequestMapping(value = "/books/{id}", method = RequestMethod.DELETE)
    public ResponseEntity<Object> deleteBook(@PathVariable("id") int id){
        return new ResponseEntity<>(booksService.deleteBook(id), HttpStatus.OK);
    }

    @RequestMapping(value = "/books", method = RequestMethod.POST)
    public ResponseEntity<Object> addBook(String title, int pages, int authorId){
        title = title.strip();
        if (BookValidator.isValidBook(title, pages, authorId)) {
            return new ResponseEntity<>("Invalid data", HttpStatus.NOT_ACCEPTABLE);
        }
        return new ResponseEntity<>(booksService.addBook(title, pages, authorId), HttpStatus.OK);
    }
}