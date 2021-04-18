package pl.edu.pwr.ztw.models;

public class Book {
    private Integer id;
    private String title;
    private Integer authorId;
    private Integer pages;

    public Book(Integer id, String title, Integer pages, Integer authorId) {
        this.id = id;
        this.title = title;
        this.authorId = authorId;
        this.pages = pages;
    }

    public Integer getId() {
        return id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public Integer getAuthor() {
        return authorId;
    }

    public void setAuthor(Integer author) {
        this.authorId = author;
    }

    public Integer getPages() {
        return pages;
    }

    public void setPages(Integer pages) {
        this.pages = pages;
    }
}
