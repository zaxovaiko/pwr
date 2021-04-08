package pl.edu.pwr.ztw.services;

import pl.edu.pwr.ztw.models.Book;

public interface IReaderService {
    public abstract Book rentBook(int bookId, int readerId);
    public abstract Book returnBook(int bookId, int readerId);
}