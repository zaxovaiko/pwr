package pl.edu.pwr.ztw.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import pl.edu.pwr.ztw.services.IReaderService;

@RestController
public class ReaderController {
    @Autowired
    IReaderService readerService;

    @RequestMapping(value = "/books/rent", method = RequestMethod.POST)
    public ResponseEntity<Object> getBooks(int bookId, int readerId) {
        return new ResponseEntity<>(readerService.rentBook(bookId, readerId), HttpStatus.OK);
    }

    @RequestMapping(value = "/books/return", method = RequestMethod.POST)
    public ResponseEntity<Object> getBook(int bookId, int readerId){
        return new ResponseEntity<>(readerService.returnBook(bookId, readerId), HttpStatus.OK);
    }
}
