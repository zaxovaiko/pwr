package pl.edu.pwr.ztw.models;

public class Book {
    private int id;
    private String title;
    private int authorId;
    int pages;

    public Book(int id, String title, int pages, int authorId) {
        this.id = id;
        this.title = title;
        this.authorId = authorId;
        this.pages = pages;
    }

    public int getId() {
        return id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public int getAuthor() {
        return authorId;
    }

    public void setAuthor(int author) {
        this.authorId = author;
    }

    public int getPages() {
        return pages;
    }

    public void setPages(int pages) {
        this.pages = pages;
    }
}
